import pandas as pd 


data = {

    "name": ['kiran','vyanki','pritish'],
    'Age': [10,20,30],
    "city":["kop","Nag","Nanded"]
}

df =pd.DataFrame(data)

print ("displaying the onfo of data set")
print(df.info())