# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

- **Run the development server**: `python main.py` or `uvicorn main:app --reload`
- **Install dependencies**: `uv sync` (using uv package manager)
- **Run tests**: `pytest` (requires dev dependencies)
- **Test coverage**: `pytest --cov` (if coverage plugin is installed)
- **Format code**: `ruff format` (code formatting)
- **Lint code**: `ruff check` (linting and code analysis)
- **Fix linting issues**: `ruff check --fix` (auto-fix linting issues)

## Architecture

This is a FastAPI application that implements a CRUD API for dishes (platos). The architecture follows these patterns:

### Core Components

- **main.py**: FastAPI application with all route handlers for platos CRUD operations
- **schemas.py**: Pydantic models for request/response validation (Plato, PlatoCreate, PlatoUpdate)
- **settings.py**: Application configuration using a Settings class with environment variable support

### Data Storage

- Uses in-memory storage (`platos_db` dictionary) for dish data
- Global `next_id` counter for ID generation
- No database integration currently implemented

### API Endpoints

- `GET /`: Welcome message
- `GET /health`: Health check endpoint
- `POST /platos/`: Create new dish
- `GET /platos/`: Get all dishes
- `GET /platos/{plato_id}`: Get specific dish
- `PUT /platos/{plato_id}`: Update dish
- `PATCH /platos/{plato_id}`: Partial update (alias for PUT)
- `DELETE /platos/{plato_id}`: Delete dish
- `GET /platos/stats/summary`: Get menu statistics

### Development Guidelines

The project follows these coding standards from Cursor rules:

- Use functional programming; avoid classes where possible
- Use type hints for all function signatures
- Prefer Pydantic models over raw dictionaries for input validation
- Use async def for asynchronous operations, def for pure functions
- Handle errors and edge cases at the beginning of functions
- Use early returns to avoid deeply nested if statements
- Document endpoints with clear descriptions and examples using docstrings
- Use proper HTTP status codes for responses
- Use ruff for code formatting and linting (configured in pyproject.toml)

### Dependencies

- FastAPI >= 0.104.0
- Uvicorn for ASGI server
- Pydantic for data validation
- Python >= 3.8
- Ruff >= 0.1.0 (dev dependency for formatting and linting)

### Testing

- Uses pytest with asyncio support
- Test files should be placed in `tests/` directory
- Async test mode is enabled in pytest configuration