"""
np.insert(array, index , value , axis = None)

array = original  array 
index = position number 
value = actual data 
axis =  0 , means row  wise data ko axis krna hai , 
        1. means column wise axis krna hai 
"""



import numpy as np 

arr = np.array([10,20,30,40,50,60])
print(arr)

new_arr  =  np.insert(arr,-2,110,axis=0)

print(new_arr)