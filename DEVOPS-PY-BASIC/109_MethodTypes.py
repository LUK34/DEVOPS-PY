# Types of methods:
# 4 ways
# 1. Method with no parameter and no return type
# 2. Method with parameter and no return type
# 3. Method with no parameter but return type
# 4. Method with parameter and return value.


class MyClass:
    # 1. Method with no parameter and no return type
    def noParameterNoReturn(self):
        print("Hi")

    # 2. Method with parameter and no return type
    def ParameterNoReturn(selfself,name):
        print("Good Afternoon",name)

    # 3. Method with no parameter but return type
    def noParameterReturn(self):
        return "Today is Monday"

    # 4. Method with parameter and return value.
    def parameterReturnType(self,name):
        return "Hey "+name+" I am starting to office"

mc=MyClass()
mc.noParameterNoReturn()
mc.ParameterNoReturn("Karthik")
print(mc.noParameterReturn())
print(mc.parameterReturnType("Luke"))