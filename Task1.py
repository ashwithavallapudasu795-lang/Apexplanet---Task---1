import pandas as pd
#Load Dataset
df = pd.read_excel("ApexPlanet_DataAnalytics_Dataset (1).xlsx")
#Display first 5 rows
df.head()
#Display dataset shape
df.shape
#Display all column names
df.columns
#Display data types
df.dtypes
#Dataset information
df.info()
#Summary statistics
df.describe()
#Missing values in each column
df.isnull().sum()
#Fill missing Age values with Mean
df["Age"]=df["Age"].fillna(df["Age"].mean())
#Verify missing values are removed
df.isnull().sum()
#Count duplicate rows
duplicates=df.duplicated().sum()
print("Duplicate Rows:",duplicates)
#Convert Order_Date to DateTime format
df["Order_Date"]=pd.to_datetime(df["Order_Date"])
#Final dataset information
df.info()
df.isnull().sum()
#Save cleaned dataset
df.to_excel("Cleaned_Dataset.xlsx", index=False)
print("Cleaned Dataset Saved Successfully!")
