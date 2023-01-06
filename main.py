
# Python Dictionary sorted() method

# The sorted() function sorts the elements of a given iterable in a specific order
# (ascending or descending) and returns it as a list.
# The syntax of the sorted() function is: sorted(iterable, key=None, reverse=False)
# iterable - A sequence (string, tuple, list) or collection (set, dictionary, frozen set) or any other iterator.
# reverse (Optional) - If True, the sorted list is reversed (or sorted in descending order). Defaults to False if not provided.
# key (Optional) - A function that serves as a key for the sort comparison. Defaults to None.

# dictionary
py_dict = {'e': 1, 'a': 2, 'u': 3, 'o': 4, 'i': 5}

# sorted based ok key*

print(sorted(py_dict))  # O/p : ['a', 'e', 'i', 'o', 'u']

print(sorted(py_dict, reverse=True))  # O/p : ['u', 'o', 'i', 'e', 'a']

py_dict1 = {1: 112, 6: 143, 3: 233, 5: 421, 7: 345}

print(sorted(py_dict1))  # O/p : [1, 3, 5, 6, 7]

print(sorted(py_dict1, reverse=True))  # O/p : [7, 6, 5, 3, 1]


