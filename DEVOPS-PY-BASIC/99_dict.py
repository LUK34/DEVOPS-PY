# Dictionary Data Structure
# =========================
# When we want to create the data structures with key-value pairs, we can use "dictionaries".
# Syntax:
#	dictionary-name = {key1 : val1, key2 : val2, ......}

#Ex: Web application
#registration form
#	user-name : xxxxxx
#	mobile: xxxxxx
#	age : xxx

# Dictionary is also a pre-defined data structure because it has pre-defined class "dict".

# How to access dictionary elements:
# ----------------------------------
# - no index is possible to access the dictionary.
# - to access the dictionary elements, we can use "keys".
# Syntax:
#	dictionary-name[key]

# Is dictionary ordered -> Yes
# Is dictionary mutable or immutable -> mutable

print("----------------------------------------------------------------")

d = {'user':'ravi','age':31,'weight':65.6}
print("Data type: ")
print(type(d))
print(d['user'])
print(d['age'])
print(d['weight'])
print("Display all the elements in the dictionary:")
print(d)
print("The id value of dictionary:")
print(id(d))
d['user'] = 'Karthik'
print("After updating the username from ravi to karthik:")
print(d)
print("The id value of dictionary:")
print(id(d))
