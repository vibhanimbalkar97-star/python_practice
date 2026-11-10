# Python Strings & String Methods – Complete Beginner Notes

Python strings are one of the most important topics for coding interviews. You use them for storing text, accessing characters, searching, replacing, splitting, joining, and solving coding problems.

I'll cover the basics, rules, every important method, common mistakes, and tricks to solve string questions.

## 1. What is a string?

A string (`str`) is a sequence of characters enclosed in quotes.

```
name = "Python"city = 'Pune'message = """Welcome to Python"""
```

All three are valid strings.

Rules:

- Use single quotes `' '`, double quotes `" "`, or triple quotes `""" """`.
- A string can contain letters, numbers, symbols, and spaces.
- Even numbers inside quotes are strings.

```
a = "100"b = 100print(type(a))  # <class 'str'>print(type(b))  # <class 'int'>
```

Remember: `"100"` is text; `100` is an integer.

## 2. Creating strings

```
s1 = "Hello"s2 = 'Hello's3 = """HelloPythonWorld"""print(s3)
```

Output:

```
Hello
Python
World
```

Triple quotes allow multiline strings.

### Quotes inside strings

```
print("It's Python")print('He said "Hello"')print("It\'s Python")
```

Use different outer and inner quotes, or escape a quote with `\`.

## 3. String indexing

Indexing means accessing one character using its position.

```
text = "Python"
```

Positive indexing (left to right)

P

0

y

1

t

2

h

3

o

4

n

5

Negative indexing (right to left)

P

-6

y

-5

t

-4

h

-3

o

-2

n

-1

```
text = "Python"print(text[0])   # Pprint(text[1])   # yprint(text[-1])  # nprint(text[-2])  # o
```

Important rules:

- Positive indexing starts at `0`.
- Negative indexing starts at `-1`.
- Accessing an invalid index gives `IndexError`.

```
print(text[10])  # IndexError
```

## 4. String slicing

Slicing means extracting a part of a string.

Syntax:

```
string[start:stop:step]
```

- `start`: where to begin (included).
- `stop`: where to stop (excluded).
- `step`: how many positions to move each time.

```
s = "Python"print(s[0:3])   # Pytprint(s[2:5])   # thoprint(s[:3])    # Pytprint(s[2:])    # thonprint(s[:])     # Python
```

### Slicing with step

```
s = "Python"print(s[::1])   # Pythonprint(s[::2])   # Ptoprint(s[::-1])  # nohtyPprint(s[1::2])  # yhn
```



Interview trick

`[::-1]` is a quick way to reverse a string.



### Negative slicing

```
s = "Python"print(s[-4:-1])  # thoprint(s[-3:])    # honprint(s[:-2])    # Pyth
```

Common mistake: The stop index is always excluded.

```
print("Python"[1:4])  # yth
```

Index `4` is not included.

## 5. Strings are immutable

Immutable means you cannot change an existing string character directly.

```
s = "Python"s[0] = "J"  # TypeError
```

Instead, create a new string:

```
s = "Python"s = "J" + s[1:]print(s)  # Jython
```

Another important example:

```
s = "hello"s.upper()print(s)  # hello
```

Why? `upper()` returns a new string. It does not modify the original.

Correct:

```
s = s.upper()print(s)  # HELLO
```

Interview rule: String methods generally return a new string; they do not modify the original string.

## 6. String length – `len()`

`len()` returns the total number of characters, including spaces and symbols.

```
s = "Hello"print(len(s))  # 5
```

```
s = "Hello World"print(len(s))  # 11
```

Trick: A space is also a character.

```
print(len(""))   # 0print(len(" "))  # 1
```

## 7. Changing uppercase and lowercase

| Method         | Meaning                                   | Example                 | Output        |
| -------------- | ----------------------------------------- | ----------------------- | ------------- |
| `upper()`      | All uppercase                             | `"hello".upper()`       | `HELLO`       |
| `lower()`      | All lowercase                             | `"HELLO".lower()`       | `hello`       |
| `capitalize()` | First character uppercase, rest lowercase | `"pYTHON".capitalize()` | `Python`      |
| `title()`      | First character of each word uppercase    | `"hello world".title()` | `Hello World` |
| `swapcase()`   | Reverses letter cases                     | `"PyThOn".swapcase()`   | `pYtHoN`      |
| `casefold()`   | Stronger lowercase for comparisons        | `"HELLO".casefold()`    | `hello`       |

Examples:

```
s = "python programming"print(s.upper())       # PYTHON PROGRAMMINGprint(s.capitalize())  # Python programmingprint(s.title())       # Python Programming
```

Trick: For case-insensitive comparisons:

```
a = "Python"b = "PYTHON"print(a.lower() == b.lower())  # True
```

`casefold()` is useful for more comprehensive Unicode case-insensitive comparisons.

## 8. Removing spaces and characters

These methods remove characters from the beginning/end, not from the middle.

| Method     | Meaning               | Example             | Output   |
| ---------- | --------------------- | ------------------- | -------- |
| `strip()`  | Remove from both ends | `"  hi  ".strip()`  | `"hi"`   |
| `lstrip()` | Remove from left      | `"  hi  ".lstrip()` | `"hi  "` |
| `rstrip()` | Remove from right     | `"  hi  ".rstrip()` | `"  hi"` |

```
s = "  Python  "print(s.strip())   # "Python"print(s.lstrip())  # "Python  "print(s.rstrip())  # "  Python"
```

You can also specify characters:

```
s = "***hello***"print(s.strip("*"))  # hello
```

Important trick: `strip("abc")` removes any matching characters from the ends, not the exact substring `"abc"`.

```
print("cabhelloabc".strip("abc"))  # hello
```

## 9. Searching inside strings

| Method     | Meaning                  | Example                | Output |
| ---------- | ------------------------ | ---------------------- | ------ |
| `find()`   | First position, or -1    | `"banana".find("a")`   | `1`    |
| `rfind()`  | Last position, or -1     | `"banana".rfind("a")`  | `5`    |
| `index()`  | First position, or error | `"banana".index("n")`  | `2`    |
| `rindex()` | Last position, or error  | `"banana".rindex("n")` | `4`    |
| `count()`  | Number of occurrences    | `"banana".count("a")`  | `3`    |

```
s = "banana"print(s.find("a"))    # 1print(s.rfind("a"))   # 5print(s.find("z"))    # -1print(s.count("a"))   # 3
```

### `find()` vs `index()`

```
s = "Python"print(s.find("z"))   # -1print(s.index("z"))  # ValueError
```

Interview trick: Use `find()` when the character may not exist and you want `-1` instead of an error.

## 10. Checking string contents – Boolean methods

These methods return `True` or `False`.

| Method         | Checks                      | Example                     | Output |
| -------------- | --------------------------- | --------------------------- | ------ |
| `isalpha()`    | Only letters                | `"Python".isalpha()`        | True   |
| `isdigit()`    | Only digit characters       | `"123".isdigit()`           | True   |
| `isdecimal()`  | Decimal digits              | `"123".isdecimal()`         | True   |
| `isnumeric()`  | Numeric characters          | `"½".isnumeric()`           | True   |
| `isalnum()`    | Letters or numbers          | `"Python123".isalnum()`     | True   |
| `isspace()`    | Only whitespace             | `"   ".isspace()`           | True   |
| `islower()`    | All cased letters lowercase | `"hello".islower()`         | True   |
| `isupper()`    | All cased letters uppercase | `"HELLO".isupper()`         | True   |
| `istitle()`    | Title-case format           | `"Hello World".istitle()`   | True   |
| `startswith()` | Starts with given text      | `"Python".startswith("Py")` | True   |
| `endswith()`   | Ends with given text        | `"Python".endswith("on")`   | True   |

### Important differences

`isalpha()` vs `isalnum()`

```
print("Python".isalpha())     # Trueprint("Python123".isalpha())  # Falseprint("Python123".isalnum())  # Trueprint("Python 123".isalnum()) # False
```

Space and special characters make `isalnum()` false.

`isdigit()` vs `isdecimal()` vs `isnumeric()`

```
print("123".isdecimal())  # Trueprint("123".isdigit())    # Trueprint("123".isnumeric())  # Trueprint("²".isdecimal())    # Falseprint("²".isdigit())      # Trueprint("²".isnumeric())    # Trueprint("½".isdecimal())    # Falseprint("½".isdigit())      # Falseprint("½".isnumeric())    # True
```

Remember the general relationship: `isdecimal()` is the narrowest, `isdigit()` includes more digit characters, and `isnumeric()` includes the widest range of numeric characters.

Important: Empty strings return `False` for these checking methods.

```
print("".isalpha())  # Falseprint("".isdigit())  # Falseprint("".isspace())  # False
```

## 11. Replacing characters or words – `replace()`

Syntax:

```
string.replace(old, new, count)
```

- `old`: text to replace.
- `new`: replacement text.
- `count`: optional maximum number of replacements.

```
s = "banana"print(s.replace("a", "o"))     # bononoprint(s.replace("a", "o", 1))  # bonanaprint(s.replace("a", ""))      # bnn
```

Replace words:

```
s = "I love Java"print(s.replace("Java", "Python"))# I love Python
```

Trick: `replace()` does not modify the original string.

```
s = "hello"s.replace("h", "H")print(s)  # hello
```

## 12. Splitting strings – `split()`

`split()` divides a string into a list.

Syntax:

```
string.split(separator, maxsplit)
```

```
s = "I love Python"print(s.split())# ['I', 'love', 'Python']
```

Split using a comma:

```
s = "apple,banana,mango"print(s.split(","))# ['apple', 'banana', 'mango']
```

Limit the number of splits:

```
s = "one-two-three-four"print(s.split("-", 1))# ['one', 'two-three-four']
```

Important difference:

```
s = "a  b   c"print(s.split())# ['a', 'b', 'c']print(s.split(" "))# ['a', '', 'b', '', '', 'c']
```

- `split()` without an argument treats consecutive whitespace as one separator and ignores leading/trailing whitespace.
- `split(" ")` splits on each individual space, so empty strings can appear.

## 13. Joining strings – `join()`

`join()` combines list elements into one string.

Syntax:

```
separator.join(iterable)
```

```
words = ["I", "love", "Python"]print(" ".join(words))# I love Pythonprint("-".join(words))# I-love-Pythonprint("".join(words))# IlovePython
```

Important: `join()` is called on the separator string, not on the list.

Incorrect:

```
words.join(" ")  # AttributeError
```

Correct:

```
" ".join(words)
```

If list elements are not strings, convert them first:

```
numbers = [1, 2, 3]result = "-".join(map(str, numbers))print(result)  # 1-2-3
```

## 14. Checking the beginning and ending

```
s = "Python Programming"print(s.startswith("Python"))  # Trueprint(s.startswith("Java"))    # Falseprint(s.endswith("Programming"))  # Trueprint(s.endswith("Python"))       # False
```

You can pass a tuple of possible prefixes or suffixes:

```
filename = "photo.png"print(filename.endswith((".png", ".jpg", ".jpeg")))# True
```

Useful for file extensions and input validation.

## 15. String formatting

Formatting means inserting variable values into strings.

### Method 1: f-strings (recommended)

```
name = "Vibha"age = 30print(f"My name is {name} and my age is {age}")
```

Output:

```
My name is Vibha and my age is 30
```

You can put expressions inside `{}`:

```
a = 10b = 20print(f"Total = {a + b}")  # Total = 30
```

### Method 2: `format()`

```
name = "Python"print("I love {}".format(name))# I love Python
```

### Method 3: `%` formatting

```
name = "Python"print("I love %s" % name)
```

Interview tip: Prefer f-strings in modern Python code because they are readable and convenient.

## 16. Padding and alignment

| Method     | Meaning           | Example               | Output   |
| ---------- | ----------------- | --------------------- | -------- |
| `center()` | Center text       | `"hi".center(6, "*")` | `**hi**` |
| `ljust()`  | Left-align text   | `"hi".ljust(5, "-")`  | `hi---`  |
| `rjust()`  | Right-align text  | `"hi".rjust(5, "-")`  | `---hi`  |
| `zfill()`  | Add zeros on left | `"42".zfill(5)`       | `00042`  |

```
print("Python".center(10, "*"))# **Python**print("Python".ljust(10, "-"))# Python----print("42".zfill(5))# 00042
```

The width is the minimum total width. If the original string is already longer, it is not shortened.

## 17. Other useful string methods

| Method           | Purpose                           | Example                           | Output              |
| ---------------- | --------------------------------- | --------------------------------- | ------------------- |
| `partition()`    | Split into 3 parts at first match | `"a-b-c".partition("-")`          | `('a', '-', 'b-c')` |
| `rpartition()`   | Split at last match               | `"a-b-c".rpartition("-")`         | `('a-b', '-', 'c')` |
| `removeprefix()` | Remove prefix if present          | `"unhappy".removeprefix("un")`    | `happy`             |
| `removesuffix()` | Remove suffix if present          | `"file.txt".removesuffix(".txt")` | `file`              |
| `expandtabs()`   | Replace tabs with spaces          | `"a\tb".expandtabs(4)`            | `a   b`             |
| `encode()`       | Convert string to bytes           | `"hi".encode()`                   | `b'hi'`             |

Examples:

```
s = "www.example.com"print(s.partition(".")) # ('www', '.', 'example.com')print("test.py".removesuffix(".py"))# test
```

Trick: `partition()` always returns a tuple of three parts, even if the separator is missing.

```
print("hello".partition("-"))# ('hello', '', '')
```

## 18. String operators

| Operator | Purpose            | Example                  | Output   |
| -------- | ------------------ | ------------------------ | -------- |
| `+`      | Concatenation      | `"Py" + "thon"`          | `Python` |
| `*`      | Repetition         | `"Hi" * 3`               | `HiHiHi` |
| `in`     | Check substring    | `"Py" in "Python"`       | True     |
| `not in` | Check absence      | `"Java" not in "Python"` | True     |
| `==`     | Compare equality   | `"hi" == "HI"`           | False    |
| `!=`     | Compare inequality | `"hi" != "HI"`           | True     |

```
a = "Hello"b = "World"print(a + " " + b)  # Hello Worldprint("Hi" * 3)     # HiHiHiprint("ell" in a)   # True
```

### String comparison is case-sensitive

```
print("python" == "Python")  # Falseprint("a" < "b")             # Trueprint("A" < "a")             # True
```

Python compares strings lexicographically using Unicode code points. It does not automatically ignore uppercase/lowercase differences.

## 19. Escape characters

Escape characters are special sequences that represent characters inside a string.

| Escape | Meaning      | Example            |
| ------ | ------------ | ------------------ |
| `\n`   | New line     | `"Hello\nWorld"`   |
| `\t`   | Tab          | `"Hello\tWorld"`   |
| `\\`   | Backslash    | `"C:\\Users"`      |
| `\'`   | Single quote | `'It\'s Python'`   |
| `\"`   | Double quote | `"He said \"Hi\""` |

```
print("Hello\nWorld")
```

Output:

```
Hello
World
```

### Raw strings

A raw string treats backslashes mostly as literal characters.

```
path = r"C:\new\test"print(path)# C:\new\test
```

Useful for Windows paths and regular expressions. A raw string cannot end with a single unescaped backslash.

## 20. Character frequency and common string logic

These are common building blocks for coding questions.

### Count a particular character

```
s = "banana"print(s.count("a"))  # 3
```

### Count vowels

```
s = "Python Programming"count = 0for ch in s.lower():    if ch in "aeiou":        count += 1print(count)
```

### Reverse a string

```
s = "Python"print(s[::-1])  # nohtyP
```

### Check palindrome

A palindrome reads the same forward and backward.

```
s = "madam"if s == s[::-1]:    print("Palindrome")else:    print("Not palindrome")
```

### Count each character

```
s = "banana"for ch in set(s):    print(ch, s.count(ch))
```

This prints each distinct character and its count, but the order of characters from a set is not guaranteed.

For a frequency dictionary, use:

```
s = "banana"freq = {}for ch in s:    freq[ch] = freq.get(ch, 0) + 1print(freq)# {'b': 1, 'a': 3, 'n': 2}
```

Trick: `dict.get(key, default)` returns the existing value or the default if the key is not present.

## 21. Important rules and tricky cases

These are common interview output questions.

Rule 1: Strings are case-sensitive.

```
print("Python" == "python")  # False
```

Rule 2: `in` checks for a substring, not just a single character.

```
print("thon" in "Python")  # Trueprint("xyz" in "Python")  # False
```

Rule 3: `count()` does not count overlapping matches.

```
print("aaaa".count("aa"))  # 2
```

It counts two non-overlapping occurrences.

Rule 4: `replace()` replaces all occurrences by default.

```
print("aaaa".replace("a", "b"))  # bbbb
```

Rule 5: `split()` returns a list, not a string.

```
result = "a,b,c".split(",")print(type(result))  # <class 'list'>
```

Rule 6: `join()` returns a string.

```
result = "-".join(["a", "b", "c"])print(type(result))  # <class 'str'>
```

Rule 7: Strings can be looped through character by character.

```
for ch in "cat":    print(ch)
```

Output:

```
c
a
t
```

Rule 8: An empty string is falsy.

```
print(bool(""))     # Falseprint(bool(" "))    # Trueprint(bool("abc"))  # True
```

Rule 9: String concatenation with an integer requires conversion.

```
age = 25# print("Age: " + age)  # TypeErrorprint("Age: " + str(age))  # Age: 25
```

Rule 10: A string is iterable but immutable.

You can read its characters in a loop, but cannot assign to an individual position.

```
s = "cat"for ch in s:    print(ch)# s[0] = "b"  # TypeError
```

## 22. Tricks to solve string coding questions

| If question says...         | Think about...                     | Example                          |
| --------------------------- | ---------------------------------- | -------------------------------- |
| Reverse a string            | Slicing                            | `s[::-1]`                        |
| Check palindrome            | Compare with reverse               | `s == s[::-1]`                   |
| Count characters            | `count()` or dictionary            | `s.count("a")`                   |
| Find first occurrence       | `find()`                           | `s.find("a")`                    |
| Find last occurrence        | `rfind()`                          | `s.rfind("a")`                   |
| Remove spaces at ends       | `strip()`                          | `s.strip()`                      |
| Remove all spaces           | `replace()`                        | `s.replace(" ", "")`             |
| Divide into words           | `split()`                          | `s.split()`                      |
| Combine list words          | `join()`                           | `" ".join(words)`                |
| Remove duplicate characters | `set()` or dictionary              | Preserve order with a loop       |
| Check anagram               | Sort both strings or use frequency | `sorted(a) == sorted(b)`         |
| Find character frequency    | Dictionary                         | `freq[ch] = freq.get(ch, 0) + 1` |
| Check substring             | `in`                               | `"py" in s`                      |
| Change case                 | `lower()` / `upper()`              | `s.lower()`                      |

### Five useful coding patterns

Pattern 1 – Loop through every character

```
s = "hello"for ch in s:    print(ch)
```

Pattern 2 – Build a new string

```
s = "hello"result = ""for ch in s:    if ch != "l":        result += chprint(result)  # heo
```

Pattern 3 – Use a counter

```
s = "banana"count = 0for ch in s:    if ch == "a":        count += 1print(count)  # 3
```

Pattern 4 – Use a dictionary

```
s = "hello"freq = {}for ch in s:    freq[ch] = freq.get(ch, 0) + 1print(freq)# {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

