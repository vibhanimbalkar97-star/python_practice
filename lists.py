lists = ["Apple", 20, 3.4, True]
# print(lists)
# print(lists[2])
# print(len(lists))

# loop by index value
# for i in range(len(lists)):
#     print(lists[i])

# direct lopp
# for i in lists:
#     print(i)

# reverse
# for i in range(len(lists)-1,-1,-1):
#     print(lists[i])

# nums = [10, 20, 30, 40, 50]
# del nums
# print(nums)
# print(nums[1] + nums[-1])

# remove elements 
# print(nums.remove(20))
# print(nums.pop(3))

# nums = [10, 20, 30, 40, 50]

# del nums[1]

# print(nums)

# nums = [10, 20, 30, 40, 50]

# print(len(nums))

# list comprehension
# squares = [i * i for i in range(5)]
# print(squares)

# even_num=[i for i in range(1,6) if i%2==0]
# print(even_num)

# double = [i * 2 for i in range(5)]
# print(double)

# copy list
# a = [1, 2, 3]
# b = a.copy()

# slicing
# b=a[:]


# list
# b=list(a)
# print(b)

# element exists
# print(4 in a)

# nums = [5, 2, 8, 1]

# print(sorted(nums))
# print(nums)

# nums = [5, 2, 8, 1]

# nums.sort()

# print(nums)

# questions
# Find the largest element in a list.
# list = [80, 30, 20, 60, 80, 10]

# largest = max(list)
# print(largest)

# largest = list[0]
# for i in list:
#     if largest < i:
#         largest = i
# print(f"{largest} largest number")




# Find the smallest element in a list.

# print(min(list))

# smallest = list[0]
# for i in list:
#     if smallest > i:
#         print(smallest)
#         smallest = i
# print(f"{smallest} smallest number")


# Remove duplicates from a list.
# numbers = [1, 2, 2, 3, 4, 4, 5]
# unique = list(set(numbers))
# print(unique)
# Note: set() removes duplicates but does not preserve the original order.

# preserve method
# unique = []
# for num in numbers:
#     if num not in unique:
#         unique.append(num)
# print(unique)

# Find the second largest number.
# numbers.sort()
# print(numbers[-2])

# largest = second = float("-inf")
# for i in numbers:
#     if i > largest:
#         second = largest
#         largest = i
#     elif largest > i and i > second:
#         second = largest
# print(second)

# Count occurrences of an element.
# print(numbers.count(5))

# count = 0
# for i in numbers:
#     if i == 1:
#         count+=1
# print(count)

# count every number
# unique = []
# for i in numbers:
#     if i not in unique:
#         print(f"{i} occurs {numbers.count(i)} times")
#         unique.append(i)
    
# Merge two sorted lists.
# list1 = [1, 3, 5]
# list2 = [2, 4, 6]
# merged = sorted(list1 + list2)
# print(merged)

# Rotate a list by k positions.
# Rotate means moving elements from one end of the list to the other.
# numbers = [1, 2, 3, 4, 5]
# rotate from right use -ve, left use +ve
# If k = 2, rotate right by 2 positions. [-k:] , [:-k] [4, 5, 1, 2, 3]
# asks for left rotation, [3,4,5,1,2] [k:] + [:k]

# k = 2
# rotated = numbers[2:] + numbers[:2]
# print(rotated)

# Find common elements between two lists.
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# common = []
# for num in list1:
#     if num in list2:
#         common.append(num)
# print(common)

# Split a list into even and odd numbers.
# numbers = [1, 2, 3, 4, 5, 6]
# even = []
# odd = []
# for i in numbers:
#     if i %2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)


# Find the sum of all elements in a list.
# numbers = [10, 20, 30, 40]
# print(sum(numbers))

# sum = 0
# for i in numbers:
#     sum += i
# print(sum)

# Remove all empty strings from a list.
# words = ["Python", "", "Java", "", "C++", ""]

