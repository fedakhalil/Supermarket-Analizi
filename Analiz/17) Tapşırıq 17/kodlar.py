# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv("esas_mehsullar.csv")
df = data.copy()
df.head()


# In[3]:


# çatışmayan verilənləri silmək

df.dropna(subset=["mehsul_qiymet", "mehsul_ad"],inplace = True)


# In[4]:


# satish_tarixi sütununu tarix tipli dəyişənə çevirmək

df["satish_tarixi"] = df["satish_tarixi"].transform(lambda x: x.replace("T", " ")).astype("datetime64")


# In[5]:


# tarixləri index olaraq qeyd etmək

df.set_index("satish_tarixi", drop = True, inplace = True)


# In[6]:


df


# In[7]:


# saat aralığına aid olan datanı seçmək

gece = df.between_time("23:00", "06:00")


# In[8]:


gece


# In[9]:


# mağazalar üzrə gecə növbəsi satışları

satislar = gece.groupby("magaza_ad")["mehsul_qiymet"].sum().to_frame().reset_index()


# In[10]:


satislar.rename(columns={"mehsul_qiymet" : "umumi_satis"}, inplace=True)
satislar.sort_values(by = "umumi_satis", inplace = True)
satislar


# In[11]:


# keyfiyyətə görə bölmək

labels = ["Pis","Orta","Yaxşı"]
satislar["keyfiyyet"] = pd.qcut(satislar["umumi_satis"],3,labels = labels)


# In[12]:


satislar


# In[14]:


# qrafik


plt.figure(figsize = (12,9))
ax = sns.barplot(x = "umumi_satis", y = "magaza_ad", hue = "keyfiyyet", data = satislar, dodge=False);

plt.title("Gecə növbəsində mağazalar üzrə ümumi satış miqdarı", fontsize = 15, fontweight = "bold", color = "b")

ax.set_ylabel("Mağaza Adı", fontsize = 14, fontweight = "bold", color = "b");
plt.yticks(fontsize = 12, fontweight = "bold", color = "brown");

ax.set_xlabel("Ümumi satış", fontsize = 14, fontweight = "bold", color = "b");
plt.xticks(fontsize = 12, fontweight = "bold", color = "brown");

plt.legend(fontsize = 13, facecolor = "lightgrey");

plt.savefig("qrafik.png", dpi = 100, bbox_inches = "tight")

