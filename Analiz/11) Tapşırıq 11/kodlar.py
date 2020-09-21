# Tapşırıq 11.

## Bu sevindiricidir ki, müştərilərimizin əksəriyyəti bonus kartdan istifadə edir, lakin bəzi marketlərimizdə bonus kartla alış–veriş edənlərin sayı azdır. Bütün marketlərimiz üzrə il ərzində bonus kartla satış sayını və mağaza adlarını bir cədvəldə hazırlayın. Bonus kartla satış sayını azdan çoxa sıralayın ki, az olan marketlərimizdə bonus karta cəlb edən reklam lövhələri asaq.



# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("esas_mehsullar.csv")
df = data.copy()
df.head()


# In[3]:


# yalnız bonus kartla alış veriş edilmiş müştərilər

df[df["bonus_kart"] == True]


# In[4]:


bonus_sayi = df["magaza_ad"].value_counts().to_frame()


# In[5]:


# bütün mağazalar üzrə bonus kartla olan satış sıralaması

bonus_sayi = bonus_sayi.rename(columns = {"magaza_ad" : "satish_sayi"}).sort_values(by = "satish_sayi")
bonus_sayi


