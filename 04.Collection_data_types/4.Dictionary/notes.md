9. Dictionary — dict
Use a dictionary to store key-value pairs.
student = {"name": "Vibha", "age": 25}print(student["name"])  # Vibha



Rules:
- Access values using their keys.
- Keys must be unique and hashable.
- Values can be duplicated and can have different data types.
- Assigning to an existing key updates its value.
student["age"] = 26print(student["age"])  # 26



Accessing a missing key using student["city"] raises KeyError. Use student.get("city") when a missing key should return None by default.