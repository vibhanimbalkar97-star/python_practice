2. Collection data types
Collections store multiple values. The important difference is whether they are ordered, changeable, and allow duplicates.
Type	Example	Mutable?	Duplicates?
list	[10, 20, 10]	Yes	Yes
tuple	(10, 20, 10)	No*	Yes
set	{10, 20}	Yes	No
dict	{"age": 25}	Yes	Keys must be unique

Tuple elements cannot be reassigned, but a tuple can contain mutable objects such as lists.


6. List — list
Use a list when you need an ordered collection that can change.
numbers = [10, 20, 30]numbers.append(40)print(numbers)  # [10, 20, 30, 40]



Rules:
- Indexing starts at 0.
- Duplicates are allowed.
- Items can be changed, added, or removed.
- Use [] to create a list.
numbers[0] = 100print(numbers)  # [100, 20, 30, 40]



If you try to access numbers[10] when the list has only four elements, Python raises IndexError.