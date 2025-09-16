import pandas as pd 

df = pd.read_json("D:\Code_with_sagar\LIBRARY\PANDAS\howTo_Rows_shows\dummy_data.json",encoding="latin1")
print("displaying the info of data set ")
print((df.info()))