# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv("esas_mehsullar.csv")
df = data.copy()
df.head()


# In[3]:


df.isnull().sum()


# In[4]:


# çatışmayan verilənləri silmək

df.dropna(subset=["mehsul_ad","mehsul_qiymet"], inplace = True)


# In[5]:


df.isnull().sum()


# In[6]:


df["mehsul_kateqoriya"].unique()


# In[7]:


# meyvə şirələri kateqoriyası

meyvesire_df = df[df["mehsul_kateqoriya"] == "Meyvə Şirələri"]


# In[8]:


meyvesire_df


# In[9]:


# VİTA 1000 şirələri datası

vitamin_df = meyvesire_df[meyvesire_df["mehsul_ad"].transform(lambda x: x.str.startswith("VITA 1000")) == True]


# In[10]:


vitamin_df


# In[11]:


# meyvə şirələri kateqoriyası üzrə ümumi satış məbləği

meyvesire_df["mehsul_qiymet"].sum()


# In[12]:


# VİTA 1000 şirələrinin satış məbləği

vitamin_df["mehsul_qiymet"].sum()


# In[19]:


# faizlə göstərmək

print("Cavab: %.2f" % ((vitamin_df["mehsul_qiymet"].sum() * 100) / meyvesire_df["mehsul_qiymet"].sum()), "%")


# In[16]:


# qrafik

labels = "Digər məhsullar", "VİTA 1000 şirələri"
sizes = [meyvesire_df["mehsul_qiymet"].sum(), vitamin_df["mehsul_qiymet"].sum()]
explode = (0,0.2)

fig, ax = plt.subplots(figsize = (10,8))
plt.title("Meyvə şirələri kateqoriyası üzrə satış faizi", {"fontsize" : 18,"fontweight" : "bold", "color" : "b"})

plt.pie(sizes, explode=explode, labels = labels,
        autopct='%1.1f %%', colors = ["r","y"], labeldistance=1.05, startangle = 355,
        textprops={'color':"b","fontsize" : 15, "fontweight":"bold"});

fig.set_facecolor("lightgrey")

plt.savefig("qrafik.png",dpi = 80, facecolor = "lightgrey", bbox_inches = "tight")

