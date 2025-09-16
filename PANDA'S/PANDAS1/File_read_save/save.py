import pandas as pd 

data = {
    'Name' : ['ram','shyam','ghanshyam'],
    'Age': [10,20,30],
    'City':["kop","pune","mumbai"]
}


df = pd.DataFrame(data)
print(df)

# save in csv file 
#df.to_csv("output.csv",index=False)



# save in exel file 
#df.to_excel("output.xlsx",index=False)

# save in json file 
#df.to_json("output.json",index=False)

