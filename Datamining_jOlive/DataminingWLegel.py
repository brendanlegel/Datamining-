
# coding: utf-8

# In[45]:


"hello world"
import random


# In[10]:


def qmefag():
    print("fag")
    x=5
    return x


# In[11]:


qmefag()


# In[51]:


def ifblind(x):
    if x == 0:
        #print("blind")
        return "blind"
    else:
        #print("fucked")
        return "fucked"


# In[52]:


ifblind(100)


# In[53]:


ifblind(0)


# In[54]:


def checkblind(a):
    temp = 0
    for i in range(len(a)):
        if ifblind(a[i]) == "fucked":
            temp = temp + 1
    return temp


# In[55]:


a = [0,1,1,1,1,1,1,1,0]


# In[56]:


print(checkblind(a))


# In[64]:


def generator():
    listofA = []
    for i in range(1000):
        a = random.random()*10
        if a < 5:
            a = 0
        else:
            a = 1
        listofA.append(a)
    return listofA


# In[65]:


checkblind(generator())


# In[67]:


total = []
for i in range(100000):
    total.append(checkblind(generator()))
a = 0
for i in range(len(total)):
    a = total[i] + a
print(a/len(total))
    


# In[68]:


#i know scan reddit
def scan():


# In[4]:



import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup


# In[5]:


def makefile(make, take):
    nameIt = make
    nameItFull = nameIt+".txt"
    file = open(nameItFull,"w") 
    file.write(take)
    file.close()
    print("complete")

def reader(file):
    fileCheck = open(file, "r")
    output = fileCheck.read()
    return output


# In[6]:


site = "https://www.reddit.com/r/CryptoCurrency/"
site2 = "https://www.cnn.com/"
target = "trump"
def sweep(site, target):
    pageFile = urlopen(site)
    pageHtml = str(pageFile.read())
    print(pageHtml)
    pageFile.close()
    makefile("reddit",pageHtml)
    #soup = BeautifulSoup("".join(pageHtml))

    #sAll = soup.findAll("li")
    #sAll = soup.findAll("a")
    #for href in sAll:
     #   print (href)


# In[7]:


#write
sweep(site, target)


# In[40]:


site = "https://www.reddit.com/r/CryptoCurrency/"
site2 = "https://www.cnn.com/"
target = "trump"
def bsweep(site2, target):
    pageFile = urlopen(site2)
    pageHtml = str(pageFile.read())
    #print(pageHtml)
    pageFile.close()
    titlecount = 0
    spot = [] 
    for i in (range(len(pageHtml)-5)):
        first = pageHtml[i]
        second = pageHtml[i+1]
        third = pageHtml[i+2]
        fourth = pageHtml[i+3]
        fifth = pageHtml[i+4]
        finalstr = first + second + third + fourth+ fifth
        if finalstr == "title":
            #print("found")
            spot.append(i)
            titlecount = titlecount + 1 
    print(titlecount)
    print(spot)
            
    for j in range(len(spot)):
        a = int(spot[j])
        
        print(pageHtml[a:a+35])
    #soup = BeautifulSoup("".join(pageHtml))
    #sAll = soup.findAll("<title>")
    #sAll = soup.findAll("li")
    #for href in sAll:
    #    print (href)
    #makefile("cnntitles",sAll)


# In[41]:


#need to proces the scan 
bsweep(site2, target)


# In[70]:


#make regression


# In[71]:


#all here

