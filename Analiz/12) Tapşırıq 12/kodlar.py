# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from warnings import filterwarnings
filterwarnings("ignore")


# In[2]:


data = pd.read_csv("esas_mehsullar.csv")
df = data.copy()
df.head()


# In[3]:


df["magaza_ad"].unique()


# In[4]:


# radiozavod mağazasının datası

df = df[df["magaza_ad"] == "Radiozavod"]
df


# In[5]:


df.isnull().sum()


# In[6]:


# çatışmayan lazımsız verilənləri silmək

df.dropna(subset = ["mehsul_ad","mehsul_qiymet"], inplace = True)


# In[7]:


df.isnull().sum()


# In[8]:


df


# In[9]:


df["satish_kodu"] = df["satish_kodu"].astype("object")


# In[10]:


df = df[["satish_kodu","mehsul_qiymet","satish_tarixi"]]
df


# In[11]:


# müştəri kodlarına görə qruplaşdırmaq

df = df.groupby(["satish_kodu","satish_tarixi"])["mehsul_qiymet"].sum().to_frame()
df.reset_index(inplace = True)


# In[12]:


df


# In[13]:


# 40+ azn alış veriş edən müştərilər

df = df[df["mehsul_qiymet"] >= 40]


# In[14]:


df


# ## tarixi aylara çevirmək

# In[15]:


df["satish_tarixi"] = df["satish_tarixi"].transform(lambda x: x.replace("T", " ")).astype("datetime64")


# In[16]:


df


# In[17]:


aylar = {1: 'Yanvar', 2: 'Fevral', 3: 'Mart', 4: 'Aprel', 5: 'May',
            6: 'İyun', 7: 'İyul', 8: 'Avqust', 9: 'Sentyabr', 10: 'Oktyabr', 11: 'Noyabr', 12: 'Dekabr'}


# In[18]:


aylar


# In[19]:


df.info()


# In[20]:


df["satish_tarixi"] = pd.DatetimeIndex(df["satish_tarixi"]).month


# In[21]:


df


# In[22]:


# aylar üzrə sıralamaq

df.sort_values(by = "satish_tarixi", inplace = True)


# In[23]:


df = df.replace({"satish_tarixi" : aylar})


# In[24]:


df


# In[25]:


df.rename(columns={"satish_kodu" : "musteri_kodu",
                  "satish_tarixi" : "aylar",
                  "mehsul_qiymet" : "hesab"}, inplace = True)


# In[26]:


df


# In[27]:


# aylar üzrə satış sayına görə qruplamaq

ay_sira = df.groupby("aylar", sort = False, as_index=False)["aylar"].size()


# In[28]:


ay_sira


# In[29]:


plt.figure(figsize = (12,6))
ax = sns.barplot(x = "aylar", y = "size", palette="nipy_spectral",saturation=1.75, data = ay_sira);
plt.title("Aylar üzrə 40 AZN üzəri alış veriş edən müştəri sayı", fontsize = 15, fontweight = "bold", color = "brown")
ax.set_xlabel("Aylar", fontsize = 15, fontweight = "bold", color = "grey")
plt.xticks(fontsize = 12, fontweight = "bold", color = "b");
ax.set_ylabel("Müştəri sayı", fontsize = 15, fontweight= "bold", color = "grey")
plt.yticks(fontsize = 12, fontweight = "bold", color = "b");
for i,j in enumerate(ay_sira["size"]):
    ax.text(i-0.2,j, str(j), va = "bottom", fontsize = 14, fontweight = "bold", color = "b")
    
# şəkili saxlamaq

plt.savefig("qrafik", dpi = 80, bbox_inches = "tight")


