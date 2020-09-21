# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("esas_mehsullar.csv")
df = data.copy()
df.head()


# In[3]:


# kompot kateqoriyasından ibarət dataset yaratmaq

kompotlar = df[df["mehsul_kateqoriya"] == "Kompotlar"]
kompotlar


# In[4]:


# dataframe-ə çevirmək

new_data = pd.DataFrame(kompotlar[["mehsul_ad", "mehsul_qiymet"]].reset_index(drop = True))


# In[5]:


new_data


# In[6]:


# kompotların qiymətləri

qiymetler = new_data.groupby("mehsul_ad")["mehsul_qiymet"].mean()
qiymetler = pd.DataFrame(qiymetler)
qiymetler


# In[7]:


# kompotların ümumi satış sayı

satis_sayi = new_data.groupby("mehsul_ad").count()
satis_sayi = pd.DataFrame(satis_sayi)
satis_sayi = satis_sayi.rename(columns = {"mehsul_qiymet" : "satis_sayi"})
satis_sayi


# In[8]:


# dataları birləşdirmək

kompotlar = pd.merge(satis_sayi,qiymetler, on = "mehsul_ad")


# In[9]:


kompotlar


# In[10]:


kompotlar.reset_index(inplace=True)
kompotlar




# In[11]:


# excel formatına çevirmək

kompotlar.to_excel("Kompotlar.xlsx")


