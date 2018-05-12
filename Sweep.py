
# coding: utf-8

# In[12]:


# raw info sweeper 
import requests
from bs4 import BeautifulSoup
site = "http://www.foxnews.com/"
target = "trump"
def sweep(site, target):
    r = requests.get(site, auth=('user','pass'))
    out = r.text
    return out

    


# In[13]:


sweep(site,target)

