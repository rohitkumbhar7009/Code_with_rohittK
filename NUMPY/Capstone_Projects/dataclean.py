import pandas as pd 
import numpy as np 


#dataset loading 


df = pd.read_csv('employees.csv')
print(df)


#checking the missing value 
print("missing value in Each column")
print(df.isnull().sum())


df.fillna(0, inplace=True)
print("Missing value in Each column after fillna:")
print(df.isnull().sum())




df.replace([np.inf, -np.inf], np.nan, inplace=True )



#remove duplicates records 
df.drop_duplicates(inplace=True)