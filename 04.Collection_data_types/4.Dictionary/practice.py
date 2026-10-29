"""
dict    =  store values as key value pair
           key names must be unique and hashable
           values can be duplicate but have the different data type
           empty dict shows as name = {}
           dict are mutable
           you can access value by using key
           assigning to existing key update the value
           if not key present raise keyerror, instead of use .get(key) = kuch nahi deta error 0/p gives by default
           if duplicate key it removed automatically

"""
students = {
    "name" : "ABC",
     "1"   : "ABC",
     "1.5" : 45,
     "True": "Yes"
}
students["name"] = "AAAA"
# students["email"]       #keyerror
students.get("email") # nothing gives o/p only
print(students)

print(type(5 / 2))
print(type(5 // 2))
