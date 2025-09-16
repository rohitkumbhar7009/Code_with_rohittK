try:
    num1 = int(input('enter number 1:  '))
    num2 = int(input('enter number 2: '))

    try:
        result = num1 / num2
        print (f'Result :{result}')

    except ZeroDivisionError:
        print("you can not divide with Zero  ") 
except ValueError:
    print ("you must provide a valid input ") 




