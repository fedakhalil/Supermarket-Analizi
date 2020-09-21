# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("esas_mehsullar.csv").copy()
data.head()


# In[3]:

# bizə lazım olan dəyişənləri seçirik

data = data[["satish_kodu", "bonus_kart"]].copy()
data.head()


# In[4]:


data.info()


# In[5]:


data.isnull().sum()


# In[6]:


data["satish_kodu"] = data["satish_kodu"].astype("object")


# In[7]:


data.head()


# In[ ]:


# üç və daha çox məhsul alanları filter edirik

df = data.groupby("satish_kodu")["satish_kodu"].count() >= 3


# In[ ]:


df


# In[10]:


# yalnız True olanları filter edirik

ucden_boyuk = df[df]
ucden_boyuk


# In[12]:


# True olan satış kodlarından yeni dataframe yaradırıq 

df = pd.DataFrame(ucden_boyuk.index)


# In[13]:


df


# In[14]:


# satış kodlarına görə bonus kartlarını qruplayırıq

bonus = data.groupby("satish_kodu")["bonus_kart"].mean()


# In[15]:


# satış kodları ilə bonus kartlarını birləşdiririk

last_data = pd.merge(df,bonus,on="satish_kodu")


# In[16]:


last_data


# In[17]:


last_data[last_data["bonus_kart"] == True]


# In[18]:


# bonus_kart True olanların ümumi bonus kart sayına nisbətini tapırıq

print("Nəticə = %.2f" % ((34867 * 100) / 70016), "%")

