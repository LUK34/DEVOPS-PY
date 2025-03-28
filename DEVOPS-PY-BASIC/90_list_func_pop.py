print("---------------------------------------------------------")
print("List functions:")
print("6.pop()")
print("When we want to remove the specified element from the list, we can use pop().")
print("--------------------------------")
l1 = [10,11,20,22,30,33,40,44]
print("Before pop:")
print(l1)
ind = 0
for i in l1:
    print("index = ",ind," value= ",i)
    ind=ind+1
print("--------------------------------")
print("After popping index value 0:")
l1.pop(0)
print(l1)
ind = 0
for i in l1:
    print("index = ",ind," value= ",i)
    ind=ind+1
print("--------------------------------")
print("After popping index value 1:")
l1.pop(1)
print(l1)
ind = 0
for i in l1:
    print("index = ",ind," value= ",i)
    ind=ind+1
print("--------------------------------")
print("After popping index value 2:")
l1.pop(2)
print(l1)
ind = 0
for i in l1:
    print("index = ",ind," value= ",i)
    ind=ind+1
print("--------------------------------")
