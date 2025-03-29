print("------------------------------------------------------------")
#add():
#-----
#-> if you want to add only one element to the set at any random position, we can use "add()".
#Syntax:
#	set-data.add(element)
s1 = {11,22,10,20,30,22,11,20,10,7,9}
print("Before we use add():")
print(s1)
# print(s1[0])
print("id value before we use add():")
print(id(s1))
s1.add(55)
print("After we use add():")
print(s1)
print("id value after we use add():")
print(id(s1))
print("------------------------------------------------------------")