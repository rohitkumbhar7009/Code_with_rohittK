import pandas as pd



data = {
    "Name" :['Arun','varun','karun','Narun','Marun'],
    "Age" :[28,34,22,34,28],
    "Salary" :[50000, 60000, 45000, 52000, 48000]
 }


df = pd.DataFrame(data)
print(df)



grouped = df.groupby("Age")["Salary"].sum()

print(grouped)