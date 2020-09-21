# Tapşrıq 21.
 
## Ümumi il ərzində üzrə ən çox satış hansı mağazada reallaşıb?



# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("esas_mehsullar.csv")
df = data.copy()
df.head()


# In[3]:


df.isnull().sum()


# In[4]:


df.dropna(subset= ["mehsul_ad","mehsul_qiymet"], inplace = True)


# In[5]:


df.isnull().sum()


# ## Müştəri sayına görə ən çox satış edilən mağaza

# In[6]:


# mağazalar üzrə satış sayı

satis_sayi = df.groupby("magaza_ad").size().sort_values(ascending = False)
satis_sayi


# In[7]:


# ən çox müştəri ziyarəti edilən mağaza

satis_sayi.nlargest(1)




# ## Ümumi məbləğə görə ən çox satış edilən mağaza

# In[8]:


df.head()


# In[9]:


# mağazalar üzrə ümumi gəlir sıralaması

umumi_gelir = df.groupby("magaza_ad")["mehsul_qiymet"].sum().sort_values(ascending = False)
umumi_gelir


# In[10]:


# ən çox gəlir əldə edilən mağaza

umumi_gelir.nlargest(1)


