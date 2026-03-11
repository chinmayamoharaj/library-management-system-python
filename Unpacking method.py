#. What is Unpacking?

# Unpacking in Python is the process of assigning elements of a collection (tuple, list, set, dict, etc.) to multiple variables in a single statement.

# It extracts values from a collection and assigns them to variables.

# Works with tuples, lists, sets, dictionaries, strings, and even iterables.

# Unpacking Strings
s = "ABC"

a, b, c = s
print(a, b, c)

# Extended Unpacking
numbers = [1, 2, 3, 4, 5]

a, b, *rest = numbers

print(a)     # 1
print(b)     # 2
print(rest)  # [3, 4, 5]

*start, last = numbers
print(start)  # [1, 2, 3, 4]
print(last)   # 5

first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5