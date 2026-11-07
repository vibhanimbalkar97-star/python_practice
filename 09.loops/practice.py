"""for
syntax : for variable in iterable:
         code

example : for char in str
         print(char)
"""
# fruits = ["apple", "banana", "cherry"]

# for fruit in fruits:
#     print(fruit)

# for i in [1,2,3,4,5]:
#     print(i)

# loop over string
# name = "python"
# for char in name:
#     print(char)

# # list
# num = [1,2,3,4,5]
# for n in num:
#     print(n)

# range 
"""
range(stop)
range(start, stop)
range(start,stop,step)
stop is excluded
step not be zero gives value error, in for loop without list print nothing in console
if no step value by default it is +1
range formula, next value = current value + step
print(list(range(5, 1))) = [] , start value > stop value
"""
# print(list(range(5)))             [0,1,2,3,4]
# print(list(range(1, 3)))          [1,2]
# print(list(range(5, 1)))          []
# print(list(range(5, 1, -1)))      [5,4,3,2]
# print(list(range(1, 5, 0)))       value error

# for i in range(5, 1):
#     print(i)                           nothing print


"""while loop
syntax: while condition:
         code

condition checked before body,
if condition intially false , body executes 0 times, nothing in console,
if infinite loop runs if update not given, so update variable,
check where print is written
"""
# i = 5
# while(i <= 5):
#     print(i)       #5
#     i+=1
#     print(i)      #6


"""
break       = stops loop
continue    = skip current iteration and continue
pass        = nothing, just a placeholder
"""
# for i in range(1,4):
#     if (i == 2):
#         break
#     print(i)               #1
# # print(i)                   #2

"""nested loops
i is outer loop, j is inner loop,
inner loop runs completely for every outer iteration,
inner loops starts again from its initial value for each iteration
"""
# for i in range(1,4):
#     for j in range(1, 3):
#         print(i,j)
#     print(f"outer: {i,j}")
# print(f"outer: {i,j}")

# for i in range(1,4):
#     for j in range(1, i+1):
#         print(i,j)
#     print(f"outer: {i,j}")
# print(f"outer: {i,j}")

"""How this works
- print("*", end="") prints stars on the same line.
- print() moves to the next line.
- Outer loop controls rows.
- Inner loop controls stars in each row."""

# for i in range(1,4):
#     for j in range(1, 3):
#         # print(i,j)
#         print("*", end="")
#     print()
    # print(f"outer: {i,j}")
# print(f"outer: {i,j}")

for i in range(1,4):
    for j in range(i):
        print("*", end="")
    print()

# n = [1,2,3,4,5]
# for num in n:
#     print(num)
