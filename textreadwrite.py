
# coding: utf-8

# In[17]:


def makefile(make, take):
    nameIt = str(input("name it please"))
    nameItFull = nameIt+".txt"
    file = open(nameItFull,"w") 
    file.write(take)
    print("complete")

def reader(file):
    fileCheck = open(file, "r")
    output = fileCheck.read()
    return output

