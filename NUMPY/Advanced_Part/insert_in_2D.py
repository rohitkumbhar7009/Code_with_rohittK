import numpy as np 

arr_2d = np.array([[1,2], [3,4]])
print(arr_2d)

#insert a new row at index 1 

new_arr_2d = np.insert(arr_2d, 0,  [5,6], axis=None)

print("new 2d array ",new_arr_2d)