#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn import preprocessing
import numpy as np
import seaborn as sns
from sklearn.linear_model import LinearRegression, Lasso
import datetime
from statistics import mean


# In[8]:


data= pd.read_csv("forestfires.csv")


# In[9]:


data


# In[5]:


data.shape


# # MISSING VALUES

# In[7]:


data.isnull()


# In[8]:


data.info()


# In[9]:


data.describe()


# In[10]:


data.isnull().sum()


# In[11]:


data.isnull().sum().sum()


# data.head()

# # remove outliers 'x'

# In[15]:


sns.displot(data['X'])


# In[17]:


sns.boxplot(data['X'])


# In[18]:


data['X'].mean()


# In[19]:


df=data[data['X']<10]


# In[20]:


df['X'].mean()


# In[21]:


df.shape


# In[22]:


df.boxplot()


# In[23]:


df.hist()


# # remove outlier "Y"

# In[24]:


sns.displot(data['Y'])


# In[25]:


sns.boxplot(data['Y'])


# In[26]:


data['Y'].mean()


# In[27]:


df=data[data['Y']<10]


# In[28]:


df['Y'].mean()


# In[29]:


df.shape


# In[30]:


df.boxplot()


# In[31]:


df.hist()


# In[ ]:





# In[11]:





# In[ ]:





# In[ ]:




