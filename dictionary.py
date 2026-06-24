# 1. Create a dictionary
# Create a dictionary of a student with:
# name
# age
# city
# # Print the dictionary.
student = {
    "name":"Ravi",
    "age": 22,
    "city":"Mumbai"
}
# print(student)

# 2. Access values
# print(student["name"])
# print(student["age"])
# print(student["city"])

# print(student.get("name"))

# 3. Add a new key
# student["marks"] = 90
# print(student)

# 4. Update value
# student["age"] = 23
# print(student)

# 5. Remove a key
# del student["city"]
# student.pop("city")
# print(student)

# 6. Check if key exists
# print("marks" in student)
# print("name" in student)

# if "city" in student:
#     print("Found")
# else:
#     print("Not found")

# 7. Find length
# Print total number of keys.
# print(len(student))

# 8. Print all keys
# for key in student:
#     print(key)

# 9. Print all values
# for value in student.values():
#     print(value)

# 10. Print all key-value pairs
# for key,value in student.items():
#     print(key, value)

# (Loops + Dictionary)

# marks = {
#     "Math":80,
#     "Science":90,
#     "English":85
# }
# 11. Sum all values
# sum = 0
# for value in marks.values():
#     sum = sum + value
# print(sum)

# 12. Find highest mark
# highest_subject = max(marks, key = marks.get)
# print(highest_subject, marks[highest_subject])

# highest_mark = 0
# highest_subject = ""
# for subject, mark in marks.items():
#     if highest_mark < mark:
#         highest_mark = mark
#         highest_subject = subject
# print(highest_subject,highest_mark)

# 13. Find lowest mark
# lowest = min(marks, key = marks.get)
# print(lowest, marks[lowest])

# subjects = list(marks.keys())
# lowest_subject = subjects[0]
# lowest_mark = marks[lowest_subject]
# for subject,mark in marks.items():
#     if mark < lowest_mark:
#         lowest_mark = mark
#         lowest_subject = subject
# print(lowest_mark, lowest_subject)

# 14. Count total values greater than 80
# count = 0
# for value in marks.values():
#     if value > 80:
#         count+=1;
# print(count)

# 15. Print only keys whose value is greater than 80
# count = 0
# for key, value in marks.items():
#     if value > 80:
#         print(key)
#         count+=1
       
# 16. Print dictionary in reverse order

# student = {
#     "name": "Rahul",
#     "age": 22,
#     "city": "Pune"
# }

# by using convert to list
# keys = list(student.keys())
# for i in range(len(keys)-1, -1, -1):
#     key = keys[i]
#     print(key, student[key])

# by using reversed
# for key in reversed(student):
#     print(key, student[key])

# by using key,value
# for key, value in reversed(student.items()):
#     print(key,value)

# 17. Count vowels in dictionary values
students = {
"name":"Rahul",
"city":"Pune"
}

# count = 0
# for value in students.values():
#     for char in value.lower():
#         if char in 'aeiou':
#             count+=1
# print(count)

# 18. Convert all values to uppercase
# for key in students:
#     students[key] = students[key].upper()
# print(students)


# 19. Print only string values
student = {
    "name": "Rahul",
    "age": 22,
    "city": "Pune",
    "marks": 85
}
# for value in student.values():
#     if isinstance(value, str):
#         print(value)

# 20. Print only integer values
# for value in student.values():
#     if isinstance(value, int):
#         print(value)

# isinstance("Rahul", str)     # True
# isinstance(22, int)          # True
# isinstance(85.5, float)      # True
# isinstance([1, 2], list)     # True
# isinstance((1, 2), tuple)    # True
# isinstance({"a": 1}, dict)   # True

# thinking questions
# 21. Swap keys and values
d = {
    "a": 1,
    "b": 2
}
# res = {}
# for key, value in d.items():
#     res[value] = key
# print(res)

# 22. Merge two dictionaries (Without using update())
d1 = {
    "a": 1,
    "b": 2
}

d2 = {
    "c": 3,
    "d": 4
}

# d1.update(d2)
# print(d1)

# res = {}
# for key,value in d1.items():
#     res[key] = value

# for key,value in d2.items():
#     res[key] = value

# print(res)

# 23. Count frequency of characters
# word = "banana"
# res = {}
# for char in word:
#     if char in res:
#         res[char] += 1
#     else:
#         res[char] = 1
# print(res) 

# 24. Count frequency of words
# text = "apple mango apple orange mango apple"
# words = text.split()
# res = {}
# for word in words:
#     if word in res:
#         res[word]+=1
#     else:
#         res[word] = 1
# print(res)

# 25. Find duplicate values
# d = {
#     "a": 10,
#     "b": 20,
#     "c": 10,
#     "d": 30
# }
# res = {}
# for value in d.values():
#     if value in res:
#         res[value] +=1
#     else:
#         res[value]=1
# print(res)

# for value, freq in res.items():
#     if freq > 1:
#         print(value) 

# 26. Remove duplicate values
# d = {
#     "a": 10,
#     "b": 20,
#     "c": 10,
#     "d": 30
# }

# seen = set()
# res={}
# for key, value in d.items():
#     if value not in seen:
#         res[key] = value
#         seen.add(value)
# print(res)

# 27. Sort dictionary by keys
d = {
    "c": 3,
    "a": 1,
    "b": 2
}
# for key in sorted(d):
#     print(key, d[key])

# 28. Sort dictionary by values
# sorted_items = sorted(d.items(), key=lambda item:item[1])

# for key, value in sorted_items:
#     print(key, value)
# item[0] → Sort by keys
# item[1] → Sort by values
# lambda item: item[1] → "Take each (key, value) tuple and use its value as the sorting key."

# 31. Create a dictionary from two lists
# keys = ["name","age","city"]

# values = ["Rahul",22,"Pune"]

# res = dict(zip(keys, values))
# print(keys, res)
