"""
Definition: A data type tells Python what kind of value an object represents and what operations can be performed on it.
            Python is dynamically typed, meaning you don't have to declare the type yourself.
"""
"""
| Category | Data types                         |
| -------- | ---------------------------------- |
| Numeric  | `int`, `float`, `complex`          |
| Boolean  | `bool`                             |
| Text     | `str`                              |
| Sequence | `list`, `tuple`, `range`           |
| Mapping  | `dict`                             |
| Set      | `set`, `frozenset`                 |
| Binary   | `bytes`, `bytearray`, `memoryview` |
| Special  | `NoneType`                         |
"""

"""
Mutable vs Immutable

Immutable types
int, float, complex, bool, str, tuple, range, frozenset, bytes

Mutable types
list, dict, set, bytearray

"""

#checking data types
data = 12
print(type(data))
print(isinstance(data,int))

"""
conceptual model
Variable/name
      │
      ▼
    Object
      │
      ├── value
      └── type
"""
#Type Conversion / Type Casting
a = "12"
print(type(a))
a = int(a)
print(type(a))
b = 12
c = float(b)
print(c)