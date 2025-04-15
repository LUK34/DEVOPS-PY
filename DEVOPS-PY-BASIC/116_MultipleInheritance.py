# Multiple Inheritance
# means that a child class inherits from more than one parent class.
# This allows the child class to access attributes and methods from all its parent classes.

class Parent1:
    def m1(self):
        print("Hi")
class Parent2:
    def m2(self):
        print("Good Evening")

class Child(Parent1,Parent2):
    def m3(self):
        print("Today I have work.")
ch=Child()
ch.m3()
ch.m2()
ch.m1()