# fillna() ---> missing data fill 
# fillna(value,inplace = True)  --customized value drop 


import pandas as pd 

data =  {
    "Name": ['Ram',None,'Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age": [28,None,22,30,29,40,25,32],
    "Salary":[50000,None,45000,52000,49000,70000,48000,58000],
    "Performance_Score":[85,None,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
print(df)


# default value place
# df.fillna(0,inplace=True)
# print("default value place ")  
# print(df)

# calculated value place 
df["Age"].fillna(df['Age'].mean(),inplace=True)
df["Salary"].fillna(df['Salary'].mean(),inplace=True)
df["Performance_Score"].fillna(df['Performance_Score'].mean(),inplace=True)



print("calculated value place ")
print(df)