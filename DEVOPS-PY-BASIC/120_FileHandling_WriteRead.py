# File handling in Python lets you create, read, write, and delete files using built-in functions.

fp=open("abc.txt","w")
fp.write("Hello World")
data=fp.read()
print(data)