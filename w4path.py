
# coding: utf-8

# In[1]:

get_ipython().magic(u'pwd')


# In[2]:

get_ipython().magic(u'cd C:\\\\Users\\\\Administrator\\\\p162')


# In[3]:

mydir = get_ipython().magic(u'pwd')


# In[4]:

mydir


# In[5]:

import os


# In[6]:

myplantdir=os.path.join(mydir,'lib')


# In[7]:

myplantdir


# In[8]:

get_ipython().magic(u'cd {myplantdir}')


# In[9]:

mydot="C:\\Program Files (x86)\\Graphviz2.38\\bin\\dot.exe"


# In[10]:

mydot


# In[11]:

import glob


# In[12]:

get_ipython().magic(u'cd {myplantdir}')


# In[13]:

glob.glob(r'./*.jar')


# In[14]:

import os
os.environ['GRAPHVIZ_DOT']=mydot
print os.environ['GRAPHVIZ_DOT']
get_ipython().system(u'java -jar {myplantdir}/plantuml.jar -testdot')


# In[15]:

get_ipython().magic(u'install_ext https://raw.githubusercontent.com/sberke/ipython-plantuml/master/plantuml_magics.py')


# In[16]:

get_ipython().magic(u'load_ext plantuml_magics')


# In[17]:

get_ipython().run_cell_magic(u'plantuml', u'', u'@startuml\nstart\n:set how many turns;\n:set how much to grow bigger;\n:set angle;\n:set start size;\nrepeat\nif (i is divided by 2) then\n    :grow bigger;\nendif\n:draw;\nrepeat while(turns)\nstop\n@enduml')


# In[ ]:



