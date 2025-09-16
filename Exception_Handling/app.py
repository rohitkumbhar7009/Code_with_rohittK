# compile time error 
"""
if 1 == 1 
 print ("ok")

"""



# Runtime Errors
"""
print (2 % 0)
"""

# logical Errors 
"""
a = int (input("enter a Number 1= "))
b = int (input("enter a Number 2= "))

print (a*b, "sum")  #declared sum but write multiply this is logical errors 

"""



try:
    num = int(input("enter a num = "))
    result = 10/ num 
    print (f'result:,{result}')

except ZeroDivisionError:
    print('You can not divide with Zero')

except ValueError:
    print("you can not divide with string ")

