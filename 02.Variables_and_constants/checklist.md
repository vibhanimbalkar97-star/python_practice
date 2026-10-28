Final interview revision checklist
Concept	                              JavaScript	                     Python
Declare a variable	                 let x = 10	                          x = 10
Constant convention	                 const x = 10	                      X = 10 (naming convention only)
Uninitialized variable	             let x; gives undefined	              Reading an unassigned name raises NameError
Reassignment	                     Allowed with let	                  Allowed
Scope	                             let and const are block-scoped	      Functions create local scope; if blocks do not
Hoisting	                         var is initialized to undefined;    
                                     let/const have a temporal dead zone	No JavaScript-style variable hoisting
Mutable objects	                     const objects can be mutated	        Lists and dictionaries can be mutated
Modify global variable inside function	Depends on declaration/scope rules	Use global to reassign a module-level variable

Important: Python has no enforced constant keyword like JavaScript's const. Uppercase names such as MAX_SIZE = 100 are a convention that tells programmers not to change the value.

# Python Scope — From Basic to Tricky

Let's understand Python scope step by step in simple English, with a little Hindi explanation where useful. First, we will learn the rules with examples, then you will solve interview-style questions from easy to hard.

## 1. What is scope in Python?

Scope means where a variable can be accessed in your code.

Think of a variable like a person who has permission to enter certain rooms. Some variables are available everywhere in a module, while others are available only inside a function.

Python has four commonly discussed scope levels, remembered by LEGB:

## L

Local scope

A variable created inside a function.

```
def greet():    message = "Hello"    print(message)greet()  # Hello
```

`message` belongs to `greet()`. You normally cannot access it outside that function.

## E

Enclosing scope

A variable in an outer function, used by an inner function.

```
def outer():    x = 10    def inner():        print(x)    inner()outer()  # 10
```

`inner()` can access `x` from `outer()`.

## G

Global scope

A variable created at the module level, outside functions.

```
x = 100def show():    print(x)show()  # 100
```

The function can read the global `x` because there is no local `x` hiding it.

## B

Built-in scope

Names provided by Python, such as `print()`, `len()` and `sum()`.

```
numbers = [10, 20, 30]print(len(numbers))  # 3
```

Python finds `len` among its built-in names.

Hindi shortcut: Scope matlab variable kahan accessible hai. LEGB batata hai Python variable ko kis order mein search karta hai: Local → Enclosing → Global → Built-in.

## 2. Rule: A function can read a global variable

```
x = 10def show():    print(x)show()print(x)
```

Output:

```
10
10
```

Why? The function doesn't create its own `x`, so Python looks outside the function and finds the global variable.

Remember: Reading a global variable is allowed by default.

## 3. Rule: A local variable does not change the global variable

```
x = 10def show():    x = 20    print(x)show()print(x)
```

Output:

```
20
10
```

Why? The assignment `x = 20` inside the function creates a local variable named `x`. It is separate from the global `x`.

Think of two separate boxes

Global x

# 10

Local x

# 20

Changing the local box doesn't change the global box.

## 4. Rule: Assignment makes a name local inside a function

This is one of the most important interview rules.

```
x = 10def show():    print(x)    x = 20show()
```

Output: `UnboundLocalError`

Why does it fail?

Python sees `x = 20` anywhere in the function and decides that `x` is a local variable throughout that function, unless declared `global` or `nonlocal`.

Therefore, `print(x)` tries to read the local `x` before it has a value.

Hindi: Function ke andar assignment hai, isliye Python `x` ko local maanta hai. Pehle use read kar rahe hain, lekin value abhi assign nahi hui.

Compare these two:

| Code inside function                | Result                               |
| ----------------------------------- | ------------------------------------ |
| `print(x)` with no local assignment | Can read global `x`                  |
| `x = 20`                            | Creates/assigns local `x` by default |
| `print(x)` before `x = 20`          | `UnboundLocalError`                  |

## 5. Rule: Use `global` to reassign a global variable

```
x = 10def update():    global x    x = 20update()print(x)
```

Output:

