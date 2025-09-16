"""
.revel() -> views
.flatten() -> copy
"""


import numpy as np 

arr2d = np.array([[10,20,30],
                [40,50,60]])




print(arr2d.ravel())

print(arr2d.flatten())