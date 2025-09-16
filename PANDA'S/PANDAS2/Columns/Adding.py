import pandas as pd 

data =  {
    "Name": ['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age": [28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance_Score":[85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
print(df)

#  Adding columns two types (STRAIGHT FORWORD And INSERT)


# STRAIGHT FORWORD
# Adding Columns Bonus with showing 10%  in salary  
df["Bonus"] = df['Salary'] * 0.1
print(df)
 

#INSERT()
# any location add coumns by using index location 
# df.insert(loc,"Column_Name",some_data)
df.insert(0,"Employee ID",[1,2,3,4,5,6,7,8])
print(df) 