
# Python dictionary any() method

#  Return True if any key of the dictionary is true. If the dictionary is empty, return False.
# The syntax of the any() function is: any(iterable)

# 0 is False
d = {0: 'False'}
print(any(d))  # O/p : False

# 1 is True
d = {0: 'False', 1: 'True'}
print(any(d))  # O/p : True

# 0 and False are false
d = {0: 'False', False: 0}
print(any(d))  # O/p : False

# iterable is empty
d = {}
print(any(d))  # O/p : False

# 0 is False
# '0' is True
d = {'0': 'False'}
print(any(d))  # O/p : True




