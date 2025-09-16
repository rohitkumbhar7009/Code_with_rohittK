import pandas as pd 

data =  {
    "Name": ['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age": [28,34,22,30,29,40,25,32],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance_Score":[85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)
print(df)

#  .loc[]

# syntax
# df.loc[row_index, "Column_name"] = new_value


# update the Ram Salary 55000
df.loc[0,'Salary'] = 55000
print(df)

# update the  first name ram = ganesh
df.loc[0,"Name"] = "Ganesh"
print(df)



# Show original data types
print("Before update:\n", df.dtypes)


# Update Salary of Ram to a float value (e.g. 55000.75)
df.loc[0, 'Salary'] = 55000.75
# Check updated dataframe and data types
print("\nAfter salary update:\n", df)
print("\nData types after salary update:\n", df.dtypes)





