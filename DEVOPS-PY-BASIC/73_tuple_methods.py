#Methods of Tuple
print("Methods of Tuple:")
# len() ==> used to find the length of the tuple
# count() ==> return the number of occurrences of the specified element within the tuple
# index() ==> to get the index of the specified element, we can use "index()".
# sorted() ==> to sort the tuple, we can use "sorted()"

t = (11,22,33,44,55,55,44,33,22,11,10,20,11,22)
print("len() method")
print(len(t))
print("count() method")
print(t.count(11))
print("index() method")
#print(t.index(10))
#print(t.index(100))
#print(t.index(22)) # first occurrence
print("sorted() method of tuple in ascending order: ")
print(sorted(t))
print("sorted() method of tuple in descending order: ")
print(sorted(t,reverse = True))




