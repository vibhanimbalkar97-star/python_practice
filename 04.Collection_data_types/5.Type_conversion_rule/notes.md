## 3. Type conversion rules

Type conversion changes a value from one type to another.

| Code             | Result            | Why?                     |
| ---------------- | ----------------- | ------------------------ |
| `int("10")`      | `10`              | Valid integer text       |
| `float("2.5")`   | `2.5`             | Valid float text         |
| `str(10)`        | `"10"`            | Converts number to text  |
| `int(3.9)`       | `3`               | Truncates decimal part   |
| `bool(0)`        | `False`           | Zero is falsy            |
| `list("cat")`    | `['c', 'a', 't']` | Iterates over characters |
| `set([1, 1, 2])` | `{1, 2}`          | Removes duplicates       |

Important interview rule: Conversion can fail.

```
int("hello")  # ValueError
"10" + 5      # TypeError
```

Why? `"hello"` is not valid integer text, and Python does not automatically add a string to an integer.

Correct approach:

```
int("10") + 5  # 15
```

## 4. Truthy and falsy values

Python can evaluate values as true or false in conditions without requiring an explicit Boolean.

```
if "Python":    print("Runs")
```

Output: `Runs`, because a non-empty string is truthy.

| Falsy values  | Truthy examples   |
| ------------- | ----------------- |
| `False`       | `True`            |
| `None`        | `"False"`         |
| `0`, `0.0`    | `1`, `-1`         |
| `""`          | `" "`             |
| `[]`, `()`    | `[0]`, `(0,)`     |
| `{}`, `set()` | `{"a": 1}`, `{1}` |

Remember: `" "` contains a space, so it is not empty.

```
print(bool([]))     # Falseprint(bool([0]))    # Trueprint(bool("0"))    # Trueprint(bool(0))      # False
```

Why? Empty collections and zero are falsy. Non-empty strings and collections are truthy, even if their contents include zero or the word `"False"`.

## 5. Data type rules for interview output questions

### Rule 1: `+` depends on the types

```
print(2 + 3)       # 5print("2" + "3")   # 23print("2" + 3)     # TypeError
```

Numbers are added; strings are concatenated. Mixed string-integer addition raises an error.

### Rule 2: `*` can repeat strings

```
print("Hi" * 3)  # HiHiHi
```

But `"Hi" * 2.5` raises `TypeError`, because string repetition requires an integer count.

### Rule 3: Strings are immutable

```
text = "cat"# text[0] = "b"  # TypeErrortext = "bat"     # Valid: reassigns the name
```

You cannot modify a string character in place, but you can reassign the variable.

### Rule 4: Lists are mutable

```
a = [1, 2]b = ab.append(3)print(a)  # [1, 2, 3]
```

Both names refer to the same list, so the mutation is visible through both.

### Rule 5: `==` and `is` are different

```
a = [1, 2]b = [1, 2]print(a == b)  # Trueprint(a is b)  # False
```

`==` compares equality; `is` checks object identity.

### Rule 6: `input()` always returns a string

```
age = input("Enter age: ")print(type(age))  # str
```

Even if the user types `25`, the result is `"25"`.

```
age = int(input("Enter age: "))
```

Convert the input when you need to perform numeric operations.

### Rule 7: `type()` identifies a value's type

```
print(type(10))     # intprint(type(10.0))   # floatprint(type(True))   # bool
```

One tricky fact: `bool` is a subclass of `int`.

```
print(isinstance(True, int))  # Trueprint(True + 2)               # 3
```

This works because Python treats `True` numerically as `1` and `False` as `0`. In normal application code, avoid relying on this unless you intentionally need it.

## 6. Quick rules to remember before interviews

| Rule                 | Remember                                                    |
| -------------------- | ----------------------------------------------------------- |
| Dynamic typing       | A variable can refer to different types over time.          |
| `type(x)`            | Returns the type of `x`.                                    |
| `isinstance(x, int)` | Checks whether `x` is an instance of `int` or its subclass. |
| `10 / 2`             | Returns `5.0`, a float.                                     |
| `10 // 3`            | Returns `3`, an integer.                                    |
| `int(4.8)`           | Returns `4`; it doesn't round.                              |
| `None`               | Check with `x is None`.                                     |
| `str`                | Immutable sequence of characters.                           |
| `list`               | Mutable, ordered collection.                                |
| `tuple`              | Ordered collection; elements cannot be reassigned.          |
| `set`                | Unique, hashable elements; no guaranteed order.             |
| `dict`               | Key-value pairs; keys are unique.                           |
| `bool("")`           | `False`.                                                    |
| `bool("False")`      | `True`.                                                     |
| `bool([])`           | `False`.                                                    |
| `bool([0])`          | `True`.                                                     |
| `"5" + 2`            | Raises `TypeError`.                                         |
| `int("5.5")`         | Raises `ValueError`.                                        |

Mini interview quiz
5/5 answered

1. What is the output?
x = 10
x = "20"
print(type(x).__name__)


A. int

B. str

C. float

D. TypeError

Correct — str

Python is dynamically typed, so x can refer to a string after reassignment.


2. What is the output?
print(bool(" "))
print(bool(""))


A. False False

B. True False

C. True True

D. False True

Correct — True False

A space is a character, so " " is non-empty and truthy. An empty string is falsy.


3. What is the output?
a = [1, 2]
b = a
b[0] = 9
print(a)


A. [1, 2]

B. [9, 2]

C. [9, 2, 9]

D. Error

Correct — [9, 2]

Both variables reference the same mutable list.


4. What happens?
x = (5)
print(type(x).__name__)


A. tuple

B. int

C. list

D. Error

Correct — int

Parentheses alone do not create a tuple. The comma does: (5,).


5. What is the output?
print(True + False)
print(type(True).__name__)


A. 1 then bool

B. True then int

C. 1 then int

D. Error

Incorrect — 1 then bool

Booleans behave like 1 and 0 in arithmetic, but the type of True remains bool.

Score: 4/5
Try again