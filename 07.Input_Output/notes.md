# Python Input and Output – Beginner Interview Notes

In Python, Input means taking data from the user, and Output means displaying data to the user.

Let's understand all the important concepts with simple examples, rules, and interview points.

## 1. What is Input in Python?

Python uses the `input()` function to take data from the user.

### Syntax

```
variable = input("Enter something: ")
```

### Example

```
name = input("Enter your name: ")print(name)
```

Output:

```
Enter your name: Vibha
Vibha
```

How it works:

1. `input()` displays the message.
2. The user enters data.
3. Python stores the entered data in the variable.
4. `print()` displays the value.










```

# Quick Interview Revision Notes

| Concept                           | Rule                                  |
| --------------------------------- | ------------------------------------- |
| `input()`                         | Always returns a string               |
| `int(input())`                    | Converts input to integer             |
| `float(input())`                  | Converts input to float               |
| `input().split()`                 | Separates input into strings          |
| `map(int, input().split())`       | Converts separated values to integers |
| `list(map(int, input().split()))` | Creates a list of integers            |
| `print()`                         | Displays output                       |
| `sep`                             | Separates values in print             |
| `end`                             | Controls what comes at the end        |
| `f"{value}"`                      | Inserts variable values into strings  |
| `f"{num:.2f}"`                    | Displays two decimal places           |
| `sum()`                           | Calculates total                      |
| `max()`                           | Returns maximum                       |
| `min()`                           | Returns minimum                       |
| `try-except`                      | Handles invalid input errors          |

# Practice Questions – Python Input & Output

Try these questions without looking at the answers.

## 10 Interview Practice Questions

0/10 answered

1\. What is the output?

a = input()\
print(type(a))



\<class 'int'>

\<class 'str'>

\<class 'float'>



2\. What is the output?

a = input()\
b = input()\
print(a + b)



30

1020

Error



3\. What is the output?

a, b = map(int, input().split())\
print(a + b)

Input: 10 20

1020

30

['10', '20']



4\. What is the output?

print("A", "B", "C", sep="-")



A B C

ABC

A-B-C



5\. What is the output?

print("Hello", end=" ")\
print("Python")



Hello\nPython

Hello Python

HelloPython



6\. What is the output?

print(bool(input()))

Input: False

False

True

Error



7\. What is the output?

numbers = list(map(int, input().split()))\
print(sum(numbers))

Input: 1 2 3 4

10

1234

[1, 2, 3, 4]



8\. What is the output?

price = 12.567\
print(f"{price:.2f}")



12.56

12.57

12.567



9\. What is the output?

a = "10"\
print(int(a))\
print(type(a))



10 then int

10 then str

Error



10\. What error occurs?

a, b = input().split()

Input: 10 20 30

TypeError

ValueError

No error



Submit Answers

Interview tip: When solving coding questions, always check whether the input should be a string, integer, float, or list. Most beginner input/output mistakes happen because `input()` returns a string.