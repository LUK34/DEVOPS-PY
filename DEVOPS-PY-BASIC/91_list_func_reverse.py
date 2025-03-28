print("---------------------------------------------------------")
print("List functions:")
print("7.reverse()")
print("When we want to reverse the list we use ")
print("--------------------------------")
l1 = [10,11,20,22,30,33,40,44]
print("Before reversing:")
print(l1)
ind = 0
for i in l1:
    print("index = ",ind," value= ",i)
    ind=ind+1
print("--------------------------------")
print("After reversing:")
l1.reverse()
print(l1)
ind = 0
for i in l1:
    print("index = ",ind," value= ",i)
    ind=ind+1
print("--------------------------------")