# polymorphism with classes  method overriding

"""
# Method Overriding -  Jo bhi child class ki methods hai vo uske parent class ki methods hai usko override kar jayegi  

"""


# eg 

class Bird():
    def sound(self):
        print(f"Birds Maked Sound")

class Crow(Bird):
    def sound(self):
         print(f'Crows Say "Caw Caw "')

class Parrot(Bird):
    def sound(self):
        print (f'Parrot sound , Squawk')

bird1 = Crow()
bird2 = Parrot()


bird1.sound()

bird2.sound()

birdSOund = Bird()

birdSOund.sound()