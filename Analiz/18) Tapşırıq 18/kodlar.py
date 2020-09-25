# # Tapşırıq 18.
# 
# ## Data əsasında alınma ehtimalı 50%-dən çox olan məhsul kombinasiyalarını bizə bildirin, zəhmət olmasa.

# In[ ]:





# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("esas_mehsullar.csv")
df = data.copy()
df.head()


# In[3]:


# müştəri kodları və aldığı məhsullar

df = df[["satish_kodu","mehsul_ad"]]


# In[4]:


df


# In[5]:


# çatışmayan məlumatlar

df.isnull().sum()


# In[6]:


df = df.dropna()


# In[7]:


df.isnull().sum()


# In[8]:


# məhsulları satış kodlarına görə qruplamaq

items = df.groupby("satish_kodu")["mehsul_ad"].apply(lambda x: ";".join(x))


# In[9]:


items = items.to_frame()


# In[10]:


items.head()


# In[11]:


# məhsulları ayrı ayrılıqda list formatına çevirmək

transactions = list(items["mehsul_ad"].transform(lambda x: x.split(";")))


# In[12]:


transactions[0]


# In[13]:


# məhsulları pivot formatında səbətə çevirmək: hər bir sətirdə(səbətdə) hansı məhsulların olub olmaması

from mlxtend.preprocessing import TransactionEncoder

tr_enc = TransactionEncoder()
basket = pd.DataFrame(tr_enc.fit_transform(transactions), columns=tr_enc.columns_)


# In[14]:


basket


# In[15]:


# səbət analizi üçün lazım olan funksiyalar

from mlxtend.frequent_patterns import apriori,association_rules


# In[16]:


# məhsulların ayrı ayrılıqda və birlikdə səbətlərdə görünmə dərəcəsi

frequent = apriori(basket, min_support=0.00002, low_memory=True, use_colnames = True)
frequent


# In[17]:


# sol tərəfdəki məhsullar alındıqda sağ tərəfdəki məhsulların alınma ehtimalı ən yüksək olan kombinasiyalar (confidence dəyərinə görə) 
association_rules(frequent, metric = "confidence", min_threshold = 0.05).sort_values(by = "confidence",
                                                                                        ascending = False)

