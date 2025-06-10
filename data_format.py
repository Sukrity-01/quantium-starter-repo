
import pandas as pd
import numpy as np
import glob as glob

csv_files=glob.glob("data/*.csv")
combined_data=pd.DataFrame()
for file in csv_files:
    df=pd.read_csv(file)
    df['date']=pd.to_datetime(df['date'])
    df=df[df['product']=='pink morsel']
    df['price']=df['price'].str.replace('$','',regex=False).astype(float)
    df['sales']=df['price']*df['quantity']
    df=df[['sales','date','region']]
    combined_data=pd.concat([combined_data,df], ignore_index=True)
combined_data.to_csv('formatted_sales_data.csv',index=False)
print(combined_data)
print("Formatted sales data created successfully")
