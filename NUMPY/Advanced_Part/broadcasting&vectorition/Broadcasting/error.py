"""
3- Incompatable shapes-  

"""

import numpy as np


arr1= np.array([[1,2,3],[4,5,6]])  

arr2 =  np.array([1,2])

result =  arr1 + arr2 

print(result)


#showing Error -- ValueError

# Traceback (most recent call last):
#   File "e:\python\Python,Pandas,Numpy\LIBRARY\NUMPY\Advanced_Part\Broadcasting&Vectorization\error.py", line 13, in <module>
#     result =  arr1 + arr2
#               ~~~~~^~~~~~
# ValueError: operands could not be broadcast together with shapes (2,3) (2,)