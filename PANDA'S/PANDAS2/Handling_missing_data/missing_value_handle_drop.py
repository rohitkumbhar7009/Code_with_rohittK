# 1 removing and 2 is fill the value
#dropna()----> remove the row  missing value 
# syntax - df.dropna(axis = 0, inplace = True ) 
# axis = 0 --->means rows missing value drop 
# axis = 1 ---> means column missing value drop 

import pandas as pd 

data =  {
    "Name": ['Ram',None,'Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age": [28,None,22,30,29,40,25,32],
    "Salary":[50000,None,45000,52000,49000,70000,48000,58000],
    "Performance_Score":[85,None,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
print(df)



# df.dropna( inplace = True )
print("after removing value ")
print(df)

# # row missing data drop 
df.dropna(axis = 0, inplace = True )
print("row data missing drop")
print(df)

# column data missing  drop
df.dropna(axis = 1, inplace = True )
print("column data missing drop")
print(df)




