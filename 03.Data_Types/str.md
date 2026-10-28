## What does “Strings are immutable” mean in Python?

Immutable means you cannot change the existing string's characters after creating it.

### 1. Example: Trying to change one character

```
name = "Cat"name[0] = "B"print(name)
```

Output: `TypeError`

Why?

- `name[0]` refers to the first character, `"C"`.
- Python does not allow you to replace that character inside the existing string.
- So Python raises a `TypeError`.

### 2. How can we change `"Cat"` to `"Bat"`?

You can create a new string and assign it to the variable.

```
name = "Cat"name = "Bat"print(name)
```

Output:

```
Bat
```

Why does this work?

Initially, `name` refers to `"Cat"`. Then, `name = "Bat"` makes `name` refer to the new string `"Bat"`.

You did not modify `"Cat"`; you reassigned the variable.

### 3. Tricky interview example

```
a = "Cat"b = aa = "Bat"print(a)print(b)
```

Output:

```
Bat
Cat
```

Why?

`"Cat"`

Original string — unchanged

`b` → `"Cat"`

`a` → `"Bat"`

`a = "Bat"` reassigns only `a`. The name `b` still refers to `"Cat"`.

### 4. How to modify a string indirectly

If you want to replace a character, create a new string using slicing or a string method.

```
name = "Cat"name = "B" + name[1:]print(name)
```

Output:

```
Bat
```

Here, `"B" + name[1:]` creates a new string, `"Bat"`, and assigns it to `name`.

### Remember this interview rule

- `name[0] = "B"` → ❌ Not allowed; strings are immutable.
- `name = "Bat"` → ✅ Allowed; the variable is reassigned.
- `name = name.replace("C", "B")` → ✅ Allowed; `replace()` returns a new string.

In simple words: You cannot edit a string character directly, but you can create a modified string and assign it to the same variable.

3. String — str

Text enclosed in quotes.
name = "Python"print(name[0])  # Pprint(len(name))  # 6



Rule: Strings are immutable. You can create a new string, but you cannot change an individual character in place.