Pattern 5 – Use two pointers

Useful for palindrome checks and comparing characters from both ends.

```
s = "madam"left = 0right = len(s) - 1is_palindrome = Truewhile left < right:    if s[left] != s[right]:        is_palindrome = False        break    left += 1    right -= 1print(is_palindrome)  # True
```

## 23. Common mistakes to avoid

| Mistake                                            | Why it is wrong                       | Correct way                             |
| -------------------------------------------------- | ------------------------------------- | --------------------------------------- |
| `s[0] = "A"`                                       | Strings are immutable                 | Create a new string                     |
| `s.upper()` expecting original to change           | Returns a new string                  | `s = s.upper()`                         |
| `s.find("x")` expecting an error                   | Returns `-1`                          | Use `index()` if error is desired       |
| `s.split()` expecting a string                     | Returns a list                        | Use `" ".join(...)` to combine          |
| `s.join(words)`                                    | Join belongs to separator             | `" ".join(words)`                       |
| `len(s) - 1` as last character                     | This is an index, not a character     | `s[-1]`                                 |
| `s[0:3]` expecting 4 characters                    | Stop is excluded                      | Use `s[0:4]`                            |
| `"Age: " + 20`                                     | Cannot concatenate string and integer | `"Age: " + str(20)`                     |
| `s.strip("abc")` expecting exact substring removal | Removes matching end characters       | Use `removeprefix()` / `removesuffix()` |

