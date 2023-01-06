
# Dictionary Membership Test in python using in and not in over key

# test if a key is in a dictionary or not using the keyword in. Notice that the membership test is only
# for the keys and not for the values.
# Syntax :  del dictionary_name[key]

# Membership Test for Dictionary Keys
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# Output: True
print(1 in squares)  # O/p :  True

print(2 not in squares)  # O/p : True

# membership tests for key only not value
print(49 in squares)  # O/p : False




