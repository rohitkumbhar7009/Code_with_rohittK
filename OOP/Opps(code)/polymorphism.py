"""
Definition: Polymorphism means one interface, many implementations. It allows methods to behave differently based on the object using it.

Real-Life Example:

Animals: A dog and a cat both make sounds, but the sound is different (bark() for a dog, meow() for a cat).

"""

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):

        print("Cat meows")

# Polymorphism in action
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    animal.sound()


"""
✅ Explanation
sound() behaves differently depending on the object (Dog or Cat).

Python automatically resolves the correct method using Method Overriding.
"""