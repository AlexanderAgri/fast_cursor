"""
Pydantic Schemas for FastAPI Application
"""
from pydantic import BaseModel, Field
from typing import Optional


class Plato(BaseModel):
    """Model to represent a dish from the menu"""
    id: int = Field(..., description="Unique dish ID", example=1)
    name: str = Field(..., min_length=1, max_length=100, description="Dish name", example="Paella Valenciana")
    precio: float = Field(..., gt=0, description="Dish price in euros", example=15.50)
    
    class Config:
        """Model configuration"""
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Paella Valenciana",
                "precio": 15.50
            }
        }


class PlatoCreate(BaseModel):
    """Model to create a new dish"""
    name: str = Field(..., min_length=1, max_length=100, description="Dish name", example="Paella Valenciana")
    precio: float = Field(..., gt=0, description="Dish price", example=15.50)
    
    class Config:
        """Model configuration"""
        json_schema_extra = {
            "example": {
                "name": "Paella Valenciana",
                "precio": 15.50
            }
        }


class PlatoUpdate(BaseModel):
    """Model to update an existing dish"""
    name: Optional[str] = Field(None, min_length=1, max_length=100, description="Dish name")
    precio: Optional[float] = Field(None, gt=0, description="Dish price")
    
    class Config:
        """Model configuration"""
        json_schema_extra = {
            "example": {
                "name": "Paella Valenciana Actualizada",
                "precio": 18.00
            }
        }
