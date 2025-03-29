# 2) get():
#---------
# i) when we want to access any value of the dictionary with respect to the key, we can use "get()".
# Syntax:
#	dictionary-name.get(key)

# ii) When we want to set new default value for any existing key of the dictionary, we can use get().
# But if the specified key is already existed with some value, then we can get with existed value. Otherwise we can get the specified key with default value.
# Syntax:
#	dictionary-name.get(key, default-value)

d = {'user':'Ravi','age':31,'weight':65.6}
print("Get the value of the corresponding key in dictionary:")
print(d.get('user'))
print(d.get('age'))
print(d.get('weight'))

# ii) When we want to set new default value for any existing key of the dictionary, we can use get().
# But if the specified key is already existed with some value, then we can get with existed value. Otherwise we can get the specified key with default value.
# Syntax:
# 	dictionary-name.get(key, default-value)
print("Set new default value for any existing key of the dictionary, we can use get():")
print(d.get('user','anonymous'))
print(d.get('age',18))
print(d.get('weight',70))





