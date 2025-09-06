"""
FastAPI Application - Platos CRUD API
"""
from fastapi import FastAPI, HTTPException, status
from typing import List, Dict
from settings import settings
from schemas import Plato, PlatoCreate, PlatoUpdate

# Create the FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)

# In-memory simulated database
platos_db: Dict[int, Plato] = {}
next_id = 1

# Basic application routes
@app.get("/")
async def root():
    """Main route"""
    return {"message": "Welcome to the Dishes API!", "status": "running"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION
    }

# CRUD Endpoints for Dishes

@app.post("/platos/", response_model=Plato, status_code=status.HTTP_201_CREATED)
async def create_plato(plato: PlatoCreate):
    """
    Create a new dish
    
    - **name**: Dish name (required)
    - **precio**: Dish price in euros (must be greater than 0)
    """
    global next_id
    
    new_plato = Plato(
        id=next_id,
        name=plato.name,
        precio=plato.precio
    )
    
    platos_db[next_id] = new_plato
    next_id += 1
    
    return new_plato

@app.get("/platos/", response_model=List[Plato])
async def get_all_platos():
    """
    Get all dishes
    
    Returns a list with all available dishes in the menu
    """
    return list(platos_db.values())

@app.get("/platos/{plato_id}", response_model=Plato)
async def get_plato(plato_id: int):
    """
    Get a specific dish by its ID
    
    - **plato_id**: Unique dish ID
    """
    if plato_id not in platos_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Dish with ID {plato_id} not found"
        )
    
    return platos_db[plato_id]

@app.put("/platos/{plato_id}", response_model=Plato)
async def update_plato(plato_id: int, plato_update: PlatoUpdate):
    """
    Update an existing dish
    
    - **plato_id**: Unique ID of the dish to update
    - **name**: New dish name (optional)
    - **precio**: New dish price (optional)
    """
    if plato_id not in platos_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Dish with ID {plato_id} not found"
        )
    
    existing_plato = platos_db[plato_id]
    update_data = plato_update.model_dump(exclude_unset=True)
    
    # Update only the provided fields
    for field, value in update_data.items():
        setattr(existing_plato, field, value)
    
    platos_db[plato_id] = existing_plato
    return existing_plato

@app.patch("/platos/{plato_id}", response_model=Plato)
async def patch_plato(plato_id: int, plato_update: PlatoUpdate):
    """
    Partial update of a dish (PUT alias)
    
    - **plato_id**: Unique ID of the dish to update
    - **name**: New dish name (optional)
    - **precio**: New dish price (optional)
    """
    return await update_plato(plato_id, plato_update)

@app.delete("/platos/{plato_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_plato(plato_id: int):
    """
    Delete a dish from the menu
    
    - **plato_id**: Unique ID of the dish to delete
    """
    if plato_id not in platos_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Dish with ID {plato_id} not found"
        )
    
    del platos_db[plato_id]
    return None

# Additional endpoint to get statistics
@app.get("/platos/stats/summary")
async def get_platos_stats():
    """
    Get menu statistics
    
    Returns statistical information about available dishes
    """
    if not platos_db:
        return {
            "total_platos": 0,
            "precio_promedio": 0,
            "precio_minimo": 0,
            "precio_maximo": 0
        }
    
    precios = [plato.precio for plato in platos_db.values()]
    
    return {
        "total_platos": len(platos_db),
        "precio_promedio": round(sum(precios) / len(precios), 2),
        "precio_minimo": min(precios),
        "precio_maximo": max(precios)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
