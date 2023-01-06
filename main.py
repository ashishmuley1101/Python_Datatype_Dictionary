
# Python dictionary all() method

#  The all() function returns True if all elements in the given iterable are true. If not, it returns False.
# The syntax of the all() function is: all(iterable)

s = {0: 'False', 1: 'False'}
print(all(s))  # O/p : False

s = {1: 'True', 2: 'True'}   # O/p : True
print(all(s))

s = {1: 'True', False: 0}  # O/p : False
print(all(s))

s = {}
print(all(s))  # O/p : True

s = {'0': 'True'}
print(all(s))  # O/p : True




