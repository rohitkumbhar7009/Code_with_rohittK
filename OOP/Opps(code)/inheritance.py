# Inheritance allows us to create specialized classes by reusing the properties of a parent class.


"""
Definition: Inheritance allows a class to reuse the properties and methods of another class (parent class). The child class can also add its own methods.

Real-Life Example:

Vehicle Types: A car and a bike inherit common vehicle properties like speed, fuel, etc.

"""

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Child Class Inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def display_details(self):
        super().display_details()
        print(f"Fuel Type: {self.fuel_type}")

# Object Creation
car1 = Car("Toyota", "Fortuner", "Diesel")
car1.display_details()


"""
✅ Explanation
Car inherits the Vehicle class using super().

display_details() is overridden to add fuel type details.
"""
