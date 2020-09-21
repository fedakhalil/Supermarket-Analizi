# Tapşırıq 19.

## Endirim kampaniyaları çərçivəsində hansı məhsul kateqoriyası liderlik edib? Zəhmət olmasa, hər bir kampaniya üçün ayrılıqda olmaqla məsələni həll edin


# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("esas_mehsullar.csv")
df = data.copy()
df.head()


# In[3]:


df["endirim_kompaniya"].unique()


# In[4]:


df["endirim_kompaniya"] = df["endirim_kompaniya"].transform(lambda x: x.replace("S?rf?li Yaz", "Sərfəli Yaz"))


# In[5]:


df["endirim_kompaniya"].unique()


# In[6]:


# hər bir endirim kompaniyası üzrə ən çox satılan məhsul kateqoriyası

kateqoriya = df.groupby("endirim_kompaniya")["mehsul_kateqoriya"].apply(lambda x: x.value_counts().nlargest(1)).to_frame()


# In[7]:


kateqoriya


# In[8]:


kateqoriya.reset_index().rename(columns={"level_1" : "mehsul_kateqoriya", "mehsul_kateqoriya" : "satish_sayi"})


