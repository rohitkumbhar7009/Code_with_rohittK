class Animal:
    def speak(self):
        print('Animals make sounds')

class Dog(Animal):
    def bark(self):
        print('Dogs Bark')



dog = Dog()
dog.bark()  
dog.speak()   
