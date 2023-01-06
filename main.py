
# Removing elements from Dictionary datatype in python using del

# The del statement removes the element associated with the key .
# Syntax :  del dictionary_name[key]

student_id = {111: "Crack", 112: "Mack", 113: "Joy"}

print("Before delete : ", student_id)

del  student_id[113]

print("After delete : ", student_id)
# Output
# Before delete :  {111: 'Crack', 112: 'Mack', 113: 'Joy'}
# After delete :  {111: 'Crack', 112: 'Mack'}

# ------Delete the whole dictionary using the del----------

student_id = {114: "Tom", 115: "Jerry", 116: "Mario"}

# delete student_id dictionary
del student_id     # deleted the student_id dictionary and student_id doesn't exist anymore

print(student_id)
# Output :
# NameError: name 'student_id' is not defined



