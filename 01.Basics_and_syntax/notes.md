# Python Basics & Syntax — Interview Revision Notes

These notes cover the important Python rules, syntax, and tricky concepts you should revise before interviews, from beginner to advanced questions.

## 1. Important rules and short notes

### A. Python syntax rules

| Rule                | Short note                                                                                |
| ------------------- | ----------------------------------------------------------------------------------------- |
| Case-sensitive      | `name` and `Name` are different variables.                                                |
| Indentation         | Python uses indentation to define code blocks, usually 4 spaces.                          |
| Colon `:`           | Used after `if`, `else`, `for`, `while`, `def`, and `class`.                              |
| Comments            | Use `#` for single-line comments.                                                         |
| Multiple statements | Usually write one statement per line.                                                     |
| Semicolon `;`       | Optional for separating statements, but generally avoid it.                               |
| Line continuation   | Use parentheses `()`, brackets `[]`, or braces `{}` for multiline expressions.            |
| Quotes              | Strings can use single `' '`, double `" "`, or triple quotes `''' '''`.                   |
| Naming              | Variable names can contain letters, numbers, and `_`, but cannot start with a number.     |
| Keywords            | Reserved words such as `if`, `for`, `class`, and `True` cannot be used as variable names. |

### B. Variables and assignment

```
x = 10name = "Python"a, b = 5, 10x, y = y, x  # Swap values
```

- Python is dynamically typed: you don't declare a variable's type explicitly.
- `=` means assignment; `==` means equality comparison.
- A variable must be assigned before you access it.
- Variables can be reassigned to values of different types.
- Python does not require a separate declaration for constants; uppercase names are a convention.

```
x = 10x = "Hello"
```

This is valid Python.

### C. Basic data types

| Type       | Example           |
| ---------- | ----------------- |
| Integer    | `10`, `-5`        |
| Float      | `3.14`, `2.0`     |
| String     | `"Hello"`         |
| Boolean    | `True`, `False`   |
| None       | `None`            |
| List       | `[1, 2, 3]`       |
| Tuple      | `(1, 2, 3)`       |
| Set        | `{1, 2, 3}`       |
| Dictionary | `{"name": "Sam"}` |

Important rules:

- `type(value)` returns the type of a value.
- `None` represents the absence of a value.
- `True` and `False` are Boolean values; their capitalization matters.
- `bool(0)` is `False`, while `bool(1)` is `True`.
- Empty strings and empty collections are falsy.
- Non-empty strings, including `"0"` and `"False"`, are truthy.

### D. Type conversion

```
int("10")       # 10float("3.5")    # 3.5str(100)        # "100"bool(0)         # Falseint(3.9)        # 3
```

- `int(3.9)` truncates the decimal part; it does not round.
- `int("3.9")` raises `ValueError`.
- `int("10")` works because the string represents an integer.
- Adding a string and an integer directly, such as `"10" + 2`, raises `TypeError`.

### E. Operators and precedence

| Operator             | Purpose                 |
| -------------------- | ----------------------- |
| `+`, `-`, `*`, `/`   | Arithmetic              |
| `//`                 | Floor division          |
| `%`                  | Modulus (remainder)     |
| `**`                 | Exponentiation          |
| `==`, `!=`           | Equality and inequality |
| `>`, `<`, `>=`, `<=` | Comparisons             |
| `and`, `or`, `not`   | Logical operators       |
| `in`, `not in`       | Membership              |
| `is`, `is not`       | Object identity         |
| `+=`, `-=`, `*=`     | Augmented assignment    |

Remember:

```
print(10 / 2)    # 5.0print(10 // 3)   # 3print(2 ** 3)    # 8print(10 % 3)    # 1
```

- `and` and `or` short-circuit and can return operands, not necessarily Boolean values.
- `is` checks whether two references point to the same object; `==` checks equality.
- Use parentheses to make complicated expressions clearer.

### F. Input and output

```
name = input("Enter name: ")age = int(input("Enter age: "))print(name, age)print("Age:", age)print(f"My age is {age}")
```

- `input()` returns a string, even when the user enters a number.
- Convert input explicitly when you need numeric values.
- `print()` separates multiple arguments with a space by default.
- F-strings use `f"..."` and `{}` to insert expressions.

### G. Conditional statements

```
if age >= 18:    print("Adult")elif age >= 13:    print("Teenager")else:    print("Child")
```

- Use a colon after each condition.
- Indentation determines which statements belong to each branch.
- Python uses `elif`, not `else if`.
- Conditions can use truthy and falsy values.
- Only the first matching branch executes.

### H. Loops

```
for i in range(3):    print(i)  # 0, 1, 2i = 0while i < 3:    print(i)    i += 1
```

- `range(start, stop, step)` excludes the `stop` value.
- `break` exits the nearest loop.
- `continue` skips to the next iteration.
- `pass` is a placeholder that does nothing.
- A `while` loop can become infinite if its condition never becomes false.

### I. Common syntax mistakes

- Using `=` instead of `==` in a comparison.
- Forgetting a colon after `if`, `for`, or `while`.
- Incorrect indentation.
- Trying to add incompatible types, such as `"5" + 2`.
- Using `True`, `False`, or `None` with incorrect capitalization.
- Accessing a variable before assigning it.
- Forgetting that `input()` returns a string.
- Expecting `range(1, 5)` to include `5`.