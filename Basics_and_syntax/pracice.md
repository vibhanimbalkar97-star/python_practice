## 2. Practice questions — Easy to hardest

Try answering these without running the code first. Each question tests a different Python basics or syntax rule.

## Python basics quiz

10/10 answered

1\. Variables

Easy

Predict the output:

x = 5\
x = x + 2\
print(x)

A. 5

B. 7

C. 12

D. Error

Correct — Answer: B. 7

x is reassigned to 5 + 2, which is 7.

2\. Data types

Easy

Predict the output:

x = "10"\
y = 5\
print(type(x).\_\_name\_\_)\
print(type(y).\_\_name\_\_)

A. int then str

B. str then int

C. str then str

D. int then int

Correct — Answer: B. str then int

"10" is a string, while 5 is an integer.

3\. Input and conversion

Easy

Predict the output:

x = "4"\
print(x \* 2)

A. 8

B. 44

C. Error

D. 4 4

Correct — Answer: B. 44

Multiplying a string by an integer repeats the string twice.

4\. Division

Medium

Predict the output:

print(7 // 2)\
print(7 / 2)

A. 3 and 3

B. 3.5 and 3.5

C. 3 and 3.5

D. 3.5 and 3

Correct — Answer: C. 3 and 3.5

Floor division gives 3; true division gives 3.5.

5\. Boolean values

Medium

Predict the output:

print(bool("False"))\
print(bool(""))

A. False, False

B. True, False

C. False, True

D. True, True

Correct — Answer: B. True, False

Any non-empty string is truthy, even "False". An empty string is falsy.

6\. Operator precedence

Medium

Predict the output:

print(2 + 3 \* 2 \*\* 2)

A. 20

B. 14

C. 16

D. 25

Correct — Answer: B. 14

Exponentiation first: 2\*\*2 = 4; then 3\*4 = 12; then +2 = 14.

7\. Chained assignment

Hard

Predict the output:

a = b = 10\
a += 2\
print(a, b)

A. 12 12

B. 10 12

C. 12 10

D. Error

Correct — Answer: C. 12 10

Both names initially refer to the integer 10. Reassigning a does not change b.

8\. Identity vs equality

Hard

Predict the output:

a = [1, 2]\
b = [1, 2]\
print(a == b)\
print(a is b)

A. True, True

B. False, False

C. True, False

D. False, True

Correct — Answer: C. True, False

The lists have equal contents but are two separate list objects.

9\. Negative floor division

Hard

Predict the output:

print(-7 // 2)\
print(-7 % 2)

A. -3, -1

B. -4, 1

C. -4, -1

D. -3, 1

Correct — Answer: B. -4, 1

Floor division rounds down toward negative infinity. Python's remainder satisfies a = (a // b) \* b + (a % b), so -7 = (-4)\*2 + 1.

10\. Short-circuit evaluation

Tricky

Predict the output:

x = 0\
result = x or "Python"\
print(result)

A. 0

B. False

C. Python

D. Error

Correct — Answer: C. Python

Zero is falsy, so or returns the second operand, the string Python.

## Your score: 10/10

Try again

Interview tip: Pay special attention to indentation, type conversion, operator precedence, truthy/falsy values, `is` vs `==`, and floor division. These are common sources of tricky Python output questions.