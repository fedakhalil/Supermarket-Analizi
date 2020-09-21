# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv("esas_mehsullar.csv")
df = data.copy()
df.head()


# In[3]:


# qiymət və bonus kart sütunu

df = df[["mehsul_qiymet","bonus_kart"]]


# In[4]:


df


# In[5]:


df.isnull().sum()


# In[6]:


# çatışmayan verilənləri silmək

df.dropna(inplace = True)


# In[7]:


df


# In[8]:


df["bonus_kart"] = df["bonus_kart"].astype("object")


# In[9]:


df.info()


# In[10]:


df = pd.get_dummies(df)


# In[11]:


df


# In[12]:


df.rename(columns = {"bonus_kart_False" : "False", "bonus_kart_True" : "True"}, inplace = True)


# In[13]:


df


# In[14]:


# məhsul qiymətləri ilə bonus kartlar arasındakı korrelyasiya

df.corr()




# In[15]:


# korrelyasiya qrafiki

plt.figure(figsize = (8,6))
plt.xticks(fontsize = 15, color = "r", fontweight = "bold")
plt.yticks(fontsize = 15, color = "r", fontweight = "bold")
sns.heatmap(df.corr(),cmap = "YlGnBu");




# ## Nəticə: Zəif korrelyasiya


