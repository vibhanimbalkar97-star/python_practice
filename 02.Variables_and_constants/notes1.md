# Python Variables and Constants — Interview Revision Notes

## 1. What is a variable?

A variable is a name that refers to a value (object) in Python.

```
name = "Vibha"age = 25print(name)print(age)
```

Output:

```
Vibha
25
```

Here, `name` refers to `"Vibha"` and `age` refers to `25`.

## 2. Rules for naming variables

| Rule                                          | Example                       |
| --------------------------------------------- | ----------------------------- |
| Can contain letters                           | `name = "Sam"`                |
| Can contain numbers, but not at the beginning | `age2 = 25`                   |
| Can contain underscores                       | `user_name = "Sam"`           |
| Cannot start with a number                    | `2age = 25` ❌                 |
| Cannot contain spaces                         | `user name = "Sam"` ❌         |
| Case-sensitive                                | `age` and `Age` are different |
| Cannot use reserved keywords                  | `class = "Python"` ❌          |

Best practice: Use descriptive `snake_case` names.

```
first_name = "Vibha"total_price = 500
```

## 3. Variable declaration and assignment

Python doesn't require a separate variable declaration.

```
x = 10
```

- `x` — variable name.
- `=` — assignment operator.
- `10` — value assigned to `x`.

Unlike JavaScript, Python does not require `let`, `var`, or `const` to declare variables.

```
x = 10       # Assignmentx = 20       # Reassignmentx = x + 5    # Uses the old value and assigns a new valueprint(x)     # 25
```

## 4. Dynamic typing

Python is dynamically typed. You can assign values of different types to the same variable.

```
x = 10x = "Hello"x = 3.14print(x)         # 3.14print(type(x))   # <class 'float'>
```

The variable name `x` refers to a different value after each assignment.

## 5. Multiple variable assignments

Multiple assignment:

```
a, b, c = 10, 20, 30print(a, b, c)  # 10 20 30
```

Same value for multiple variables:

```
a = b = c = 100
```

All three names initially refer to the same integer object.

Swapping variables:

```
a = 10b = 20a, b = b, aprint(a, b)  # 20 10
```

Python allows swapping without a temporary variable.

## 6. Local and global variables

### Local variable

Created inside a function and normally accessible only within that function.

```
def test():    x = 10    print(x)test()  # 10# print(x)  # NameError
```

### Global variable

Created outside a function.

```
x = 10def test():    print(x)test()  # 10
```

### Modifying a global variable

Use `global` when you want to reassign a module-level variable inside a function.

```
x = 10def test():    global x    x = 20test()print(x)  # 20
```

Without `global`, assigning to `x` inside the function makes it a local variable.

## 7. The `nonlocal` keyword

`nonlocal` lets an inner function reassign a variable from its nearest enclosing function scope.

```
def outer():    x = 10    def inner():        nonlocal x        x = 20    inner()    print(x)outer()  # 20
```

- `global` — refers to a module-level name.
- `nonlocal` — refers to a name in an enclosing function scope.

## 8. Variable scope: LEGB rule

Python looks for a variable using the LEGB order.

| Scope         | Meaning                             |
| ------------- | ----------------------------------- |
| L — Local     | Inside the current function         |
| E — Enclosing | Inside an outer function            |
| G — Global    | At module level                     |
| B — Built-in  | Names such as `print()` and `len()` |

Example:

```
x = "Global"def outer():    x = "Enclosing"    def inner():        x = "Local"        print(x)    inner()outer()  # Local
```

Python finds the nearest matching variable first.

## 9. Mutable vs immutable objects

This is an important interview topic because variables refer to objects.

| Immutable objects | Mutable objects                    |
| ----------------- | ---------------------------------- |
| `int`             | `list`                             |
| `float`           | `dict`                             |
| `bool`            | `set`                              |
| `str`             | Most custom objects can be mutable |
| `tuple`\*         |                                    |

Tuples cannot have their elements reassigned, but a tuple can contain a mutable object.

Immutable example:

```
x = 10x = x + 1print(x)  # 11
```

Python creates/reuses an integer object for the new value and rebinds `x`; it does not modify the original integer.

Mutable example:

```
numbers = [1, 2]numbers.append(3)print(numbers)  # [1, 2, 3]
```

The existing list is modified.

## 10. Variables and object references

Two variables can refer to the same object.

```
a = [1, 2]b = ab.append(3)print(a)  # [1, 2, 3]print(b)  # [1, 2, 3]
```

