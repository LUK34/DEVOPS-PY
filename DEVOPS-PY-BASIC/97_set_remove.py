#remove():
#---------
#-> when we want to remove the specified element from the set we can use "remove()".
#Syntax:
#	set-data.remove(element)

#Note:
#----
#if the specified element is not in the set, remove() can give "key error".

s1 = {1,11,10,20,22,20,7,9}
print("Before using remove()")
print(s1)
print("After using remove()")
s1.remove(11)
print(s1)
print("After using remove()")
s1.remove(22)
print(s1)







