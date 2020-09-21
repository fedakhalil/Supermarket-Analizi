# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv("esas_mehsullar.csv")
df = data.copy()
df.head()


# In[3]:


df["satish_kodu"] = df["satish_kodu"].astype("object")


# In[4]:


df["endirim_kompaniya"] = df["endirim_kompaniya"].transform(lambda x: x.replace("S?rf?li Yaz", "Sərfəli Yaz"))


# In[5]:


# çatısmayan verilənlər

df.isnull().sum()


# In[6]:


# çatışmayan lazımsız verilənləri silmək

df.dropna(subset=["mehsul_ad", "mehsul_qiymet"], inplace = True)


# In[7]:


df.isnull().sum()


# In[8]:


# kompaniyalar üzrə müştəri sayı

say = df.groupby("endirim_kompaniya")["satish_kodu"].apply(lambda x: x.count()).sort_values()
say = pd.DataFrame(say)
say





# In[9]:


# kompaniyalar üzrə ümumi gəlir

gelir = df.groupby("endirim_kompaniya")["mehsul_qiymet"].apply(lambda x: x.sum()).sort_values()
gelir = pd.DataFrame(gelir)
gelir


# In[10]:


# dataları birləşdirmək

data2 = pd.merge(say,gelir, on = "endirim_kompaniya")
data2


# In[11]:


# data üzərində düzəlişlər

data2.rename(columns={"satish_kodu" : "musteri_sayi",
                     "mehsul_qiymet" : "umumi_gelir"}, inplace = True)
data2.reset_index(inplace = True)
data2


# In[12]:


# qrafiklə göstərmək

ax = data2.plot(y = ["musteri_sayi","umumi_gelir"], x = "endirim_kompaniya", kind = "barh", 
           figsize = (9,6),
           color = ["b","r"]);
plt.legend(["Müştəri sayı", "Ümumi gəlir"], fontsize = 14)
plt.ylabel("Kompaniya adı", fontsize = 15);
ax.set_facecolor('grey') 
plt.yticks(fontsize = 12, fontweight = "bold")
plt.xticks(fontsize = 10, fontweight = "bold")
plt.title("Endirim kompaniyalarının gəlirlilik sıralaması", fontsize = 15, fontweight = "bold");
plt.savefig('qrafik.png', dpi = 100, bbox_inches = 'tight')


