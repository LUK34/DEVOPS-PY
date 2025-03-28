print("---------------------------------------------------------")
print("List functions:")
print("8.sort()")
print("When we want to sort the list we use sort() ")
print("--------------------------------")
l1 = [10,-1,0,11,-7,27,19,97,23,26,79]
print("Before sort:")
print(l1)
ind = 0
for i in l1:
    print("index = ",ind," value= ",i)
    ind=ind+1
print("--------------------------------")
print("After sort -> by default in ascending.")
l1.sort()
print(l1)
ind = 0
for i in l1:
    print("index = ",ind," value= ",i)
    ind=ind+1
print("--------------------------------")
print("Sorting in reverse -> sorting in descending.")
l1.sort(reverse = True)
print(l1)
ind = 0
for i in l1:
    print("index = ",ind," value= ",i)
    ind=ind+1
print("--------------------------------")

