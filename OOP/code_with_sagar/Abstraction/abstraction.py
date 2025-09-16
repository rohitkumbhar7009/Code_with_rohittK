# Abstraction means Complex in detail ko  hide krna  and sirf vahis how krana jitna user keliye jaruri hai 

from abc import ABC,abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass # no implementation 

class Car(Vehicle):
    def start(self):
        print('Car Starts with a key ')

class Bike (Vehicle):
    def start(self):
        print('start with button')

car = Car()
bike = Bike()

car.start()
bike.start()