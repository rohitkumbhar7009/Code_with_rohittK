# check password strength 


def check_password (password):
  if len(password) < 8:
     raise Exception(" Error : Password must be >= 8 Character")  #by using custom Exception 
  print("Password is strong..!")


try:
   password  = input("enter a Password = ")
   check_password(password)

except Exception as e:
   print(e)
   