## 24. Quick revision checklist

Use this table to revise before interviews.

| Topic               | Must remember                 | Example                  |
| ------------------- | ----------------------------- | ------------------------ |
| String creation     | Quotes                        | `"Python"`               |
| Data type           | `str`                         | `type("Hi")`             |
| Indexing            | Starts from 0                 | `s[0]`                   |
| Negative indexing   | Starts from -1                | `s[-1]`                  |
| Slicing             | Stop excluded                 | `s[1:4]`                 |
| Reverse             | Negative step                 | `s[::-1]`                |
| Length              | Counts spaces too             | `len(s)`                 |
| Immutable           | Cannot update character       | `s[0] = "A"` gives error |
| Uppercase           | `upper()`                     | `s.upper()`              |
| Lowercase           | `lower()`                     | `s.lower()`              |
| Remove outer spaces | `strip()`                     | `s.strip()`              |
| Search              | `find()` / `index()`          | `s.find("a")`            |
| Count               | `count()`                     | `s.count("a")`           |
| Replace             | `replace()`                   | `s.replace("a","b")`     |
| Split               | String to list                | `s.split()`              |
| Join                | List of strings to string     | `" ".join(words)`        |
| Check letters       | `isalpha()`                   | `"abc".isalpha()`        |
| Check numbers       | `isdigit()`                   | `"123".isdigit()`        |
| Check alphanumeric  | `isalnum()`                   | `"abc123".isalnum()`     |
| Prefix/suffix       | `startswith()` / `endswith()` | `s.endswith(".py")`      |
| Formatting          | f-string                      | `f"Hi {name}"`           |
| Membership          | `in` / `not in`               | `"py" in s`              |
| Frequency           | Dictionary                    | `freq.get(ch, 0)`        |

## 25. What to practise next

I recommend learning strings in this order:

1. Indexing and slicing.
2. All important string methods.
3. Loops with strings.
4. Character frequency and duplicate characters.
5. Palindrome and anagram problems.
6. Easy-to-hard string coding questions.

Important interview advice: Don't just memorise methods. Practise solving the same problem using both built-in methods and loops. Interviewers often want to understand your logic.

Next, you can practise a beginner Python strings quiz with output-based tricky questions and coding questions, with answers hidden until submission.

🐍Send 5 Python string challenges dailyTap to set up