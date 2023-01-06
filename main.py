
# Python Dictionary keys() method

# The keys() method extracts the keys of the dictionary and returns the list of keys as a view object.
# The syntax of the keys() function is: dict.keys()
#  object that displays the list of all the keys

numbers = {1: 'one', 2: 'two', 3: 'three'}

# extracts the keys of the dictionary
dictionaryKeys = numbers.keys()

print(dictionaryKeys)
# Output: dict_keys([1, 2, 3])

employee = {'name': 'Phill', 'age': 22}

# extracts the dictionary keys
dictionaryKeys = employee.keys()

print('Before dictionary update:', dictionaryKeys)

# adds an element to the dictionary
employee.update({'salary': 3500.0})

# prints the updated view object
print('After dictionary update:', dictionaryKeys)

# Output:
# Before dictionary update: dict_keys(['name', 'age'])
# After dictionary update: dict_keys(['name', 'age', 'salary'])



