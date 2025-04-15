# Polymorphism
# 2 types of polymorphism
# compile time:
# Method overriding
# Run time:
# method Overloading

class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("The dog barks")

class Cat(Animal):
    def speak(self):
        print("The cat meows")

# Runtime Polymorphism
def animal_sound(animal: Animal):
    animal.speak()

a = Animal()
d = Dog()
c = Cat()

animal_sound(a)  # Output: The animal makes a sound
animal_sound(d)  # Output: The dog barks
animal_sound(c)  # Output: The cat meows
