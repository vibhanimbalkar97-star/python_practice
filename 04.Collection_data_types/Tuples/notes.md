7. Tuple — tuple
Use a tuple when you want an ordered collection whose elements cannot be reassigned.
point = (10, 20)print(point[0])  # 10



Rules:
- Ordered and allows duplicates.
- Cannot reassign an element.
- Usually written using ().
- A one-item tuple requires a comma.
a = (5,)  # Tupleb = (5)   # Integer, not tuple



If you try point[0] = 50, Python raises TypeError because tuples do not support item assignment.