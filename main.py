
# Python Dictionary values() method

# The values() method returns a view object that displays a list of all the values in the dictionary.
# The syntax of the values() function is: dictionary.values()
#  object that displays the list of all the values

marks = {'Physics':67, 'Maths':87}

print(marks.values())
# Output: dict_values([67, 87])

# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

print(sales.values())
# Output:  dict_values([2, 4, 3])

# --------values() works when a dictionary is modified------------

# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

values = sales.values()

print('Original items:', values)

# delete an item from dictionary
del sales['apple']

print('Updated items:', values)

# Output
# Original items: dict_values([2, 4, 3])
# Updated items: dict_values([4, 3])



