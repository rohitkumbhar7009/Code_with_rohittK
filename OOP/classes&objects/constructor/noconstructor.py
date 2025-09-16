# constructor is a special method in a class .  object properties initialize setup
"""
constructor is represent by 
__init__()

""" 

class car():
    def set_details(self,brand,color):
        self.brand = brand 
        self.color= color 

#create objects 
car1 = car()
car1.set_details("tesla","white")

print(car1.brand)
print(car1.color)