# word=[]
# for i in words:
#     if i != "":
#         word.append(i)
# print(word)

# Find duplicates in a list.
# numbers = [1, 2, 2, 3, 4, 4, 5]

# result = []
# for i in numbers:
#     if numbers.count(i) > 1 and i not in result:
#         result.append(i)
# print(result)

# Convert a list into a dictionary.
# keys = ["name", "age", "city"]
# values = ["John", 25, "Pune"]
# # result = dict(zip(keys, values))
# # print(result)

# result = {}
# for i in range(len(keys)):
#     result[keys[i]] = values[i]
# print(result) 

# Find pairs with a given sum.
# numbers = [1, 2, 3, 4, 5]

# target = 6
# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         if numbers[i] + numbers[j] == target:
#             print(numbers[i], numbers[j])


# Shuffle a list randomly.
# numbers = [1, 2, 3, 4, 5]
# import random
# random.shuffle(numbers)
# print(numbers)

# Generate a list of prime numbers.

# Find missing numbers in a sequence.
# numbers = [1, 2, 4, 6, 7]
# result = []
# for i in range(numbers[0], numbers[-1] + 1):
#     if i not in numbers:
#         result.append(i)
# print(result)

# Swap two elements in a list.
# numbers = [10, 20, 30, 40]
# Swap index 1 and 3.
# numbers[1], numbers[3] = numbers[3], numbers[1]
# print(numbers)

# Convert a list of strings to integers.
# numbers = ["10", "20", "30", "40"]

# result=[]
# for i in numbers:
#     result.append(int(i))
# print(result)

# Filter elements based on conditions.
# Find numbers greater than 20.
# numbers = [10, 25, 30, 15, 40]

# result = []
# for i in numbers:
#     if i > 20:
#         result.append(i)
# print(result)

# Using list comprehension:
# result = [i for i in numbers if i > 20]
# print (result)

# 6 Print positive and negative elements of an List?
# numbers = [10, 25, -30, -15, 40]
# positive = []
# negative = []
# for i in numbers:
#     if i > 0:
#         positive.append(i)
#     else:
#         negative.append(i)
# print(positive, negative)

# print("positive elements are ")
# for i in numbers:
#     if i >= 0:
#         print(i)
# print("negitive elements are")
# for i in numbers:
#     if i < 0:
#         print(i)

# 6 Mean of List elements?
# numbers = [10, 25, 30, 15, 40]
# sum = 0
# for i in numbers:
#     sum = sum + i 
# print(sum/ len(numbers))
    

# 6 Find the greatest element and print its index too?
# numbers = [12,435,67,89,23,25,69]
# largest = numbers[0]
# index = 0
# for i in range(len(numbers)):
#     if largest < numbers[i]:
#         largest = numbers[i]
#         index = i
# print(f"{largest} is largest number at index {index}")

# 6 Find the second greatest element?
# Initialize the variables to negative infinity so they don't incorrectly start with the first element.
# largest = float("-inf")
# sec_lar = float("-inf")
# lar_index = -1
# sec_index = -1
# for i in range(len(numbers)):
#     if numbers[i] > largest:
#         sec_lar = largest
#         sec_index = lar_index

#         largest = numbers[i]
#         lar_index = i
#     elif largest > numbers[i] and numbers[i] > sec_lar:
#         sec_lar = numbers[i]
#         sec_index = i
# print(f"Largest = {largest} at index {lar_index}")
# print(f"Second Largest = {sec_lar} at index {sec_index}")
# Why -1?

# -1 is commonly used as a sentinel value, meaning:

# "Not found"
# "Not assigned yet"
# "Invalid index"
# We initialize the indices with -1 because it means "no valid index found yet.
# Before the loop even starts, Python thinks the largest element is already at index 0, which isn't true yet.


# 6 Check if List is sorted or not.
# a = [12,13,18,15,16]
# for i in range(len(a) - 1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break
# else:
#     print("your list is sorted")