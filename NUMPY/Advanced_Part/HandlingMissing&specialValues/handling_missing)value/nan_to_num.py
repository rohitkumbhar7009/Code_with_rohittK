"""
nan value ko replace krna hai 

solution - np.nan_to_num(array, nan=value)  default Value = 0
 
"""


import numpy as np 

arr = np.array([1,2,np.nan,4,5,np.nan,7,8,9])



#default value 
# cleaned_arr = np.nan_to_num(arr)
# print(cleaned_arr)
#ans-> [1. 2. 0. 4. 5. 0. 7. 8. 9.] 

cleaned_arr = np.nan_to_num(arr, nan=5)
print(cleaned_arr)
#ans-> [1. 2. 5. 4. 5. 5. 7. 8. 9.] 