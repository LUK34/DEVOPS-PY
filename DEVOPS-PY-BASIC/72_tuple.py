# Tuple is one of the collection data structure.
# When we want to define a variable with more than one value,
# we can allow to collect like `Tuple`
print("-------------------------------------------------------------")
v1=(23)
print(v1)
v2=()
print(v2)
v3=(1,2,3,4,5,6,1.2,2.3,2-3j,True)
print(v3)
v4=(1,3,4,5,7)
print(v4)
print("-------------------------------------------------------------")
# is it possible to define the tuple without ()?
v5=1,2,3,4,5
print(v5) #Yes
print("-------------------------------------------------------------")
#is it possible to define the tuple with single element?
v6=(100,)
print(v6) #Yes
v7=(200,)
print(v7) #Yes
print("-------------------------------------------------------------")
v8=tuple()
print(v8)
v9=tuple([12,23,34,45])
print(v9)
v10=tuple("string")
print(v10)
print("-------------------------------------------------------------")
print("Accessing of tuple data: Indexing and slicing")
# tuple is ordered
x = tuple("String")
print(x)
print(x[0])
print(x[1])
print(x[2])
print(x[-1])#last
print(x[-2])#second last
print(x[::-1])#last to first
print("-------------------------------------------------------------")
print("Looping on tuple:")
t = 11,'apple',1-23j,True,23.32
for i in t:
    print(i,end="\t")
# tuple is immutable

# after the definition, no modification is allowed on the tuple
#t[0]=22
#print(t) # tuple does'nt support item assignment
print("\n-------------------------------------------------------------")
# Can we convert tuple to list??
l=list(t) #yes
print(l) #yes
print("\n-------------------------------------------------------------")
# Can we convert list to tuple??
t=tuple(l) #yes
print(t) #yes
print("\n-------------------------------------------------------------")



