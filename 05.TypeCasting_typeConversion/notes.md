# Python Type Casting and Type Conversion – Complete Interview Notes

First, understand one important difference.

## 1. Type Casting vs Type Conversion

Both mean changing one data type into another.

| Type            | Meaning                                                                            |
| --------------- | ---------------------------------------------------------------------------------- |
| Type Conversion | Python automatically changes the type in certain operations.                       |
| Type Casting    | We manually convert a value using functions like `int()`, `float()`, `str()`, etc. |

Example:

```
# Automatic type conversion
a = 10
b = 2.5
print(a + b)  # 12.5
print(type(a + b))  # float
```

Why? Python converts `int` into `float` because one operand is a float.

```
# Manual type casting
a = "100"
b = int(a)
print(b)        # 100
print(type(b))  # int
```

Why? We explicitly used `int()` to convert a string into an integer.

## 2. Important Type Casting Functions

Remember these functions:

| Function    | Converts into | Example                         |
| ----------- | ------------- | ------------------------------- |
| `int()`     | Integer       | `int("10")` → `10`              |
| `float()`   | Float         | `float("10")` → `10.0`          |
| `str()`     | String        | `str(10)` → `"10"`              |
| `bool()`    | Boolean       | `bool(1)` → `True`              |
| `list()`    | List          | `list("abc")` → `['a','b','c']` |
| `tuple()`   | Tuple         | `tuple([1,2])` → `(1,2)`        |
| `set()`     | Set           | `set([1,1,2])` → `{1,2}`        |
| `dict()`    | Dictionary    | `dict([("a",1)])` → `{'a':1}`   |
| `complex()` | Complex       | `complex(10)` → `(10+0j)`       |

Interview rule: Type casting does not always modify the original variable. Usually, it returns a new value.

```
a = "100"
int(a)
print(a)  # "100"
print(type(a))  # str
```

Why? We converted the value but did not store the result.

Correct:

```
a = "100"
a = int(a)
print(a)  # 100
```










