# Mutable vs Immutable in Python (Beginner-Friendly)

The easiest way to understand this is:

- Mutable = you can change the existing object.
- Immutable = you cannot change the existing object; an operation that changes its value creates or refers to a different object instead.

Hindi: Mutable matlab existing object ko change kar sakte ho. Immutable matlab existing object ko directly change nahi kar sakte.

## 1. Mutable example — List

```
numbers = [10, 20, 30]numbers[0] = 99print(numbers)
```

Output:

```
[99, 20, 30]
```

Why? We changed the first element of the same list. We didn't need to create a new list.

Before

### 10

### 20

### 30

Change first element

After

### 99

### 20

### 30

Other common mutable types:

- `list` — `[1, 2, 3]`
- `dict` — `{"name": "Asha"}`
- `set` — `{1, 2, 3}`

## 2. Immutable example — Integer

```
x = 10x = 20print(x)
```

Output:

```
20
```

You might think we changed `10` into `20`. But that's not exactly what happened.

- `10` is an immutable integer.
- `x = 20` makes the name `x` refer to the integer value `20`.
- It does not modify the integer object `10`.

Other common immutable types:

- `int` — `10`
- `float` — `3.14`
- `bool` — `True`
- `str` — `"Hello"`
- `tuple` — `(10, 20, 30)`

## 3. Why does `a = b` confuse beginners?

Let's compare integers and lists.

### Example A: Integers (immutable)

```
a = 10b = ab = 20print(a)  # 10print(b)  # 20
```

`b = a` makes both names refer to the integer value `10`. Later, `b = 20` reassigns `b`. The value of `a` stays `10`.

### Example B: Lists (mutable)

```
a = [10, 20]b = ab[0] = 99print(a)  # [99, 20]print(b)  # [99, 20]
```

Here, `a` and `b` refer to the same list object. Changing the list through `b` also affects what you see through `a`.

### Visualize the difference

Integers

`a`

### 10

`b`

### 20

Reassigning b doesn't change a.

Lists

`a`

↘

`b`

↗

Same list object: `[99, 20]`

Mutating the shared list is visible through both names.

## 4. Important tricky rule: `+` versus mutation

```
a = [1, 2]b = ab = b + [3]print(a)  # [1, 2]print(b)  # [1, 2, 3]
```

Why? `b + [3]` creates a new list. Then `b` is reassigned to that new list. The original list referenced by `a` is unchanged.

Compare with `append()`:

```
a = [1, 2]b = ab.append(3)print(a)  # [1, 2, 3]print(b)  # [1, 2, 3]
```

`append()` modifies the existing list.

Interview shortcut: `b = b + [3]` creates a new list; `b.append(3)` mutates the existing list.

## 5. Tricky case: Strings are immutable

```
name = "Python"name = name + " Developer"print(name)
```

Output:

```
Python Developer
```

This does not modify the original `"Python"` string. Python creates a new string and reassigns `name` to it.

Trying to modify an individual character fails:

```
name = "Python"name[0] = "J"  # TypeError
```

Strings are immutable, even though you can reassign a variable that refers to a string.

## 6. What about tuples?

A tuple is immutable, but it can contain a mutable object.

```
items = ([1, 2], 10)items[0].append(3)print(items)  # ([1, 2, 3], 10)
```

This works because the tuple still refers to the same list; the list inside it is mutable.

But this fails:

```
items[0] = [7, 8]  # TypeError
```

You cannot replace an element of the tuple itself.

## 7. Test yourself: 5 tricky questions

Choose your answers first. The explanations appear when you submit.

Question 1. What is the output?

a = [1, 2]\
b = a\
b[1] = 9\
print(a)

A. [1, 2]

B. [1, 9]

C. [9, 2]

Correct!Both names refer to the same list. Changing index 1 through b is visible through a.

Question 2. What is the output?

a = 5\
b = a\
b = 8\
print(a)

A. 5

B. 8

C. Error

Correct!Integers are immutable. Reassigning b does not change a.

Question 3. What happens?

s = "Hello"\
s[0] = "Y"\
print(s)

A. "Yello"

B. "Hello"

C. TypeError

Correct!Strings are immutable, so you cannot assign to an individual character.

Question 4. What is the output?

a = [1, 2]\
b = a\
b = b + [3]\
print(a)

A. [1, 2]

B. [1, 2, 3]

C. Error

Correct!The + operation creates a new list, then b refers to it. a still refers to the original list.

Question 5. What is the output?

a = ([1, 2], 3)\
a[0].append(4)\
print(a)

A. ([1, 2], 3)

B. ([1, 2, 4], 3)

C. TypeError

Correct!The tuple cannot have its elements replaced, but its contained list can be mutated.

## Score: 5/5

Try again

The one rule to remember above everything else: Mutability belongs to the object, not the variable name. A variable can be reassigned whether it refers to a mutable or immutable object.