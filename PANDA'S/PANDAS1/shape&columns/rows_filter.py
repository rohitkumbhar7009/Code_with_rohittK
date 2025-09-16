import pandas as pd 

data = {

    "name": ['root','pritish','kiran','digu','pankaj','vyanki','satish','chandu','mahesh','manoj'],
    'age': [25,26,25,24,25,26,25,29,30,25],
    'salary':[20000,50000,40000,300000,700000,80000,500000,45000,78000,98000],
    "performance_Score" : [85,58,78,54,21,10,54,84,86,70]
}

df = pd.DataFrame(data)
# display the dataframe 
print("Sample Dataframe")
print(df)



#rows Filtered 
#find the salary  greater than 50000
filtered_Rows = df[df['salary'] > 50000]
print("employee With Salary > 50000")
print(filtered_Rows)



# multiple conditons 
# find the salary greater than 50000 and age < 25
sal = df[(df["salary"] > 50000)& (df["age"] < 25)]
print("employeee salary > 50000 and age  < 25")
print (sal)

# using or condition 
filterd_or =  df [(df["age"] > 100)  |  (df["performance_Score"] > 80)]
print("filterd OR Age is greater than 25 or performance_Score greater than 90 ")
print(filterd_or) 