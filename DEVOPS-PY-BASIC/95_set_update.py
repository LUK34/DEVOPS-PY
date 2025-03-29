print("------------------------------------------------------------")
#update():
#---------
#when we want to add more than one element to the set, we can use "update()"
#Syntax:
#	set-data.update([e1, e2, e3,...])
print("Before we use update():")
s1 = {11,22,10,20,30,22,11,20,10,7,9}
print(s1)
print("After we use update():")
s1.update((100,200,300,400))
print(s1)
print("update() method creates an iterable for range(5, 50, 10): ")
print("Before update for range(5, 50, 10):")
print(s1)
print("After update for range(5, 50, 10):")
s1.update(range(5,50,10))
print(s1)
print(id(s1))
print("------------------------------------------------------------")