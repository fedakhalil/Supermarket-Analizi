# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("esas_mehsullar.csv")
df = data.copy()
df.head()


# In[3]:


# tarixləri ayırmaq


df["satish_tarixi"] = df["satish_tarixi"].transform(lambda x: x.split("T")).transform(lambda x: x[0])


# In[4]:


df["satish_tarixi"]


# In[5]:


# sütunu tarix tipli dəyişənə çevirmək


df["satish_tarixi"] = df["satish_tarixi"].astype("datetime64")


# In[6]:


season = ["Qış", "Qış", "Yaz", "Yaz", "Yaz", "Yay", "Yay", "Yay", "Payız", "Payız", "Payız", "Qış"]


# In[7]:


month_to_season = dict(zip(range(1,13), season))


# In[8]:


month_to_season




# In[9]:


# fəsil adlarından ibarət sütun yaratmaq 

fesiller = df["satish_tarixi"].dt.month.map(month_to_season)


# In[10]:


fesiller


# In[11]:


# fesiller dəyişənini dataya əlavə etmək

df["fesiller"] = fesiller


# In[12]:


df.head()


# In[13]:


df["fesiller"].value_counts()


# In[14]:


# fəsillər üzrə ən çox satılan məhsul kateqoriyası

df.groupby("fesiller")["mehsul_kateqoriya"].apply(lambda x: x.value_counts().nlargest(1))


