# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("esas_mehsullar.csv")
df = data.copy()
df.head()


# In[3]:


df["endirim_kompaniya"].unique()


# In[4]:


#  '?' işarəsini 'ə' hərfi ilə əvəzləmək


df["endirim_kompaniya"] = df["endirim_kompaniya"].transform(lambda x: x.replace("S?rf?li Yaz", "Sərfəli Yaz"))


# In[5]:


df["endirim_kompaniya"].unique()


