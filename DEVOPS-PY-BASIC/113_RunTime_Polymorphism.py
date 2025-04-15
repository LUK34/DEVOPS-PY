# Polymorphism
# 2 types of polymorphism
# compile time
# Method overriding
# run time
# Method overloading

class MyClass:
    def addition(self,a=0,b=0,c=0):
        print("The sum = ",a+b+c)

mc = MyClass()
mc.addition()
mc.addition(123) #Method Overloading
mc.addition(123,321) #Method Overloading
mc.addition(123,213,321) #Method Overloading
