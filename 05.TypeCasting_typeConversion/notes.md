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








# 8. Rules of dict()

Dictionary conversion is slightly different.

### Rule 1: List of key-value pairs to dictionary

```
data = [("name", "Vibha"), ("age", 29)]print(dict(data))
```

Output:

```
{'name': 'Vibha', 'age': 29}
```

Why? Each inner pair contains a key and a value.

### Rule 2: Tuple of pairs to dictionary

```
data = (("a", 10), ("b", 20))print(dict(data))# {'a': 10, 'b': 20}
```

### Rule 3: Dictionary to dictionary

```
data = {"a": 10}print(dict(data))# {'a': 10}
```

### Rule 4: Duplicate keys

```
data = [("a", 10), ("a", 20)]print(dict(data))# {'a': 20}
```

Why? The latest value for the same key overwrites the previous value.

### Rule 5: Incorrect pair length gives ValueError

```
print(dict([("a", 1, 2)]))
```

Output: `ValueError`

Why? Each element must contain exactly two values.

### Rule 6: Integer cannot directly convert into dict

```
print(dict(10))
```

Output: `TypeError`

Why? An integer is not an iterable of key-value pairs.

# 9. Automatic Type Conversion in Arithmetic

Python automatically converts compatible numeric types during arithmetic.

### Rule 1: int + float = float

```
print(10 + 2.5)  # 12.5
```

Why? Integer is promoted to float.

### Rule 2: int + int = int

```
print(10 + 5)  # 15
```

### Rule 3: float + float = float

```
print(2.5 + 1.5)  # 4.0
```

### Rule 4: bool behaves like int in arithmetic

```
print(True + True)    # 2print(True + 5)       # 6print(False + 10)     # 10
```

Why? `True = 1` and `False = 0` in numeric operations.

### Rule 5: int + string causes TypeError

```
print(10 + "20")
```

Output: `TypeError`

Why? Python does not automatically convert strings into numbers during addition.

Correct:

```
print(10 + int("20"))  # 30
```

### Rule 6: String + string performs concatenation

```
print("10" + "20")  # "1020"
```

Why? `+` joins two strings.

### Rule 7: String + int causes TypeError

```
print("10" + 20)
```

Correct:

```
print(int("10") + 20)  # 30print("10" + str(20))  # "1020"
```

### Rule 8: Multiplication with string

```
print("Hi" * 3)  # HiHiHiprint(3 * "Hi")  # HiHiHi
```

Why? String repetition is supported.

But:

```
print("Hi" * 2.5)  # TypeError
```

Why? String repetition requires an integer count.

### Rule 9: Division always returns float

```
print(10 / 2)  # 5.0print(9 / 2)   # 4.5
```

### Rule 10: Floor division

```
print(10 // 3)    # 3print(-10 // 3)   # -4
```

Why? Floor division rounds down towards negative infinity, not towards zero.

Compare:

```
print(int(-10 / 3))  # -3print(-10 // 3)      # -4
```

### Rule 11: Modulus

```
print(10 % 3)   # 1print(-10 % 3)  # 2
```

Why? Python's remainder follows the sign of the divisor.

### Rule 12: Power

```
print(2 ** 3)  # 8print(2 ** -1) # 0.5
```

# 10. Type Casting with input()

Frequently asked

Remember: `input()` always returns a string.

```
age = input("Enter age: ")print(type(age))  # str
```

Even if the user enters `25`, Python stores `"25"`.

Correct:

```
age = int(input("Enter age: "))print(age + 5)
```

If the user enters 25, output = 30.

For decimal input:

```
price = float(input("Enter price: "))
```

Interview question: What happens if the user enters `"hello"`?

```
age = int(input())
```

Output: `ValueError`

Why? `"hello"` is not a valid integer.

# 11. Type Conversion Errors – Must Know

| Error        | When does it happen?        | Example             |
| ------------ | --------------------------- | ------------------- |
| `ValueError` | Value cannot be converted   | `int("abc")`        |
| `TypeError`  | Unsupported type operation  | `10 + "20"`         |
| `ValueError` | Invalid dictionary pair     | `dict([("a",1,2)])` |
| `TypeError`  | Non-iterable passed to list | `list(10)`          |
| `ValueError` | Invalid float string        | `float("hello")`    |

Remember the difference:

- TypeError = Wrong type or unsupported operation.
- ValueError = Correct general type, but invalid value.

# 12. Tricky Interview Cases

These are especially important for output-based questions.

### Case 1: String to Boolean

```
print(bool("False"))print(bool("0"))print(bool(""))
```

Output:

```
TrueTrueFalse
```

Why? Non-empty strings are always truthy.

### Case 2: Boolean to Integer

```
print(True + 10)print(False + 10)
```

Output:

```
1110
```

### Case 3: Float to Integer

```
print(int(9.99))print(int(-9.99))
```

Output:

```
9-9
```

Why? Truncation towards zero.

### Case 4: String multiplication

```
print("5" * 3)print(5 * 3)
```

Output:

```
55515
```

Why? First performs string repetition; second performs arithmetic.

### Case 5: List to Boolean

```
print(bool([0]))print(bool([]))print(bool([None]))
```

Output:

```
TrueFalseTrue
```

Why? Python checks whether the collection is empty, not whether its elements are truthy.

### Case 6: None to string

```
a = Noneprint(str(a))print(type(str(a)))print(bool(str(a)))
```

Output:

