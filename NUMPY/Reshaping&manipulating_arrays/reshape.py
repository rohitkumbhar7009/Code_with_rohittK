"""
reshape(rows, columns)  specify new shape 

if dimensions match 

note- reshaping does not create copy its return view 

"""

import numpy as np 

arr = np.array([10,20,30,40,50,60])


reshaper_Arr =  arr.reshape(2,3)

print(reshaper_Arr)