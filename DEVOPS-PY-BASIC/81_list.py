print("---------------------------------------------------------")
# using []
print("1. using []")
l1=[]
l2=[11,22,33,44,55]
l3=10,20,30,40
print(type(l1))
print(type(l2))
print(type(l3))
print("---------------------------------------------------------")
# list() is one of the type conversion function
# when we want to create a list from other collections
print("2. using list()")
l4=list("Python")
l5=list((12,24,36,48,60))
print(type(l4))
print(type(l5))
print("---------------------------------------------------------")
# run time list
print("3. using eval():")
l6=eval(input("Enter a list:"))
print(type(l6))
