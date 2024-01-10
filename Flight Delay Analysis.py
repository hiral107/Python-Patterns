#!/usr/bin/env python
# coding: utf-8

# # Import Liberaries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.offline import iplot
import plotly as py
import plotly.tools as tls
import cufflinks as cf
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


py.offline.init_notebook_mode(connected = True)
cf.go_offline()


# In[3]:


#To display all the columns of Dataframes
pd.pandas.set_option("display.max_columns", None)


# In[4]:


pip install openpyxl


# # Load Dataset

# In[5]:


traindf = pd.read_excel(r"C:\Users\Z5070\Downloads\Data_Train.xlsx", engine = "openpyxl")
traindf.head(2)


# In[6]:


traindf.shape


# In[7]:


testdf = pd.read_excel(r"C:\Users\Z5070\Downloads\Test_set.xlsx", engine = "openpyxl")
testdf.head(2)


# In[8]:


testdf.shape


# In[9]:


#Other Method to load multiple dataset
#traindf = pd.read_excel(r"C:\Users\Z5070\Downloads\Data_Train.xlsx")
#testdf = pd.read_excel(r"C:\Users\Z5070\Downloads\Test_set.xlsx")


# # View Dataset

# In[10]:


traindf.head(2)


# In[11]:


testdf.head(2)


# # Dataset Rows and Columns count

# In[12]:


rows, cols = traindf.shape
print(f"There are {rows} rows and {cols} columns in Train dataset.")


# In[13]:


rows, cols = testdf.shape
print(f"There are {rows} rows and {cols} columns in Test dataset.")


# # Merge Two datasets

# In[14]:


finaldf = traindf._append(testdf)
finaldf.head()


# # Two Dataset Rows and Columns count

# In[15]:


rows, cols = finaldf.shape
print(f"There are {rows} rows and {cols} columns in Merged dataset.")


# # Missing Values/ Null Values

# In[16]:


finaldf.isnull().sum()


# # Duplicate values

# In[17]:


duplicate = finaldf.duplicated().sum()
print(f"Total {duplicate} duplicate values are there in this dataset.")


# # Date Split

# In[18]:


finaldf["Date_of_Journey"].str.split("/").str[0]


# In[19]:


finaldf["Date"] = finaldf["Date_of_Journey"].str.split("/").str[0]
finaldf["Month"] = finaldf["Date_of_Journey"].str.split("/").str[1]
finaldf["Year"] = finaldf["Date_of_Journey"].str.split("/").str[2]


# # Dataset infomation

# In[20]:


finaldf.info()


# In[21]:


#Change datatype of date, month and year
finaldf["Date"] = finaldf["Date"].astype(int)
finaldf["Month"] = finaldf["Month"].astype(int)
finaldf["Year"] = finaldf["Year"].astype(int)


# In[22]:


finaldf.info()


# # Drop duplicate column

# In[23]:


finaldf.drop("Date_of_Journey", axis = 1, inplace = True)


# # Split Time

# In[24]:


finaldf["Arrival_Time"].str.split(" ").str[0]


# In[25]:


finaldf["Arrival_Time"] = finaldf["Arrival_Time"].apply(lambda x: x.split(" ")[0])


# In[26]:


finaldf["Arrival_Hour"] = finaldf["Arrival_Time"].str.split(":").str[0]
finaldf["Arrival_Min"] = finaldf["Arrival_Time"].str.split(":").str[1]


# In[27]:


finaldf.head(2)


# In[28]:


finaldf["Arrival_Hour"] = finaldf["Arrival_Hour"].astype(int)
finaldf["Arrival_Min"] = finaldf["Arrival_Min"].astype(int)


# In[29]:


finaldf.drop("Arrival_Time", axis = 1, inplace = True)


# In[30]:


finaldf.head(2)


# In[31]:


#Find Unique values

finaldf["Total_Stops"].unique()


# In[32]:


finaldf["Total_Stops"] = finaldf["Total_Stops"].map({"non-stop":0, "1 stop": 1, "2 stops": 2, "3 stops": 3, "4 stops": 4, "nan": 1})


# In[33]:


finaldf[finaldf["Total_Stops"].isnull()]


# In[34]:


finaldf["Airline"].unique()


# # Import sklearn library

# In[35]:


from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()


# In[36]:


finaldf["Duration_Hr"] = finaldf["Duration"].str.split(" ").str[0].str.split("h").str[0]


# In[37]:


finaldf[finaldf["Duration_Hr"] == "5m"]


# In[38]:


finaldf.drop(6474, axis = 0, inplace = True)
finaldf.drop(2660, axis = 0, inplace = True)


# In[39]:


finaldf.head(2)


# In[40]:


finaldf["Duration_Hr"] = finaldf["Duration_Hr"].astype("int")


# In[41]:


finaldf.drop("Duration", axis = 1, inplace = True)


# In[42]:


finaldf.head(2)


# In[43]:


finaldf["Airline"] = labelencoder.fit_transform(finaldf["Airline"])
finaldf["Source"] = labelencoder.fit_transform(finaldf["Source"])
finaldf["Destination"] = labelencoder.fit_transform(finaldf["Destination"])
finaldf["Additional_Info"] = labelencoder.fit_transform(finaldf["Additional_Info"])


# In[44]:


rows, cols =  finaldf.shape
print(f"There are {rows} rows and {cols} columns in this dataset.")


# In[45]:


finaldf.head(2)


# In[47]:


finaldf["Price"] = finaldf["Price"].fillna(finaldf["Price"].mean())


# In[48]:


finaldf.info()


# In[49]:


finaldf.drop("Route", axis = 1, inplace = True)


# In[50]:


finaldf.info()


# # Data Visualization

# # Chart 1 - Box Plot (Price of Source)

# In[51]:


plt.figure(figsize = (12, 8))
sns.catplot(y = "Price", x = "Source", data = finaldf.sort_values("Price", ascending = True), kind = "box", height = 6, aspect = 3)


# # Chart 2 - Box plot (Price of Airline)

# In[52]:


plt.figure(figsize = (12, 12))
sns.catplot(y = "Price", x = "Airline", data = finaldf.sort_values("Price", ascending = True), kind = "box", height = 6, aspect = 3)


# # Chart 3  - Bar Plot (Price of Total Stops)

# In[54]:


plt.figure(figsize = (12, 12))
sns.catplot(y = "Price", x = "Total_Stops", data = finaldf.sort_values("Price", ascending = False), kind = "bar", height = 6, aspect = 3)


# In[58]:


plt.figure(figsize = (12, 8))
sns.catplot(y = "Price", x = "Total_Stops", data = finaldf, kind = "bar")


# In[ ]:




