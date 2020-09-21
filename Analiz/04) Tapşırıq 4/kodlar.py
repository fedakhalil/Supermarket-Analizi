# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv("esas_mehsullar.csv")
df = data.copy()
df.head()


# In[3]:


# satish_tarixi sütununu səliqəyə salmaq və tarix tipli dəyişənə çevirmək

df["satish_tarixi"] = df["satish_tarixi"].transform(lambda x: x.replace("T"," ")).astype("datetime64")


# In[4]:


df.head()


# In[5]:


print("Minimum tarix: ",df["satish_tarixi"].min())
print("Maximum tarix: ",df["satish_tarixi"].max())



# In[6]:


# ən çox satılan 10 məhsul


top_10 = df["mehsul_ad"].value_counts().nlargest(10)
top_10


# In[7]:


# qrafiklə göstərmək

plt.figure(figsize = (7,7))
plt.xlabel("Satış Sayı", fontsize = 16, color = "purple")
plt.ylabel("Məhsul Adı", fontsize = 16, color = "purple")
plt.title("İl ərzində ən çox satılan top 10 məhsul və satış sayı",fontweight="bold")
top_10.sort_values(ascending = True).plot.barh(color = "red", fontsize = 13);
