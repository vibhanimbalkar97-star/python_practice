# variable declaration
name = "Karan"
age  = 20
print(name, age)

# variable name rules
""""
name                               = allowed
1name                              = not allowed
na me                              = not allowed
_name                              = allowed
name2                              = allowed
user_name                          = allowed
user name                          = not allowed
age and Age                        = different case sensitive
class, if for while, bool          = not allowed resereved keyword
"""

"""
3. Variable declaration and assignment
Python doesn't require a separate variable declaration.
Unlike JavaScript, Python does not require let, var, or const to declare variables.
"""
# x = 10
" x  = variable name"
" =  = assignment operator "
" 10 = value assigned to x " 

x  =  5    # assignment
x  = 25    # reassignment
x = x + 5  # uses a old value and assign a new value
print(x)   # 30


"""
4. Dynamic typing
Python is dynamically typed. 
You can assign values of different types to the same variable.
"""
a = "Hello"
a = 5
a = 5.5
print(a) # 5.5

# 5. Multiple variable assignments
b, c, d = 1,2,3
print(b,c,d) # 1,2,3

# Same value for multiple variables:All three names initially refer to the same integer object.
a1 = b1 = c1 = 100
a1 = 20
print(a1, b1, c1) # 20, 100, 100

# Swapping variables:Python allows swapping without a temporary variable.
a2 = 10,
b2 = 20

a2,b2 = b2,a2
print(a2,b2)   # 20,10

"""
6. Local and global variables
Local variable
Created inside a function and normally accessible only within that function.
"""
def test():
    x1 = 10
    # print(x1)

test()           # 10 
# print(x1)        # NameError: name 'x1' is not defined.

"""
Global variable
Created outside a function.
"""
x3 = 26

def test2():
    print(x3)

test2()

# Modifying a global variable
# Use global when you want to reassign a module-level variable inside a function.

"""
without global
a3 = 25

def test1():
    a3 = 30

test1()
print(a3) //25
"""

"with global"
a3 = 25

def test1():
    global a3
    a3 = 30

test1()
print(a3) #30

"""7. The nonlocal keyword = nonlocal lets an inner function reassign a variable from its nearest enclosing function scope.
without nonlocal and if we write global it gives as outer function b3 as 4.
"""
def outer():
    b3 = 4

    def inner():
        nonlocal b3
        b3 = 5

    inner()
    print(b3)
outer() # 5

#8. Variable scope: LEGB rule
# a4 = "Global"
# # print(a4) # Global

# def Outer():
#     a4 = "Enclosing"

#     def inner():
#         a4 = "Local"
#         print(a4) #Local

#     inner()
#     # print(a4) Enclosing
# # print(a4) Global
# Outer()
# # print(a4) Global

a = [1, 2]
b = a
b.append(3)
print(a)  # [1, 2, 3]


a = [1, 2]
b = [1, 2]
b.append(3)
print(a, b)  # [1, 2] [1, 2, 3]

a = [1, 2]
b = a
b = b + [3]
print(a) # [1,2]
print(b) #[1,2,3]

def outer():
    e = 3
    def inner():
        nonlocal e
        e = 8
        print(e)
    inner()
    print(e)
outer()


