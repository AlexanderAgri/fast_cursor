# FastAPI Simple Project

Una API REST simple y eficiente construida con FastAPI para la gestión de platos de un menú.

## 📋 Descripción

Este proyecto implementa una API RESTful para gestionar platos de un restaurante, proporcionando operaciones CRUD completas (Crear, Leer, Actualizar, Eliminar) junto con funcionalidades adicionales como estadísticas del menú.

## 🚀 Características

- **CRUD completo** para gestión de platos
- **Validación de datos** con Pydantic
- **Documentación automática** con Swagger UI y ReDoc
- **Configuración flexible** mediante variables de entorno
- **Endpoints de salud** para monitoreo
- **Estadísticas del menú** con cálculos automáticos
- **Manejo de errores** con códigos HTTP apropiados

## 🛠️ Tecnologías

- **FastAPI** - Framework web moderno y rápido
- **Pydantic** - Validación de datos y serialización
- **Uvicorn** - Servidor ASGI para desarrollo y producción
- **Python 3.8+** - Lenguaje de programación

## 📦 Instalación

### Prerrequisitos

- Python 3.8 o superior
- uv (recomendado) o pip

### Pasos de instalación

1. **Clonar el repositorio**

   ```bash
   git clone <repository-url>
   cd fast_api
   ```

2. **Instalar dependencias**

   Con uv (recomendado):

   ```bash
   uv sync
   ```

   Con pip:

   ```bash
   pip install -e .
   ```

3. **Instalar dependencias de desarrollo** (opcional)
   ```bash
   uv sync --dev
   # o con pip:
   pip install -e ".[dev]"
   ```

## 🏃‍♂️ Uso

### Ejecutar el servidor de desarrollo

```bash
# Método 1: Ejecutar directamente
python main.py

# Método 2: Usar uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

El servidor estará disponible en: http://localhost:8000

### Documentación de la API

Una vez que el servidor esté ejecutándose, puedes acceder a:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📡 Endpoints de la API

### Endpoints básicos

| Método | Endpoint  | Descripción                      |
| ------ | --------- | -------------------------------- |
| `GET`  | `/`       | Mensaje de bienvenida            |
| `GET`  | `/health` | Estado de salud de la aplicación |

### Endpoints de platos

| Método   | Endpoint             | Descripción                       |
| -------- | -------------------- | --------------------------------- |
| `POST`   | `/platos/`           | Crear un nuevo plato              |
| `GET`    | `/platos/`           | Obtener todos los platos          |
| `GET`    | `/platos/{plato_id}` | Obtener un plato específico       |
| `PUT`    | `/platos/{plato_id}` | Actualizar un plato completo      |
| `PATCH`  | `/platos/{plato_id}` | Actualización parcial de un plato |
| `DELETE` | `/platos/{plato_id}` | Eliminar un plato                 |

### Endpoints adicionales

| Método | Endpoint                | Descripción                   |
| ------ | ----------------------- | ----------------------------- |
| `GET`  | `/platos/stats/summary` | Obtener estadísticas del menú |

## 💾 Modelos de datos

### Plato (Modelo completo)

```json
{
  "id": 1,
  "name": "Paella Valenciana",
  "precio": 15.5
}
```

### PlatoCreate (Para crear platos)

```json
{
  "name": "Paella Valenciana",
  "precio": 15.5
}
```

### PlatoUpdate (Para actualizar platos)

```json
{
  "name": "Paella Valenciana Actualizada",
  "precio": 18.0
}
```

## 📊 Ejemplos de uso

### Crear un plato

```bash
curl -X POST "http://localhost:8000/platos/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Gazpacho Andaluz",
    "precio": 8.50
  }'
```

### Obtener todos los platos

```bash
curl -X GET "http://localhost:8000/platos/"
```

### Obtener estadísticas

```bash
curl -X GET "http://localhost:8000/platos/stats/summary"
```

Respuesta ejemplo:

```json
{
  "total_platos": 5,
  "precio_promedio": 12.3,
  "precio_minimo": 8.5,
  "precio_maximo": 18.0
}
```

## ⚙️ Configuración

El proyecto utiliza variables de entorno para la configuración. Puedes crear un archivo `.env` en la raíz del proyecto:

```env
# Configuración de la aplicación
APP_NAME=Mi Restaurante API
DEBUG=true
HOST=0.0.0.0
PORT=8000

# Configuración opcional
DATABASE_URL=sqlite:///./database.db
SECRET_KEY=tu-clave-secreta-aqui
```

### Variables de configuración disponibles

| Variable       | Descripción             | Valor por defecto        |
| -------------- | ----------------------- | ------------------------ |
| `APP_NAME`     | Nombre de la aplicación | "FastAPI Simple Project" |
| `DEBUG`        | Modo debug              | `true`                   |
| `HOST`         | Host del servidor       | "0.0.0.0"                |
| `PORT`         | Puerto del servidor     | 8000                     |
| `DATABASE_URL` | URL de base de datos    | `None`                   |
| `SECRET_KEY`   | Clave secreta           | "your-secret-key-here"   |

## 🧪 Testing

Para ejecutar las pruebas (cuando estén disponibles):

```bash
# Con uv
uv run pytest

# Con pip
pytest
```

## 📁 Estructura del proyecto

```
fast_api/
├── main
```
