# Python Conditional Statements – Complete Beginner Notes

Conditional statements are used to make decisions in Python.

Simple meaning: If a condition is `True`, execute one block of code. If it is `False`, execute another block.

Example:

```
age = 18
if age >= 18:    
print("You can vote")
else:   
print("You cannot vote")
```

Output:

```
You can vote
```

Here, Python checks `age >= 18`. Since it is `True`, the `if` block executes.

Let's learn all the important concepts, rules, tricks, and interview questions.

## 1. Types of Conditional Statements

| Statement          | Meaning                     | When to use                           |
| ------------------ | --------------------------- | ------------------------------------- |
| `if`               | Checks one condition        | When one condition is needed          |
| `if-else`          | Chooses between two options | When condition is True or False       |
| `if-elif-else`     | Checks multiple conditions  | When multiple choices are available   |
| Nested `if`        | `if` inside another `if`    | When one condition depends on another |
| Short-hand `if`    | One-line `if`               | For simple conditions                 |
| Ternary expression | One-line `if-else`          | For choosing one value                |

# 16. Common Mistakes Beginners Make

| Mistake                         | Incorrect               | Correct              |
| ------------------------------- | ----------------------- | -------------------- |
| Forgetting colon                | `if x > 5`              | `if x > 5:`          |
| Using `=` in condition          | `if x = 5:`             | `if x == 5:`         |
| Incorrect indentation           | `print()` outside block | Indent by 4 spaces   |
| Forgetting input conversion     | `age = input()`         | `age = int(input())` |
| Wrong condition order           | Lowest marks first      | Highest marks first  |
| Using `and` instead of `or`     | `x < 0 and x > 10`      | `x < 0 or x > 10`    |
| Comparing with None using `==`  | `x == None`             | `x is None`          |
| Using `is` for value comparison | `x is 10`               | `x == 10`            |

### Example: Check a Number Between 1 and 10

Wrong:

```
if num >= 1 and num <= 10:    print("Valid")
```

This is actually correct.

But the following is wrong:

```
if num < 1 and num > 10:    print("Invalid")
```

A number cannot be both less than 1 and greater than 10 at the same time.

Correct:

```
if num < 1 or num > 10:    print("Invalid")
```

# 17. Problem-Solving Tricks

When solving conditional questions, follow this approach.

## 5-Step Approach

1. Understand the question

   What decision do you need to make?
2. Identify the conditions

   Write the conditions using comparison operators.
3. Choose the statement

   One condition → `if`; two options → `if-else`; multiple options → `if-elif-else`.
4. Check boundary values

   Test `0`, negative values, exact limits, and values just above/below limits.
5. Dry run the code

   Check each condition from top to bottom.

### Example: Find the Largest of Three Numbers

```
a = 10
b = 20
c = 15
if a >= b and a >= c:    
print("A is largest")
elif b >= a and b >= c:    
print("B is largest")
else:    print("C is largest")
```

Output:

```
B is largest
```

### Example: Leap Year

```
year = 2024
if year % 400 == 0:    
print("Leap year")
elif year % 100 == 0:    
print("Not a leap year")
elif year % 4 == 0:    
print("Leap year")
else:    
print("Not a leap year")
```

Why this order?

- Divisible by 400 → Leap year
- Divisible by 100 → Not leap year
- Divisible by 4 → Leap year
- Otherwise → Not leap year











