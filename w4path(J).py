
# coding: utf-8

# In[1]:

get_ipython().magic('pwd')


# In[2]:

get_ipython().magic('cd J:')


# In[3]:

get_ipython().magic('pwd')


# In[4]:

get_ipython().magic('cd p162')


# In[5]:

get_ipython().magic('pwd')


# In[6]:

mydir = get_ipython().magic('pwd')


# *  윈도우에선 '\\\'이유는 리눅스에서 다르게인식

# In[7]:

mydir


# In[8]:

import os


# In[9]:

myplantdir=os.path.join(mydir,'lib')


# In[10]:

myplantdir


# In[11]:

get_ipython().magic('cd {myplantdir}')


# In[22]:

mydot="C:\\Program Files\\Graphviz2.38\\bin\\dot.exe"


# In[23]:

mydot


# In[14]:

import glob


# In[15]:

get_ipython().magic('cd {myplantdir}')


# In[16]:

glob.glob(r'./*.jar')


# In[25]:

import os
os.environ['GRAPHVIZ_DOT']=mydot
print os.environ['GRAPHVIZ_DOT']
get_ipython().system('java -jar {myplantdir}/plantuml.jar -testdot')


# C:\Program Files\Graphviz2.38\bin\dot.exe
