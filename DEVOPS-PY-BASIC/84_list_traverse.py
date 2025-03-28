print("---------------------------------------------------------")
print("Traversing the list:")
print("printing of list elements with +eve and -eve index")
print("--------------------------")
print("Positive Indexing:")
l1 = [10,20,30,40,50]
index = 0
for i in l1:
    print("The element at positive index",index,"is = ",i)
    index = index + 1
print("--------------------------")
print("Negative Indexing:")
index1 = 0
for j in l1:
    print("The element at negative index",index1 - len(l1),"is = ",j)
    index1 += 1
print("---------------------------------------------------------")
ind = 0
for k in l1:
    print("Element at positive index",ind,"and at negative index",ind-len(l1),"is = ",k)
    ind += 1
inds = -1
for l in l1[::-1]:
    print("Element at",inds,"is = ",l)
    inds = inds - 1
print("---------------------------------------------------------")