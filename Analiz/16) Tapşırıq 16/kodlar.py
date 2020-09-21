# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("esas_mehsullar.csv")
df = data.copy()
df.head()


# In[3]:


df.info()


# In[4]:


# satish_tarixi sütununu tarix tipli dəyişənə çevirmək

df["satish_tarixi"] = df["satish_tarixi"].transform(lambda x: x.replace("T", " ")).astype("datetime64")


# In[5]:


df["satish_tarixi"]


# In[6]:


# günlərdən ibarət sütun yaratmaq

df["gun"] = pd.DatetimeIndex(df["satish_tarixi"]).day_name()


# In[7]:


df


# In[8]:


# yazı dilini dəyişmək

gunler = {"Monday" : "Bazar ertəsi", "Tuesday" : "Çərşənbə axşamı", "Wednesday" : "Çərşənbə",
         "Thursday" : "Cümə axşamı", "Friday" : "Cümə", "Saturday" : "Şənbə", "Sunday" : "Bazar"}


# In[9]:


df["gun"].replace(gunler, inplace = True)


# In[10]:


df


# In[12]:


df["gun"].unique()

