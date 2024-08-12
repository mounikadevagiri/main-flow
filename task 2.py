#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
data = pd.read_csv('C:\\Users\devag\Downloads\\01.Data Cleaning and Preprocessing.csv')
type(data)


# In[13]:


data.info #consice summary


# In[8]:


data.describe() #descriptive statistics


# In[9]:


data = data.drop_duplicates()
data


# In[10]:


data.isnull()


# In[11]:


data.isnull().sum()


# In[12]:


data.notnull()


# In[14]:


data.isnull().sum().sum()


# In[47]:


data2 = data.fillna(value=0)
data 


# In[46]:


data2.isnull().sum().sum()


# In[17]:


data


# In[18]:


#filling null values with the previous values
data3 = data.fillna(method='pad')
data3


# In[19]:


#filling null values with the next value
data4 = data.fillna(method='bfill')
data4


# In[33]:


import numpy as np
from scipy import stats


# In[48]:


#detect the outliers using IQR
data2.columns


# In[49]:


data2.drop(['Observation'], axis=1, inplace=True)
data2.columns


# In[51]:


Q1= data2.quantile(0.25)
Q3= data2.quantile(0.75)
IQR=Q3-Q1
print(IQR)


# In[52]:


data2=data2[~((data2<(Q1-1.5*IQR))|(data2>(Q3+1.5*IQR))).any(axis=1)]
data2


# In[53]:


data2.describe()


# In[ ]:




