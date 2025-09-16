"""
concatenation means vertically or horizontaly  combines data 

vertically(row-wise)
horizontally (column-wise)

syntax - 

pd.concate([df1,df2],axis = 0,ignore_index = True)


[df1,df2]= 
axis = 0 (0 means row wise 1 means column wise )

"""
# vertically 

import pandas as pd 

df_Region1 = pd.DataFrame({
    "CustomerID":[1,2],
    "Name":['Gopal','Raju']

})

df_Region2 = pd.DataFrame({
    "CustomerID":[3,4],
    "Name":['shyam','babu']

})

df_Region=pd.concat([df_Region1,df_Region2],axis=1,ignore_index=True)
print(df_Region)
