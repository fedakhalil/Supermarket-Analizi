# # Tapşırıq 24.
# 
# ## Keçən il mağazalarımıza mütəmadi çörək təchizatı ilə bağlı problem yaşayırdıq. Bir çox hallarda, müştərilərin çox olan vaxtında artıq çörəklər bitmiş olur, bəzən isə uyğun olmayan vaxtda gətirilən çörəklər növbəti günə qalırdı. Bu il bu problemin yaranmasını istəmirəm, zəhmət olmasa ötən il hər bir filial üzrə 3 saatdan bir neçə çörək satıldığını qrafik və ya cədvəl şəklində hazırlayın.




# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("esas_mehsullar.csv")
df = data.copy()
df.head()


# In[3]:


df["mehsul_kateqoriya"].unique()


# In[4]:


# çörək datasını seçmək

corek_df = df[df["mehsul_kateqoriya"] == "Çörək"].copy()


# In[5]:


corek_df


# In[6]:


# satish_tarixi sütununu saat formatına çevirmək

corek_df["satish_tarixi"] = pd.DatetimeIndex(corek_df["satish_tarixi"]).strftime("%H:%M:%S")


# In[7]:


corek_df


# In[8]:


# tarix formatına çevirmək

corek_df["satish_tarixi"] = corek_df["satish_tarixi"].astype("datetime64")


# In[9]:


corek_df


# In[10]:


# indexi tarix qeyd etmək

corek_df.set_index(corek_df["satish_tarixi"], inplace=True)
corek_df


# In[11]:


# tarixi 3 saat aralığında bölmək

corek_df.resample("3H").size()


# In[12]:


# hər mağaza üzrə 3 saat aralığındakı satış sayı

corek_df.resample("3H")["magaza_ad"].value_counts()


# In[13]:


# dataframe-ə çevirmək

new_df = corek_df.resample("3H")["magaza_ad"].value_counts().to_frame()
new_df


# In[14]:


new_df.rename(columns={"magaza_ad" : "satis_sayi"}, inplace = True)


# In[15]:


new_df


# In[16]:


new_df = new_df.reset_index()
new_df


# In[17]:


# satish_tarixi dəyişənini saatlara çevirmək

new_df["satish_tarixi"] = pd.DatetimeIndex(new_df["satish_tarixi"]).hour


# In[18]:


new_df


# In[19]:


new_df.rename(columns={"satish_tarixi" : "saat"}, inplace=True)
new_df


# In[20]:


# saat dəyişənini saat aralığına çevirmək 

saatlar = {0:"00:00-03:00", 3:"03:00-06:00",6:"06:00-09:00",9:"09:00-12:00",12:"12:00-15:00",
           15:"15:00-18:00",18:"18:00-21:00",21:"21:00-00:00"}

new_df["saat"].replace(saatlar, inplace = True)


# In[21]:


new_df


# In[22]:


# hər mağaza üzrə verilmiş saat aralığındakı çörək satışları

satislar = pd.pivot_table(new_df, "satis_sayi", "saat","magaza_ad",aggfunc="sum")
satislar



# In[21]:


# excel formatında cədvəl ə

satislar.to_excel("corek_satis.xlsx")


