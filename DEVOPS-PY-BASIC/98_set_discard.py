#discard():
#---------
#-> also remove the specific element from the set.
#Syntax:
#	set-data-name.discard(element)
#Note:
#-----
#No math operations like concatenation and repetition allowed on  sets.

s1 = {1,11,10,20,22,20,7,9}
print("Before using discard()")
print(s1)
print("After using discard()")
s1.discard(11)
print(s1)
print("After using discard()")
s1.discard(22)
print(s1)