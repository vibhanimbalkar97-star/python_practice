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