```
None<class 'str'>True
```

Why? `str(None)` returns a non-empty string `"None"`.

### Case 7: Float and Boolean

```
print(10 + True)print(10.5 + False)
```

Output:

```
1110.5
```

### Case 8: String and list

```
print(list("123"))print(str([1, 2, 3]))
```

Output:

```
['1', '2', '3'][1, 2, 3]
```

Why? `list()` creates a list of individual characters, whereas `str()` creates one string representing the list.

### Case 9: Duplicate elements

```
a = [1, 2, 2, 3]b = set(a)print(b)print(len(b))
```

Output:

```
{1, 2, 3}3
```

Why? Set removes duplicates.

### Case 10: Addition and concatenation

```
print(10 + 20)print("10" + "20")print("10" + str(20))print(int("10") + int("20"))
```

Output:

```
301020102030
```

# 13. Advanced Rules Worth Knowing

These cases help with slightly harder interview questions.

Rule 1: int() does not accept complex numbers.

```
print(int(10 + 2j))
```

Output: `TypeError`

Rule 2: float() does not accept complex numbers.

```
print(float(10 + 2j))
```

Output: `TypeError`

Rule 3: bool is a subclass of int.

```
print(isinstance(True, int))  # Trueprint(type(True) == int)      # False
```

Why? `isinstance()` checks inheritance, while `type()` checks the exact type.

Rule 4: Numeric strings can contain underscores in valid positions.

```
print(int("1_000"))    # 1000print(float("1_000.5")) # 1000.5
```

Rule 5: int() can accept an integer in binary notation with a base.

```
print(int("0b1010", 0))  # 10
```

Rule 6: Converting float to int loses precision.

```
a = 10.99b = int(a)print(b)  # 10
```

Rule 7: Float may lose precision during conversion.

```
print(float("0.1") + float("0.2"))# 0.30000000000000004
```

Why? Floating-point numbers use binary representation, so some decimal values cannot be represented exactly.

Rule 8: int() accepts only strings representing integers, not decimal notation.

```
print(int("10.0"))  # ValueErrorprint(int("10"))    # 10
```

Rule 9: list(), tuple(), and set() require iterables.

```
list(10)   # TypeErrortuple(10)  # TypeErrorset(10)    # TypeError
```

Rule 10: Converting a set into a list does not guarantee a particular order.

```
a = {3, 1, 2}print(list(a))
```

Do not assume the output will always be `[3, 1, 2]`.

# 14. Final Interview Revision Checklist

Use this as your quick revision sheet before interviews.

| Rule              | Remember                |
| ----------------- | ----------------------- |
| `input()`         | Always returns string   |
| `int(10.9)`       | Returns 10, not 11      |
| `int(-10.9)`      | Returns -10             |
| `int("10.5")`     | ValueError              |
| `float("10")`     | Returns 10.0            |
| `str(False)`      | Returns `"False"`       |
| `bool("False")`   | Returns True            |
| `bool("0")`       | Returns True            |
| `bool("")`        | Returns False           |
| `bool(" ")`       | Returns True            |
| `bool([])`        | Returns False           |
| `bool([0])`       | Returns True            |
| `bool(None)`      | Returns False           |
| `True + 1`        | Returns 2               |
| `10 / 2`          | Returns 5.0             |
| `10 // 3`         | Returns 3               |
| `-10 // 3`        | Returns -4              |
| `"Hi" * 3`        | Returns `"HiHiHi"`      |
| `10 + "20"`       | TypeError               |
| `list("abc")`     | Returns `['a','b','c']` |
| `set([1,1,2])`    | Removes duplicates      |
| `dict([("a",1)])` | Creates dictionary      |

# 15. Practice – Interview Questions

Now test whether you can apply the rules without looking at the answers.

Try these 15 questions from easy to tricky.

Python Type Casting Quiz

0/15 answered

Q1. What is the output?

print(int(12.99))

12

13

12.99

ValueError

Q2. What is the output?

print(bool("False"))

False

True

ValueError

None

Q3. What is the output?

print(True + False + 5)

5

6

1

TypeError

Q4. What happens?

print(int("10.5"))

10

10.5

ValueError

TypeError

Q5. What is the output?

print(bool([0, False, None]))

False

True

None

TypeError

Q6. What is the output?

print("5" \* 2 + str(10))

510

5510

1010

TypeError

Q7. What is the output?

print(int(-8.9))

-9

-8

8

ValueError

Q8. What is the output?

print(type(float(True)))

int

bool

float

str

Q9. What is the output?

print(list({"a": 1, "b": 2}))

[1, 2]

['a', 'b']

[('a',1),('b',2)]

TypeError

Q10. What is the output?

print(-10 // 3)

-3

-4

3

4

Q11. What is the output?

print(bool(float('nan')))

False

True

ValueError

None

Q12. What is the output?

print(int(True) + float(False))

1

1.0

0.0

TypeError

Q13. What happens?

print(list(123))

[1, 2, 3]

['1','2','3']

TypeError

ValueError

Q14. What is the output?

print(dict([("a", 1), ("a", 5)]))

{"a": 1}

{"a": 5}

ValueError

TypeError

Q15. What is the output?

print(int(float("12.9")) + bool(""))

13

12

12.9

TypeError

Submit answers

Answer all 15 questions to see your score and explanations.

My suggestion: First understand Sections 3–7 and 9–12. These are especially important for Python output-based interview questions. Then solve the quiz without referring to the notes.