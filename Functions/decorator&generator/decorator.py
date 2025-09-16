# decorator  => main function ke   andar new function add krna without  changing the main function code 

# create decorator 
  

def my_decorator(func):
    def wrapper():
        print("Something is happening before the functions is called ")  #1st call 
        func()
        print("Something is happening after the functions is called ") #3rd call
    return wrapper

@my_decorator   #2nd call
def say_hello():
    print("hello")

say_hello()   




