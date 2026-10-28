## 1. Hashable — Meaning

English: An object is hashable if Python can calculate a stable hash value for it, which helps Python use it as a dictionary key or set element.

Hindi: Hashable ka matlab hai ki Python kisi object ki ek stable hash value calculate kar sakta hai, jisse us object ko dictionary ki key ya set ke element ke roop mein use kar sakte hain.

Example:

```
print(hash(10))       # Worksprint(hash("hello"))  # Works
```

## 2. Element — Meaning

English: An element is an individual item inside a collection, such as a list, tuple, or set.

Hindi: Element ka matlab hai kisi collection ke andar maujood ek item ya value.

Example:

```
numbers = [10, 20, 30]
```

Here, `10`, `20`, and `30` are individual elements of the list.

## 3. Hashable elements — Meaning

English: Hashable elements are items that Python can calculate hash values for and that can be used in a set or as dictionary keys.

Hindi: Hashable elements woh items hain jinki hash value Python calculate kar sakta hai aur jinhe set mein ya dictionary ki key ke roop mein use kar sakte hain.

```
my_set = {10, "hello", (1, 2)}print(my_set)  # Works
```

All three elements are hashable.

But:

```
my_set = {10, [1, 2]}
```

This raises `TypeError` because a list is unhashable.

## Remember this difference

| Term             | Simple English                     | Hindi                                     |
| ---------------- | ---------------------------------- | ----------------------------------------- |
| Hashable         | An object with a stable hash value | Jiski stable hash value calculate ho sake |
| Element          | An individual item in a collection | Collection ke andar ek item               |
| Hashable element | An item that can be used in a set  | Aisa item jo set mein use ho sake         |

Interview tip: Dictionary keys and set elements must be hashable. Common hashable types include `int`, `str`, and tuples containing only hashable values.

# What does Hashable mean in Python?

In simple words, a hashable object is an object that Python can give a stable hash value to, so it can be used as a dictionary key or a set element.

Think of a hash value as a kind of number-based ID that Python calculates for an object.

## 1. Simple example

```
x = 10print(hash(x))
```

Output: a hash value for `10` (typically `10`).

Python's `hash()` function calculates the hash value. For strings, the exact value can vary between Python runs.

## 2. Which types are hashable?

| Type    | Hashable? | Example    |
| ------- | --------- | ---------- |
| `int`   | Yes       | `10`       |
| `float` | Yes       | `3.14`     |
| `str`   | Yes       | `"hello"`  |
| `bool`  | Yes       | `True`     |
| `tuple` | Sometimes | `(1, 2)`   |
| `list`  | No        | `[1, 2]`   |
| `dict`  | No        | `{"a": 1}` |
| `set`   | No        | `{1, 2}`   |

Important: A tuple is hashable only if all its elements are hashable.

```
print(hash((1, 2)))     # Worksprint(hash((1, [2, 3])))  # TypeError
```

The second tuple contains a list, which is unhashable.

## 3. Why do dictionary keys need to be hashable?

Python uses hashes to help find dictionary entries efficiently.

```
student = {    "name": "Riya",    "age": 25}print(student["name"])  # Riya
```

Here, `"name"` is a hashable string, so it can be used as a dictionary key.

But this fails:

```
student = {    [1, 2]: "Riya"}
```

Output: `TypeError: unhashable type: 'list'`

Why? Lists can change after creation, so Python doesn't allow them to be dictionary keys.

## 4. Why can a tuple be a key but a list cannot?

Tuple: `(10, 20)`

Its elements cannot be replaced, and if all elements are hashable, the tuple can be a dictionary key.

List: `[10, 20]`

Its elements can be changed, so the list itself is unhashable.

One subtle point: immutable does not always mean hashable. For example, a tuple containing a list is immutable as a tuple, but it is still unhashable because of the list inside it.

## 5. Try these 3 questions

1\. Which can be a dictionary key?

[1, 2]

(1, 2)

{1, 2}

Correct!A tuple containing only hashable elements is hashable.

2\. What happens?

print(hash([1, 2]))

Prints a number

TypeError

Prints None

Correct!Lists are unhashable, so hash([1, 2]) raises TypeError.

3\. Is this tuple hashable?

x = (1, 'hello', True)

Yes

No

Correct!Integers, strings, and booleans are hashable, so this tuple is hashable.

## Score: 3/3

Interview answer: Hashable means an object has a stable hash value and can be used as a dictionary key or set element. Common examples are integers, strings, and tuples containing only hashable elements.