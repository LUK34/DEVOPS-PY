# popitem():
#----------
#Syntax:
#	d.popitem()

print("In Python dictionaries, keys must be unique. If the same key appears more than once, the last occurrence overwrites the earlier ones.")
d = {'apple' : 121,'banana':222,'cherry':212,'grape':300,'apple':321}
print("Before popping, dictionary is as follows: ")
print(d)
print("After popping, dictionary is as follows: ")
d.popitem()
print(d)
print("After adding kiwi-> dictionary is as follows: ")
d['kiwi'] = 121
print(d)