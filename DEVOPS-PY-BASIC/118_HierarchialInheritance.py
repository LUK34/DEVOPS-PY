# Hierarchial Inheritance:
# In Hierarchical Inheritance, multiple child classes inherit from the same parent class.
class Parent:
    def m1(self):
        print("Hi from Parent")
class Child(Parent):
    def m2(self):
        print("Hello from Child 1")
class Child2(Parent):
    def m3(self):
        print("Hello from Child 2")

print("---------------------------------")
print("From Child 2:")
ch2=Child2()
ch2.m3()
ch2.m1()
print("---------------------------------")
print("From Child 1:")
ch1=Child()
ch1.m2()
ch1.m1()
print("---------------------------------")