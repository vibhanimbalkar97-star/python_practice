# Find the largest element in a tuple.
# t = (10, 20, 50, 80, 60, 60, 80)

# print(max(t))

# largest = t[0]
# index = 0
# for i in range(len(t)):
#     if t[i] > largest:
#         largest = t[i]
#         index = i
# print(largest)
# print(index)

# Find the smallest element in a tuple.
# print(min(t))

# smallest = t[0]
# for i in t:
#     if i < smallest:
#         smallest = i
# print(smallest)


# Find the second largest element.
# largest = float("-inf")
# sec_lar = float("-inf")
# for i in t:
#     if i > largest:
#         sec_lar = largest
#         largest = i
#     elif largest > i and i > sec_lar:
#         sec_lar = i
# print(largest)
# print(sec_lar)


# Count the frequency of each element.
# unique=[]
# for i in t:
#     if i not in unique:
#         print(i, "occurs", t.count(i), "times")
#         unique.append(i)
# print(unique)


# Remove duplicates from a tuple.
# t = (1,2,3,4,3,4,6)
# list = []
# for i in t:
#     if i not in list:
#         list.append(i)
# print(tuple(list))

# Reverse a tuple.
# for i in range(len(t)-1, -1, -1):
#     print(t[i])

# using slicing
# print(t[: :-1])

# using rversed
# result = tuple(reversed(t))
# print(result)

# Merge two tuples.
# t1 = (1, 2, 3)
# t2=(4,5,6)
# res = t1 + t2
# print(res)


# Find common elements between two tuples.
# t1 = (1,2,3,4,5)
# t2 = (4,5,3,8,9)

# list=[]
# for i in t1:
#     if i in t2:
#         list.append(i)
# print(tuple(list))

# Find the sum of all elements.
# t1=(1,2,3,4,5)
# sum = 0
# for i in t1:
#     sum = sum + i
# print(sum)

# Find the average of all elements.
# sum = 0
# for i in t1:
#     sum = sum + i
# print(sum / len(t1))

# Swap two variables using tuples.
# t = (1,2,3,4,5,3,5)
# res = list(t)
# res[1], res[3] = res[3], res[1]
# print(tuple(res))


# Return multiple values from a function using a tuple.
# def calculate(a,b):
#     return a+b, a-b
# res=calculate(9,8)
# print(res)

# Find duplicate elements in a tuple.
# list = []
# for i in t:
#     if t.count(i) > 1 and i not in list:
#         list.append(i)
# print(tuple(list))

# Remove duplicate elements while preserving order(order not change).
# list = []
# for i in t:
#     if i not in list:
#         list.append(i)
# print(tuple(list))


# Convert a tuple of strings to integers.
# t = ("10", "20", "30", "40")
# list = []
# for i in t:
#     list.append(int(i))
# print(tuple(list))

# Convert a tuple into a dictionary.
# t = (("name", "John"), ("age", 25), ("city", "Pune"))
# d = dict(t)
# print(d)

# keys = ("name", "age", "city")
# values = ("John", 25, "Pune")

# d = dict(zip(keys, values))
# print(d)

# Sort a tuple.
t = (40, 10, 30, 20)
result = tuple(sorted(t))
print(result)

# Descending order:
result = tuple(sorted(t, reverse=True))
print(result)

# Find missing numbers in a tuple.
# numbers = (1, 2, 4, 6, 7)
# list = []
# for i in range(numbers[0], numbers[-1] + 1):
#     if i not in list:
#         list.append(i)
# print(tuple(list))

# Rotate a tuple by k positions.
# k=2
# rotate = numbers[-k:] + numbers[:-k]
# print(rotate)

# k = 1
# rotate = numbers[k:] + numbers[:k]
# print(rotate)

# Filter elements based on a condition. find number greater than 5
# for i in numbers:
#     if i > 5:
#         print(i)