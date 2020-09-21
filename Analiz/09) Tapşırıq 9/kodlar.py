# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv("esas_mehsullar.csv")
df = data.copy()
df.head()


# In[3]:


df["endirim_kompaniya"].unique()


# In[4]:


# novruz endirim kompaniyasına aid olan sətirlər

novruz = df[df["endirim_kompaniya"] == "Bərəkətli Novruz"]


# In[5]:


novruz


# In[6]:


novruz["mehsul_kateqoriya"].value_counts()


# In[7]:


# qrafiklə göstərmək

a = novruz["mehsul_kateqoriya"].value_counts().values
b = novruz["mehsul_kateqoriya"].value_counts().index


plt.figure(figsize = (11,7))
ax = sns.barplot(x = a[:5], y = b[:5]);
plt.title("Novruz endirimində ən çox satılan top 5 məhsul kateqoriyası", fontsize = 14, fontweight = "bold")
plt.xticks(fontsize = 12, fontweight = "bold", color = "b")
plt.xlabel("Satış sayı", fontsize = 15, fontweight = "bold", color = "b")
plt.yticks(fontsize = 14, fontweight = "bold", color = "r")
for i, v in enumerate(a[:5]):
    ax.text(v + 0.5, i + .05, str(v), color='blue', va = "bottom", fontweight='bold')

plt.savefig("Kateqoriyalar.png", dpi = 80, bbox_inches = "tight")




# In[8]:


# ən çox satılan məhsul kateqoriyasını ayırmaq

sirniyyat = novruz[novruz["mehsul_kateqoriya"] == "Şirniyyat"]


# In[9]:


sirniyyat["magaza_ad"].value_counts()


# In[12]:


# qrafiklə göstərmək

x = sirniyyat["magaza_ad"].value_counts().values
y = sirniyyat["magaza_ad"].value_counts().index

plt.figure(figsize = (11,8))
plt.title("Şirniyyat məhsullarının filiallar üzrə satışı", fontsize = 15, fontweight = "bold")
plt.xticks(fontsize = 13, fontweight = "bold", color = "b")
plt.xlabel("Satış sayı", fontsize = 15, fontweight = "bold", color = "b")
plt.yticks(fontsize = 13, fontweight = "bold", color = "r")
ax = sns.barplot(x = x, y = y, estimator=sum, palette="viridis");
for i, v in enumerate(x):
    ax.text(v + 3, i + .1, str(v), color='blue', fontweight='bold')

plt.savefig("Magazalar.png", dpi = 90, bbox_inches = "tight")


