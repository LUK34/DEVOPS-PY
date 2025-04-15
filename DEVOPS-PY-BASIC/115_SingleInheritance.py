# Single Inheritance:
# One child class inherits from one parent class.
class Parent:
    def m1(self):
        print("Hi")

class Child(Parent):
    def m2(self):
        print("Good Evening")

ch=Child()
ch.m2()
ch.m1()