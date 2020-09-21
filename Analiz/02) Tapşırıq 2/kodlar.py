# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("esas_mehsullar.csv")
data = df.copy()
data.head()


# In[3]:


# çatışmayan məlumatların cəmi

data.isnull().sum()




# # endirim kompaniya sütunu

# In[4]:


# boş olan sütun və sətirlər

data[data["endirim_kompaniya"].isnull()]


# In[5]:


# boş olan dəyərləri "kompaniya yoxdur" sözü ilə əvəzləmək

data["endirim_kompaniya"].fillna("Kompaniya yoxdur", inplace = True)


# In[6]:


data.head(10)


# In[7]:


data.isnull().sum()


# In[ ]:





# # mehsul_ad və mehsul_qiymet sütunu

# In[8]:


# boş olan sütun və sətirlər

data[data[["mehsul_ad","mehsul_qiymet"]].isna().any(axis = 1)]


# In[ ]:





# ## Birinci metod

# In[9]:


# boş olan bütün verilənləri datadan silmək

data = data.dropna()


# In[10]:


data.isnull().sum()


# In[11]:


data.info()


# In[12]:


# indexləri sıfırlamaq

data.reset_index(drop=True, inplace=True)


# In[13]:


data.info()


# In[14]:


data.index


# In[ ]:




# ## İkinci metod

# In[16]:


data = df.copy()
data.isnull().sum()


# In[17]:


data["endirim_kompaniya"].fillna("Kompaniya yoxdur", inplace=True)


# In[18]:


data.isnull().sum()


# In[ ]:





# In[19]:


# boş olan sütun və sətirlər

data[data[["mehsul_ad", "mehsul_qiymet"]].isnull().any(axis = 1)]


# In[20]:


# boş olan məhsul adlarını həmin sətirdəki məhsul kateqoriyası ilə əvəzləmək

data["mehsul_ad"].fillna(data["mehsul_kateqoriya"], inplace=True)


# In[21]:


data.isnull().sum()


# In[22]:


# boş olan məhsul qiymətləri

data[data["mehsul_qiymet"].isnull()].head()


# In[ ]:





# In[23]:


# boş olan məhsul qiymətlərini həmin sətirdəki məhsul kateqoriyasının ortalama və ya median dəyərləri ilə doldurmaq 

data["mehsul_qiymet"].fillna((data.groupby("mehsul_kateqoriya")["mehsul_qiymet"].transform("median")), inplace = True)


# In[24]:


data.isnull().sum()

