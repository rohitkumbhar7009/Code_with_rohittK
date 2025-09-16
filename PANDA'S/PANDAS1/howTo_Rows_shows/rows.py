# two methods  
# 1 - head() , tail()
# head(n) - first n rows display
# head() - by default 5 rows display 

# tail()- show last rows 
# tail(n) - show last 5 rows display 


import pandas as pd 

df = pd.read_json("D:\\Code_with_sagar\\LIBRARY\PANDAS\\howTo_Rows_shows\\dummy_data.json",encoding="latin1")
print(" default first 5 rows shows")
print (df.head())

print("display rows of first")
print (df.head(1))




print("difault last 5 rows show")
print (df.tail())


print(" last 5 rows show")
print (df.tail(4))
