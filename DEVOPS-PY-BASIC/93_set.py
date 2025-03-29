#Set Data Structure:
#===================
#() ==> allows duplication
#[] ==> allows duplication
#{} ==> not allows the duplication

#1) When we need to create the data structure which is not with any duplication then, we can use the set.
#2) set can be defined with {} all the elements {} must be separate with comma.
#3) set can possible to define homogeneous elements and with heterogeneous elements also.
#4) Set is also the pre-defined data, so we have a pre-defined class named as "set".

#Is set ordered data?
#--------------------
#Not ordered.
#-> indexing is not possible.
#-> slicing also not possible.

#Is set mutable or immutable?
#----------------------------
#Mutable
print("------------------------------------------------------------")
s1 = {}
print(type(s1)) # dictionary
print("------------------------------------------------------------")
# to create empty set, we can use "set()".
s2 = set()
print(type(s2))#set
s2 = {11,10,22,20,11,10,22,20}
print(type(s2))#set
s3 = {'a',True,1.2,12-23j,23}
print(type(s3))#set
print("------------------------------------------------------------")










































