# A summary of description  statistics of numerical columns in a dataframe 


# step1   sample data frame 

import pandas as pd 

data = {

    "name": ['root','pritish','kiran','digu','pankaj','vyanki','satish','chandu','mahesh','manoj'],
    'age': [25,26,25,24,25,26,25,29,30,25],
    'salary':[20000,50000,40000,300000,700000,80000,500000,45000,78000,98000],
    "performance Score" : [85,58,78,54,21,10,54,84,86,70]
}

df = pd.DataFrame(data)
print("Sample Dataframe")
print(df)


print("Descriptive Statistics")
print (df.describe())