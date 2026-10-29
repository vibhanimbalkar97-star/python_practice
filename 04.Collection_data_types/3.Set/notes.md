8. Set — set
Use a set when you need unique values.
numbers = {10, 20, 10, 30}print(numbers)  # {10, 20, 30}



Rules:
- Duplicate elements are removed.
- Sets are unordered; don't rely on their display order.
- Elements must be hashable.
- Use add() to add an element.
numbers.add(40)



An empty {} creates a dictionary, not a set.
a = set()  # Empty setb = {}     # Empty dictionary



