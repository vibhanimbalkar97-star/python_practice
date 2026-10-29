"""
sets           = use when want unique value
                 it is unordered, don't relay on order
                 removes duplicate values
                 empty set shown as set()
                 it is used as {}
                 elements must be hashable
                 {} creates an empty dictionary
                 add elements use .add()
"""
nums = { "Hello", 10, 5.8, True, 5.8 }
# nums[2] = 5   reassigment does not support
nums.add(8)
print(nums)

num1 = {}    
print(type(num1)) # dict

num2 = set()
print(type(num2))

my_set = {1, 2, [3, 4]}
print(my_set)