```
20
```

`global x` tells Python: “Use the module-level variable `x`, not a new local variable.”

Without `global`, `x = 20` would normally create a local variable inside `update()`.

Important: `global` is needed for reassigning a global name, not for merely reading it.

## 6. Rule: Enclosing scope and `nonlocal`

When functions are nested, an inner function can read a variable from its enclosing function.

```
def outer():    x = 10    def inner():        print(x)    inner()outer()
```

Output: `10`

But what if the inner function must change the enclosing function's variable?

Use `nonlocal`.

```
def outer():    x = 10    def inner():        nonlocal x        x = 20    inner()    print(x)outer()
```

Output: `20`

- `global x` → refers to a module-level variable.
- `nonlocal x` → refers to an existing variable in an enclosing function scope.
- `nonlocal` does not refer to a global variable.

## 7. Rule: Shadowing — same name, different scope

Shadowing means a variable in an inner scope uses the same name as one in an outer scope.

```
x = 100def show():    x = 50    print(x)show()print(x)
```

Output:

```
50
100
```

The local `x` shadows the global `x` inside `show()`. It doesn't overwrite it.

## 8. Rule: `if`, `for`, and `while` do not create a new local scope

Unlike JavaScript's `let` and `const` block scope, ordinary Python `if`, `for`, and `while` blocks do not create their own variable scope.

```
if True:    x = 10print(x)
```

Output: `10`

A loop works similarly:

```
for i in range(3):    passprint(i)
```

Output: `2`

The loop variable remains available after the loop completes normally.

One exception to keep in mind: if a loop never runs, its loop variable may never be assigned.

```
for i in []:    passprint(i)  # NameError, if i wasn't defined earlier
```

## 9. Rule: Function parameters are local variables

```
x = 100def show(x):    print(x)show(5)print(x)
```

Output:

```
5
100
```

The parameter `x` receives the argument `5` and is local to the function. It does not replace the global `x`.

## 10. Rule: Python looks for names in LEGB order

```
x = "Global"def outer():    x = "Enclosing"    def inner():        x = "Local"        print(x)    inner()outer()
```

Output: `Local`

Python finds the closest matching name first.

If `inner()` did not define `x`, Python would find `"Enclosing"`. If the enclosing function also didn't define it, Python would look for `"Global"` and then built-ins.

## 11. Rule: `a = b` is name assignment, not variable linking

This connects to your confusion about reassignment.

```
a = 10b = ab = 20print(a)print(b)
```

Output:

```
10
20
```

When Python executes `b = a`, it reads the current value referenced by `a` and binds the name `b` to that value. Reassigning `b` later does not reassign `a`.

For integers, this is easy to see. Lists need a little more care:

```
a = [1, 2]b = ab.append(3)print(a)  # [1, 2, 3]print(b)  # [1, 2, 3]
```

Both names refer to the same list object, so mutating it through `b` is visible through `a`.

But:

```
a = [1, 2]b = ab = [7, 8]print(a)  # [1, 2]print(b)  # [7, 8]
```

Here, `b = [7, 8]` makes `b` refer to a new list. It doesn't change the original list that `a` refers to.

Remember the difference:

- Reassignment changes what a name refers to.
- Mutation changes an existing object's contents.
- Scope determines where a name is resolved and whether an assignment is local, global, or nonlocal.

## 12. More scope rules to know for interviews

### A. `nonlocal` must find an enclosing function variable

```
def outer():    def inner():        nonlocal x        x = 10    inner()outer()
```

This raises `SyntaxError` because no enclosing function has defined `x`. `nonlocal` cannot create a new enclosing variable.

### B. Comprehensions have their own scope in Python 3

```
x = 100values = [x for x in range(3)]print(values)  # [0, 1, 2]print(x)       # 100
```

The comprehension's `x` does not overwrite the outer `x` in Python 3.

### C. A nested function can remember an enclosing variable

```
def outer():    x = 10    def inner():        return x    return innerf = outer()print(f())  # 10
```

This is called a closure. The inner function retains access to the enclosing variable even after `outer()` has returned.

