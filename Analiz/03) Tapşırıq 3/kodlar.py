
# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("esas_mehsullar.csv")
data = df.copy()
data.head()


# In[3]:


# satish_kodu dəyişənini kateqoriyalı dəyişənə çevirmək


data["satish_kodu"] = data["satish_kodu"].astype("object")


# In[4]:


#  hər market üzrə bir müştərinin ortalama aldığı məhsul sayı

data.groupby("magaza_ad")["satish_kodu"].apply(lambda x: x.value_counts().mean())



