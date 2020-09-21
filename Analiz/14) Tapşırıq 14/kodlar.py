# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("esas_mehsullar.csv")
df = data.copy()
df.head()


# In[3]:


df["mehsul_kateqoriya"].unique()


# In[4]:


df[df["mehsul_kateqoriya"] == "1"]


# In[5]:


# yanlış olan verilənləri silmək

indexes = df[df["mehsul_kateqoriya"] == "1"].index
df.drop(index = indexes, inplace=True)


# In[6]:


df["mehsul_kateqoriya"].unique()


# In[7]:


print("Mehsul kateqoriya sayı : ", df["mehsul_kateqoriya"].nunique())
print("Mağaza sayı : ", df["magaza_ad"].nunique())


# In[8]:


# hər bir filial üzrə ən çox satılan məhsul

new_df = df.groupby(["magaza_ad","mehsul_kateqoriya"])["mehsul_ad"].apply(lambda x: x.value_counts().nlargest(1))


# In[9]:


# dataframe formatına çevirmək

new_df = new_df.to_frame().reset_index()


# In[10]:


new_df


# In[11]:


new_df.rename(columns={"level_2" : "mehsul_ad", "mehsul_ad" : "satis_sayi"},inplace=True)


# In[12]:


new_df


# In[13]:


# pivot table formatına çevirmək

pivot_df = pd.pivot(new_df,"magaza_ad", "mehsul_kateqoriya", "mehsul_ad")


# In[14]:


pivot_df


# In[15]:


pivot_df.to_excel("Pivot_table.xlsx")

