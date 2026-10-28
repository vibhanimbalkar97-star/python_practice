# Python Variables & Constants: Interview Rules Cheat Sheet

Learn these rules with the examples and the reason behind each behavior. If you understand why Python behaves this way, you can solve many output-based and tricky interview questions.

## 1. Variable naming rules

| Rule                                         | Example         | Why?                                   |
| -------------------------------------------- | --------------- | -------------------------------------- |
| Names are case-sensitive                     | `age` and `Age` | Python treats them as different names. |
| Cannot start with a number                   | `2age = 10` ❌   | A name cannot begin with a digit.      |
| Can start with `_`                           | `_age = 10`     | Underscores are allowed.               |
| Cannot contain spaces                        | `first name` ❌  | Use `first_name` instead.              |
| Cannot use keywords                          | `class = 10` ❌  | `class` is reserved by Python.         |
| Can contain digits after the first character | `age2 = 20`     | Digits are allowed after the start.    |

```
age = 20Age = 30print(age, Age)  # 20 30
```

Remember: Python names are case-sensitive and must follow identifier rules.

## 2. Assignment and reassignment rules

### Rule 1: `=` assigns a value; it does not compare values.

```
x = 10x = 20print(x)  # 20
```

Why? The second assignment makes `x` refer to `20` instead of `10`.

### Rule 2: A variable must be assigned before it is accessed.

```
print(x)  # NameError if x has not been defined
```

Why? Python cannot resolve the name `x` in the current scope.

### Rule 3: Python is dynamically typed.

```
x = 10x = "Hello"print(x)  # Hello
```

Why? A name can refer to objects of different types at different times.

### Rule 4: Multiple assignment assigns values in one statement.

```
a, b = 10, 20print(a, b)  # 10 20
```

Why? Python unpacks the right-hand values into the corresponding names.

### Rule 5: Chained assignment gives multiple names the same initial object.

```
a = b = [1, 2]a.append(3)print(b)  # [1, 2, 3]
```

Why? Both names refer to the same list. Mutating that list is visible through either name.

### Rule 6: Swapping works without a temporary variable.

```
a, b = 10, 20a, b = b, aprint(a, b)  # 20 10
```

Why? Python evaluates the right-hand side before assigning the new values.

## 3. Scope rules: Local, Global, Nonlocal

### Rule 7: A variable created inside a function is local by default when assigned there.

```
x = 10def test():    x = 20test()print(x)  # 10
```

Why? The assignment creates a local `x`; it doesn't change the global `x`.

### Rule 8: Read a global variable inside a function without `global`.

```
x = 10def test():    print(x)test()  # 10
```

Why? Python searches enclosing scopes when resolving a name that isn't local.

### Rule 9: Use `global` to reassign a module-level variable.

```
x = 10def test():    global x    x = 20test()print(x)  # 20
```

Why? `global x` tells Python that assignments to `x` refer to the module-level name.

### Rule 10: Use `nonlocal` to reassign an enclosing function's variable.

```
def outer():    x = 10    def inner():        nonlocal x        x = 20    inner()    print(x)  # 20outer()
```

Why? `nonlocal` targets the nearest enclosing function scope containing that name.

### Rule 11: Python follows LEGB when looking up a name.

- L — Local
- E — Enclosing function
- G — Global/module
- B — Built-in

```
x = "Global"def test():    x = "Local"    print(x)test()  # Local
```

Why? Python uses the nearest matching binding, which here is the local `x`.

## 4. Mutable and immutable object rules

### Rule 12: Immutable objects cannot be changed in place.

```
x = 10x = x + 1print(x)  # 11
```

Why? Integers are immutable. Python calculates a new value and rebinds `x`.

Examples: `int`, `float`, `bool`, `str`, and `tuple` (with a caveat for mutable contents).

### Rule 13: Mutable objects can be modified in place.

```
items = [1, 2]items.append(3)print(items)  # [1, 2, 3]
```

Why? Lists are mutable; `append()` modifies the existing list.

Examples: `list`, `dict`, and `set`.

### Rule 14: Assignment does not automatically copy an object.

```
a = [1, 2]b = ab.append(3)print(a)  # [1, 2, 3]
```

Why? `a` and `b` refer to the same list.

### Rule 15: Reassigning one name does not reassign another name.

```
a = [1, 2]b = aa = [3, 4]print(b)  # [1, 2]
```

Why? `a` now refers to a new list, but `b` still refers to the original list.

### Rule 16: `==` compares values; `is` compares identity.

