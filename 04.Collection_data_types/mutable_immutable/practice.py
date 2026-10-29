"""
mutable           = we can change values in an existing object.

list, tuple, sets = mutable

immutable        = we cannot change the values in an existing object.

immutable        = int, float, string, tuple 
"""

name     = "Karan"
# name[0]  = "A"       # type error
name     = name + " ABC"
print(name)            # karan ABC

x   = 20
x   = 25
print(x)          # 25


num             = (1,2,3,4)
# num[0]          = 6     # type error

num1              = ([1,2], 3,4) 
num1[0].append(3)   #([1, 2, 3], 3, 4)
# num1[0]           = [8,9] # type error
print(num1)

a = 12
b = a
b = 13
print(a,b) # 12, 13

a1 = [1,2]
b1 = a1
b1 = [8,9]
print(a1,b1) #[1,2] [8,9]

a2 = (1,2)
b2 = a2
b2 = b2 + (3,)
print(a2,b2) #[1,2] [1,2,3]

a3    = [1,2,3]
b3    = a3
b3[0] = 10   
print(a3, b3)  #[10, 2, 3] [10, 2, 3]