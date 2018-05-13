
# coding: utf-8

# In[66]:


#AUTHOR: Brendan Legel
#Goal: Scrap Fox News
#Purpose: Creation of an LSTM 



# # Import

# In[67]:


import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup


# # Functions 

# In[151]:


#FUNCTIONS AREA
def MakeFile(make, take):
    nameIt = make
    nameItFull = nameIt+".txt"
    file = open(nameItFull,"w") 
    file.write(take)
    file.close()
    print("file made -> ", nameItFull)
    return(nameItFull)

def Reader(file):
    fileCheck = open(file, "r")
    output = fileCheck.read()
    #print(output)
    print("read")
    return output

def MinerStart(site, target):
    if "www." in site:
        start = (site.index("www.")) + 4
    if ".com" in site:
        end = (site.index(".com"))
    title = site[start:end] + "home"
    r = requests.get(site, auth=('user','pass'))
    out = r.text
    print("Stage 1: Miner Complete")
    NameItFull = MakeFile(title,out)
    print("Stage 2: Raw Mineral Repository Complete")
    return NameItFull

def StageData(RepositoryText):
    PreprocessStage1 = Reader(RepositoryText)
    print("Staging Complete")
    return PreprocessStage1
    
def ProcessTargets(Data):
    indexQ = []
    for i in range(len(a)):
        if a[i] == '"':
            indexQ.append(i)
    totalQ = int(len(indexQ)/2)
    Info = [] 
    for i in range(totalQ):
        start = indexQ.pop(0) +1
        end = indexQ.pop(0)
        Q = a[start:end]
        Info.append(Q)
    todaysArticleLinks = []
    count = 0 
    for i in range(len(Info)):
        if "article story" in Info[i]:
            #print(Info[i+1])
            articleLink = Info[i+2]
            articleDescription = Info[i + 11]
            if "/v/" not in articleLink and "//video" not in articleLink and "info" not in articleLink:
                todaysArticleLinks.append(articleLink)
    return todaysArticleLinks
#END 

def MinerGo(site, target):
    print("will do ")


# # RUN AREA

# Miner

# In[153]:


#TARGET
site = "http://www.foxnews.com/"
#FIRST PULL & DROP OFF
location = MinerStart(site,target)


# Stager

# In[154]:


#Read Repository Text
a = StageData(location)
#Re-evaluation Stage ( Aiming at what I wanted )


# In[155]:


#Look through starting page of fox news for todays articles ... find the links 
mytargetslist = ProcessTargets(a)
#I found them -> mytargetslist

