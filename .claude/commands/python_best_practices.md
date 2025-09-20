# Python 3.12 Type Hints Formatting Instructions

## Core Principles

- Always use the most modern Python 3.12 type hint syntax
- Prefer built-in generics over typing module equivalents when available
- Use `type` statement for type aliases (PEP 695)
- Use generic type parameter syntax for generic classes and functions (PEP 695)

## 1. Built-in Generics (Python 3.9+, enforced in 3.12)

### USE (Modern Python 3.12):

```python
def process_items(items: list[str]) -> dict[str, int]:
    pass

def merge_data(data1: dict[str, Any], data2: dict[str, Any]) -> dict[str, Any]:
    pass

def get_first(items: list[str | int]) -> str | int | None:
    pass
```

### DON'T USE (Legacy):

```python
from typing import List, Dict, Optional, Union

def process_items(items: List[str]) -> Dict[str, int]:
    pass

def get_first(items: List[Union[str, int]]) -> Optional[Union[str, int]]:
    pass
```

## 2. Union Types with | Operator (Python 3.10+)

### USE:

```python
def handle_value(value: str | int | None) -> bool:
    pass

def process_data(data: dict[str, str | int | float]) -> list[str]:
    pass
```

### DON'T USE:

```python
from typing import Union, Optional

def handle_value(value: Union[str, int, None]) -> bool:
    pass

def handle_value(value: Optional[Union[str, int]]) -> bool:
    pass
```

## 3. Type Aliases with `type` Statement (PEP 695)

### USE (Python 3.12):

```python
type UserID = int
type UserData = dict[str, str | int]
type ProcessingResult = tuple[bool, str, list[str]]
type JSONValue = dict[str, Any] | list[Any] | str | int | float | bool | None

def get_user(user_id: UserID) -> UserData:
    pass
```

### DON'T USE:

```python
from typing import TypeAlias

UserID: TypeAlias = int
UserData: TypeAlias = dict[str, str | int]
# or
UserID = int  # without type annotation
```

## 4. Generic Classes and Functions (PEP 695)

### USE (Python 3.12):

```python
class Container[T]:
    def __init__(self, value: T) -> None:
        self.value = value

    def get(self) -> T:
        return self.value

class Repository[T, K]:
    def find_by_id(self, id: K) -> T | None:
        pass

    def save(self, entity: T) -> K:
        pass

def first[T](items: list[T]) -> T | None:
    return items[0] if items else None

def transform[T, U](items: list[T], func: Callable[[T], U]) -> list[U]:
    return [func(item) for item in items]
```

### DON'T USE:

```python
from typing import TypeVar, Generic

T = TypeVar('T')
K = TypeVar('K')

class Container(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
```

## 5. Protocol and Structural Typing

### USE:

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

class Serializable(Protocol):
    def serialize(self) -> dict[str, Any]: ...

def render_shape(shape: Drawable) -> None:
    shape.draw()
```

## 6. Literal Types

### USE:

```python
from typing import Literal

type Status = Literal["pending", "completed", "failed"]
type HttpMethod = Literal["GET", "POST", "PUT", "DELETE"]

def update_status(new_status: Status) -> None:
    pass

def make_request(method: HttpMethod, url: str) -> dict[str, Any]:
    pass
```

## 7. Advanced Patterns

### Callable Types:

```python
from collections.abc import Callable

type EventHandler = Callable[[str, dict[str, Any]], None]
type Validator[T] = Callable[[T], bool]

def register_handler(event: str, handler: EventHandler) -> None:
    pass
```

### Async Functions:

```python
from collections.abc import Awaitable, Coroutine

async def fetch_data(url: str) -> dict[str, Any]:
    pass

type AsyncProcessor[T] = Callable[[T], Awaitable[bool]]
```

### Context Managers:

```python
from collections.abc import Generator
from contextlib import contextmanager

@contextmanager
def database_transaction() -> Generator[None, None, None]:
    # setup
    try:
        yield
    finally:
        # cleanup
        pass
```

## 8. Import Guidelines

### Prefer these imports for Python 3.12:

```python
# Built-in types (no import needed)
list, dict, tuple, set, frozenset

# Standard library
from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from typing import Any, Literal, Protocol, Final, ClassVar
```

### Avoid these legacy imports:

```python
# Don't use these in Python 3.12
from typing import List, Dict, Tuple, Set, Union, Optional, Callable
```

## 9. Complete Example

```python
from typing import Any, Literal, Protocol
from collections.abc import Callable, Sequence

# Type aliases using new syntax
type UserID = int
type UserRole = Literal["admin", "user", "guest"]
type JSONData = dict[str, Any]

# Protocol definition
class Persistable(Protocol):
    def save(self) -> bool: ...
    def delete(self) -> bool: ...

# Generic class
class Repository[T: Persistable]:
    def __init__(self, items: list[T]) -> None:
        self._items = items

    def find_by_condition(self, predicate: Callable[[T], bool]) -> list[T]:
        return [item for item in self._items if predicate(item)]

    def save_all(self) -> bool:
        return all(item.save() for item in self._items)

# Generic function
def batch_process[T](
    items: Sequence[T],
    processor: Callable[[T], bool]
) -> tuple[list[T], list[T]]:
    """Process items and return successful and failed ones."""
    successful: list[T] = []
    failed: list[T] = []

    for item in items:
        if processor(item):
            successful.append(item)
        else:
            failed.append(item)

    return successful, failed

# Usage with modern type hints
def handle_user_data(
    user_id: UserID,
    role: UserRole,
    data: JSONData
) -> dict[str, str | int]:
    return {"id": user_id, "role": role, "processed": len(data)}
```

## Formatting Commands Summary

1. **Replace legacy typing imports**: Remove `List`, `Dict`, `Union`, `Optional` imports
2. **Use built-in generics**: `list[T]` instead of `List[T]`
3. **Use union operator**: `str | int` instead of `Union[str, int]`
4. **Use type statement**: `type Alias = SomeType` instead of `Alias: TypeAlias = SomeType`
5. **Use PEP 695 generics**: `class Foo[T]:` instead of `class Foo(Generic[T]):`
6. **Prefer collections.abc**: Import `Callable` from `collections.abc` not `typing`
7. **Use Literal for constants**: `Literal["value"]` for string/int constants
8. **Type all function signatures**: Include return type annotations
9. **Use Protocol for structural typing**: Instead of ABC when appropriate