Both names refer to the same list.

Compare that with:

```
a = [1, 2]b = [1, 2]print(a == b)  # Trueprint(a is b)  # False
```

- `==` checks whether values are equal.
- `is` checks whether both references point to the same object.

## 11. What is a constant?

A constant is a name intended to keep the same value throughout a program.

Python does not have a built-in `const` keyword that prevents reassignment.

By convention, constant names use uppercase letters.

```
PI = 3.14159MAX_RETRIES = 3APP_NAME = "MyApp"
```

These are naming conventions, not enforced constants.

```
MAX_RETRIES = 3MAX_RETRIES = 5  # Valid Python, but usually avoid this
```

Python allows reassignment.

## 12. Constants inside modules

Constants are often defined at the top of a module and imported wherever needed.

```
# settings.pyMAX_USERS = 100
```

```
# main.pyimport settingsprint(settings.MAX_USERS)  # 100
```

Using a central constant avoids repeating the same value throughout your program.

## 13. Can we make a constant truly unchangeable?

Python has no universal, built-in constant declaration for ordinary variables. However, you can use certain tools for specific purposes.

Type hint with `Final`:

```
from typing import FinalMAX_USERS: Final[int] = 100
```

`Final` tells type checkers that the name should not be reassigned. Python itself does not enforce this at runtime.

Immutable values:

```
COLORS = ("red", "green", "blue")
```

The tuple's elements cannot be reassigned, but the variable `COLORS` can still be rebound to another object.

## 14. Class variables vs instance variables

### Instance variable

Belongs to an individual object.

```
class Student:    def __init__(self, name):        self.name = names1 = Student("Asha")s2 = Student("Ravi")print(s1.name)  # Ashaprint(s2.name)  # Ravi
```

### Class variable

Shared through the class by default.

```
class Student:    school = "ABC School"    def __init__(self, name):        self.name = nameprint(Student.school)  # ABC School
```

- `self.name` — instance variable.
- `school` — class variable.
- Class variables are not automatically constants; they can be reassigned.

## 15. Other important variable concepts

| Concept              | Example       | Meaning                                  |
| -------------------- | ------------- | ---------------------------------------- |
| `type()`             | `type(x)`     | Returns an object's type                 |
| `id()`               | `id(x)`       | Returns an object's identity             |
| `del`                | `del x`       | Removes a name binding                   |
| `None`               | `x = None`    | Represents no value / absence of a value |
| Unassigned name      | `print(x)`    | Raises `NameError` if `x` isn't defined  |
| Multiple assignment  | `a, b = 1, 2` | Assigns values to multiple names         |
| Augmented assignment | `x += 1`      | Updates a variable using an operation    |
| Naming convention    | `user_name`   | Common style for variable names          |
| Constant convention  | `MAX_SIZE`    | Uppercase name intended as a constant    |

Important: `del x` removes the name `x`; it does not necessarily destroy the object if other references still exist.

## 16. Quick interview revision: 5 tricky examples

Try predicting the output before reading the answer.

Q1. Reassignment

```
x = 10y = xx = 20print(y)
```

Answer: `10`

`y` still refers to the integer value `10`.

Q2. Shared mutable object

```
a = [1, 2]b = aa = [3, 4]print(b)
```

Answer: `[1, 2]`

Reassigning `a` doesn't change what `b` refers to.

Q3. Local variable

```
x = 5def test():    x = 10test()print(x)
```

Answer: `5`

The assignment inside `test()` creates a local variable.

Q4. Constant convention

```
PI = 3.14PI = 4print(PI)
```

Answer: `4`

Uppercase names indicate intended constants but don't prevent reassignment.

Q5. Mutable default trap

```
def add_item(item, items=[]):    items.append(item)    return itemsprint(add_item(1))print(add_item(2))
```

Answer: `[1]`, then `[1, 2]`

The default list is created once and reused across calls. A common safer pattern is `items=None`, then create a new list inside the function.

### Final interview checklist

Make sure you can explain these without hesitation:

- Variable naming and assignment rules
- Dynamic typing and reassignment
- Multiple assignment and swapping
- Local, global, and nonlocal variables
- LEGB scope
- Mutable vs immutable objects
- Object references and `is` vs `==`
- Constants and the `Final` type hint
- Class vs instance variables
- `del`, `None`, `type()`, and `id()`
- Mutable default arguments