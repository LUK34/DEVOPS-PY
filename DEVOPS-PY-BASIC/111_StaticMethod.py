# Static Method
class MyClass:
    def add(self,a,b): # Non static method
        return a+b

    @staticmethod # Static method
    def multiply(a,b):
        return a*b

mc=MyClass()
print(mc.add(99,77)) # Non static method
print(MyClass.multiply(9,7)) #Static method



# `@staticmethod` decorator

# In Python, a static method is a method that does not receive the self or cls parameter,
# meaning it does not access or modify class or instance state. It's like a regular function,
# but lives inside the class's namespace for organizational purposes.

# Key Characterstics:
# Doesn't take self or cls as the first argument.
# Cannot access or modify class or instance variables.
# Used when the method logic is related to the class, but doesn't need to access class or instance data.

# When to use:
# The logic is related to the class conceptually.
# The method doesn’t need to access or change object or class state.
# You want to keep utility functions grouped inside a class.

