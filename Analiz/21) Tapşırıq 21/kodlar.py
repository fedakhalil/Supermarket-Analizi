# # Tapşırıq 21.

# ## 2019-cu il ərzində aylar üzrə ortalama satışın göstəriciləri neçədir?



# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("esas_mehsullar.csv")
df = data.copy()
df.head()


# In[3]:


df.isnull().sum()


# In[4]:


df.dropna(subset = ["mehsul_ad"], inplace = True)


# In[5]:


df["satish_tarixi"] = df["satish_tarixi"].transform(lambda x: x.replace("T", " "))


# In[6]:


df["satish_tarixi"]


# In[7]:


# satish_tarixi sütununu aylar formatına çevirmək

df["satish_tarixi"] = pd.DatetimeIndex(df["satish_tarixi"]).month_name()


# In[8]:


df["satish_tarixi"].unique()


# In[9]:


aylar = {"January" : "Yanvar", "February" : "Fevral", "March" : "Mart", "April" : "Aprel", "May" : "May",
        "June" : "İyun", "July" : "İyul", "August" : "Avqust", "September" : "Sentyabr",
        "October" : "Oktyabr", "November" : "Noyabr", "December" : "Dekabr"}


# In[10]:


df["satish_tarixi"].replace(aylar, inplace = True)


# In[11]:


df["satish_tarixi"].unique()


# In[12]:


# aylar üzrə ortalama satış məbləği

df.groupby("satish_tarixi")["mehsul_qiymet"].mean()


