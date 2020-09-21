# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("esas_mehsullar.csv")
df = data.copy()
df.head()


# In[3]:


yeni_data = df.groupby("satish_kodu")["mehsul_qiymet"].sum()


# In[5]:


# satis kodu ve edilen odenisler

pd.DataFrame(yeni_data.sort_values(ascending = False)).rename(columns = {"mehsul_qiymet" : "hesab"})


