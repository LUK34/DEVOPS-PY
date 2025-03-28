print("---------------------------------------------------------")
print("List functions:")
print("1.count()")
print("When we want to count the number of occurrences of each element/specified element in a list we can use count().")
l1 = [1,2,3,4,5,5,3,1,1,3,5]
print(l1.count(1))
for i in l1:
    print("The number of occurrences for", i, "is = ", l1.count(i))
print("---------------------------------------------------------")