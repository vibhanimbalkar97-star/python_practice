# 41. Find the union of two sets.
s1={1,2,3}
s2={1,2,3,4,5}
# print(s1 | s2)

# 42. Find the intersection of two sets.
# print(s1 & s2)

# 43. Find the difference between two sets.
# print(s1-s2)

# 44. Find the symmetric difference.
# print(s1 ^ s2)

# 45. Check if one set is a subset of another.
# print(s1.issubset(s2))

# 46. Check if one set is a superset of another.
# print(s2.issuperset(s1))

# 47. Check whether two sets are disjoint.
# print(s1.isdisjoint(s2))

# 48. Remove duplicate elements from a list using a set.
# l = [1,2,2,3,4,4,5]
# r = set(l)
# print(r)

# 49. Find common elements between two lists using sets.
# l1 = [1,2,3]
# l2=[3,4,5]
# r = set(l1) & set(l2)
# print(r)

# 50. Find unique elements from two lists.
l1 = [1,2,3]
l2=[3,4,5]
# r = set(l1) ^ set(l2)
# print(r)

# 51. Find elements present only in the first set.
# r = set(l1) - set(l2)
# print(r)

# 52. Find elements present only in the second set.
# r = set(l2) - set(l1)
# print(r)

# 53. Find the total number of unique elements from two lists.
# r = set(l1) | set(l2)
# print(len(r))

# 54. Find the missing elements between two sets.
# set1={1,2,5,6}
# set2={3,4,7,8}
# r = set1 ^ set2
# print(r)

# 55. Check if two sets are equal.
# print(s1 == s2)

# 56. Find the maximum and minimum element in a set.
s = {40, 10, 30, 20, 5, 9}
# print(max(s))
# print(min(s))

# 57. Find the sum of all elements in a set.
# sum = 0
# for i in s:
#     sum+=i
# print(sum)

# 58. Filter even numbers from a set.
# a = set()
# for i in s:
#     if i%2==0:
#         a.add(i)
# print(a)

# 59. Convert a list into a set and back into a list.
# a = set(l1)
# print(list(a))

# 60. Create a frozenset and explain why it is immutable.
# fs = frozenset([1,2,3,4])
# print(fs)
# Why is it immutable?
# A frozenset cannot be changed after it is created.

# You cannot:
# Add elements
# Remove elements
# Update elements
# Because it is immutable, it is hashable, so it can be:
# Used as a dictionary key
# Stored inside another set
# Example
# fs = frozenset({1, 2})
# d = {fs: "Python"}
# print(d)
# Output
# {frozenset({1, 2}): 'Python'}