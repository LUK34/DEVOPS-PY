# Class method:
# `@classmethod` decorator
# In Python, a class method is a method that is bound to the class and not the instance of the class.
# It has access to the class itself via a special first parameter usually named cls.

class Dog:
    species="Canis familiaris"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def speciesInfo(cls):
        return f"All dogs belong to the species:{cls.species}"

x=Dog.speciesInfo()
print(x)