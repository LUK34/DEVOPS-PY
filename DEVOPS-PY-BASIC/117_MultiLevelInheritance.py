# Multilevel Inheritance
#  means a class is derived from a class that is also derived from another class.
# It forms a chain of inheritance.
class GrandParent:
    def m1(self):
        print("Hi")

class Parent(GrandParent):
    def m2(self):
        print("Hello")

class Child(Parent):
    def m3(self):
        print("Good Evening")

print("----------------------")
ch=Child()
ch.m3()
ch.m2()
ch.m1()
print("----------------------")
p=Parent()
p.m2()
p.m1()
print("----------------------")
g=GrandParent()
g.m1()
print("----------------------")
