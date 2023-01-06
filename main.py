
# Changing the Value of Dictionary in python using key

# use [] to change the value associated with a particular key.

# Syntax : dictionary_name[key] = value_new

student_id = {111: "Crack", 112: "Mack", 113: "Joy"}
print("Initial Dictionary: ", student_id)

student_id[112] = "Jack"

print("Updated Dictionary: ", student_id)
# Output
# Initial Dictionary:  {111: 'Crack', 112: 'Mack', 113: 'Joy'}
# Updated Dictionary:  {111: 'Crack', 112: 'Jack', 113: 'Joy'}

