"""
1- How big is your dataset 
2- what are the names of columns

shape and columns 
"""


import pandas as pd 

data = {

    "name": ['root','pritish','kiran','digu','pankaj','vyanki','satish','chandu','mahesh','manoj'],
    'age': [25,26,25,24,25,26,25,29,30,25],
    'salary':[20000,50000,40000,300000,700000,80000,500000,45000,78000,98000],
    "performance Score" : [85,58,78,54,21,10,54,84,86,70]
}

df = pd.DataFrame(data)
print(df)
print(f'Shape :{df.shape} ')
print (f'Column_names: {df.columns}')