### D. Class scope has a special rule

```
x = "Global"class Example:    x = "Class"    def show(self):        print(x)Example().show()
```

Output: `Global`

A method does not automatically look up variables in its class namespace as an enclosing scope. Here, `x` resolves to the global variable.

Practice quiz: Python scope
Try these 12 questions in order, from easy to hard. Predict the exact output or error before submitting.
Python scope challenge
12/12 answered

Question 1 · Easy

What is the output?
x = 5

def show():
    print(x)

show()


A. 5

B. None

C. NameError

D. UnboundLocalError

Correct!

The function reads x without assigning to it, so Python finds the global variable.



Question 2 · Easy

What is the output?
x = 10

def show():
    x = 20
    print(x)

show()
print(x)


A. 20 then 20

B. 10 then 20

C. 20 then 10

D. Error

Correct!

The local x is 20; the global x remains 10.



Question 3 · Easy

What is the output?
if True:
    a = 7
print(a)


A. 7

B. None

C. NameError

D. SyntaxError

Correct!

An if block does not create a new scope in Python.



Question 4 · Medium

What happens?
x = 10

def f():
    print(x)
    x = 20

f()


A. 10

B. 20

C. NameError

D. UnboundLocalError

Correct!

The assignment makes x local throughout f. The print reads it before its local assignment.



Question 5 · Medium

What is the output?
x = 1

def f():
    global x
    x = 9

f()
print(x)


A. 1

B. 9

C. None

D. Error

Correct!

global x makes the assignment target the module-level variable.



Question 6 · Medium

What is the output?
def outer():
    x = 3
    def inner():
        print(x)
    inner()
outer()


A. 3

B. NameError

C. UnboundLocalError

D. None

Correct!

inner reads x from the enclosing function's scope.



Question 7 · Medium

What is the output?
def outer():
    x = 3
    def inner():
        nonlocal x
        x = 8
    inner()
    print(x)
outer()


A. 3

B. 8

C. NameError

D. SyntaxError

Correct answer: B. 8

nonlocal lets inner reassign x from the enclosing function.



Question 8 · Hard

What is the output?
x = 10

def f(x):
    x = x + 1
    print(x)

f(4)
print(x)


A. 5 then 11

B. 5 then 10

C. 11 then 10

D. Error

Correct!

The parameter x is local. It becomes 5, while the global x stays 10.



Question 9 · Hard

What is the output?
a = [1, 2]
b = a
b = b + [3]
print(a)
print(b)


A. [1, 2, 3] then [1, 2, 3]

B. [1, 2] then [1, 2, 3]

C. [1, 2] then [1, 2]

D. Error

Correct!

List concatenation with + creates a new list. Reassignment changes b's binding, not a's list.



Question 10 · Hard

What is the output?
x = 100
values = [x for x in range(3)]
print(x)


A. 0

B. 2

C. 100

D. NameError

Correct!

In Python 3, the comprehension variable x does not overwrite the outer x.



Question 11 · Hard

What happens?
def outer():
    def inner():
        nonlocal x
        x = 5
    inner()
outer()


A. x becomes 5 globally

B. NameError

C. SyntaxError

D. Output is None

Correct!

nonlocal requires an existing binding in an enclosing function scope. None exists here, so this is a SyntaxError.



Question 12 · Hard

What is the output?
x = 'Global'
class A:
    x = 'Class'
    def show(self):
        print(x)
A().show()


A. Global

B. Class

C. None

D. NameError

Correct answer: A. Global

A method's name lookup doesn't use the class namespace as an enclosing function scope. The global x is found.


Your score: 10/12
Retry quiz
## Your five-rule revision sheet

1. Read a global? Allowed by default.
2. Assign inside a function? The name is local by default.
3. Change a global inside a function? Use `global`.
4. Change an enclosing function's variable? Use `nonlocal`.
5. Write `b = a`? It rebinds `b`; it does not automatically make `a` and `b` independent copies of a mutable object.

Start with the quiz and send me your answers or score. We can then focus on the exact rules that are still confusing.