# # Tapşırıq 22.
 
# ## Bonus kartı olan və olmayan müştərilər üzrə ortalama satış miqdarı neçədir?




# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("esas_mehsullar.csv")
df = data.copy()
df.head()




# In[3]:


df = df.dropna(subset = ["mehsul_qiymet"])


# In[4]:


df["satish_kodu"]


# ## Bonus kartı olanlar

# In[5]:


bonus_true = df[df["bonus_kart"] == True]


# In[6]:


# bonus kartı olan müştərilər üzrə ortalama satış miqdarı

bonus_true.groupby("satish_kodu")["mehsul_qiymet"].mean()


# In[7]:





# ## Bonus kartı olmayanlar

# In[8]:


bonus_false = df[df["bonus_kart"] == False]


# In[9]:


# bonus kartı olmayan müştərilər üzrə ortalama satış miqdarı

bonus_false.groupby("satish_kodu")["mehsul_qiymet"].mean()