```
a = [1, 2]b = [1, 2]print(a == b)  # Trueprint(a is b)  # False
```

Why? The contents are equal, but the lists are different objects.

Interview rule: Use `==` for value comparisons. Use `is` when checking object identity, commonly `x is None`.

## 5. Constants rules

### Rule 17: Uppercase names indicate constants by convention.

```
MAX_USERS = 100MAX_USERS = 200  # Still valid Python
```

Why? Python doesn't enforce constant variables. Uppercase is a signal to developers not to change them.

### Rule 18: `Final` is a type-checking instruction, not runtime enforcement.

```
from typing import FinalMAX_USERS: Final[int] = 100
```

Why? Type checkers can flag reassignment, but Python itself still permits it at runtime.

### Rule 19: An immutable value doesn't make its variable name constant.

```
x = "Hello"x = "World"print(x)  # World
```

Why? Strings cannot be modified in place, but the name `x` can refer to another string.

## 6. Class and instance variable rules

### Rule 20: Instance variables belong to individual objects.

```
class Student:    def __init__(self, name):        self.name = namea = Student("Asha")b = Student("Ravi")print(a.name, b.name)  # Asha Ravi
```

Why? Each instance has its own `name` attribute.

### Rule 21: Class variables are shared through the class by default.

```
class Student:    school = "ABC"a = Student()b = Student()print(a.school, b.school)  # ABC ABC
```

Why? Both instances find `school` on the class.

### Rule 22: Assigning through an instance can create an instance attribute.

```
class Student:    school = "ABC"a = Student()a.school = "XYZ"print(a.school)       # XYZprint(Student.school) # ABC
```

Why? The assignment creates `a.school`, which shadows the class attribute for that instance.

## 7. Special variable rules

### Rule 23: `None` means absence of a value; it is not the same as `0` or `""`.

```
x = Noneprint(x is None)  # True
```

Why? `None` is a special singleton object. Use `is None` to test for it.

### Rule 24: `del` removes a name binding.

```
x = [1, 2]y = xdel xprint(y)  # [1, 2]
```

Why? Only the name `x` is removed; `y` still refers to the list.

### Rule 25: `type()` tells you an object's type.

```
x = 10print(type(x))  # <class 'int'>
```

Why? The object referred to by `x` is an integer.

### Rule 26: `id()` gives an object's identity during its lifetime.

```
x = [1, 2]y = xprint(id(x) == id(y))  # True
```

Why? Both names refer to the same object.

Don't rely on specific numeric `id()` values or assume different objects can never reuse an identity after an object's lifetime ends.

## 8. Tricky interview rules

### Rule 27: Mutable default arguments are created once when the function is defined.

```
def add_item(item, items=[]):    items.append(item)    return itemsprint(add_item(1))  # [1]print(add_item(2))  # [1, 2]
```

Why? The same default list is reused between calls.

Safer approach:

```
def add_item(item, items=None):    if items is None:        items = []    items.append(item)    return items
```

Now each call without `items` gets a new list.

### Rule 28: Augmented assignment can mutate a mutable object.

```
a = [1, 2]b = aa += [3]print(b)  # [1, 2, 3]
```

Why? For lists, `+=` extends the existing list in place.

Compare:

```
a = [1, 2]b = aa = a + [3]print(b)  # [1, 2]
```

Here, `+` creates a new list, and `a` is rebound to it.

### Rule 29: Assignment inside a function determines local scope unless declared otherwise.

```
x = 10def test():    # print(x)  # UnboundLocalError if this line is enabled    x = x + 1test()
```

Why? Because Python sees the assignment to `x` in the function, it treats `x` as local throughout that function. The local value is read before it has been assigned.

### Rule 30: A tuple can contain a mutable object.

```
data = ([1, 2], 3)data[0].append(4)print(data)  # ([1, 2, 4], 3)
```

Why? The tuple's references cannot be reassigned, but the list it refers to is mutable.

## Quick method to solve any output question

When you see a variable question in an interview, check these in order:

1. Name: Which variable is being accessed?
2. Scope: Is it local, enclosing, global, or built-in?
3. Binding: What object does the name currently refer to?
4. Mutation: Is the object changed in place, or is the name reassigned?
5. Identity: Are two names referring to the same object?
6. Evaluation: Does the order of assignment or augmented assignment matter?
7. Special case: Is there a constant convention, `None`, a class attribute, or a mutable default?

If you can apply these seven checks, you can reason through most Python variables-and-constants interview questions rather than memorizing outputs.