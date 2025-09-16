import pandas as pd 

data = {

    "name": ['root','pritish','kiran','digu','pankaj','vyanki','satish','chandu','mahesh','manoj'],
    'age': [25,26,25,24,25,26,25,29,30,25],
    'salary':[20000,50000,40000,300000,700000,80000,500000,45000,78000,98000],
    "performance Score" : [85,58,78,54,21,10,54,84,86,70]
}

df = pd.DataFrame(data)
# display the dataframe 
print("Sample Dataframe")
print(df)

print("Names (single column return series)") #column name case sensitivity 
#print(df["name"])  
name = df['name']  #create object 
print (name)




#selecting multiple columns 
subset = df[["name","age","salary"]]
print('\n subset with Name ,Age And Salary')
print(subset)




