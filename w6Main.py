
# coding: utf-8

# In[23]:

def RSP():
    userA=raw_input('userA input "Rock Scissors Paper" : ')
    userB=raw_input('userB input "Rock Scissors Paper" : ')
    if userA==userB: 
        print "draw"
    elif userA=='Scissors':
        if userB=='Rock':
            print "B win"
        else:
            print "A win"
    elif userA=='Rock':
        if userB=='Papper':
            print "B win"
        else:
            print "A win"
    else:
        if userB=='Scissors':
            print "B win"
        else:
            print "A win"


# In[25]:

RSP()


# In[26]:

RSP()


# In[27]:

RSP()


# In[28]:

RSP()


# In[29]:

RSP()


# In[30]:

RSP()


# In[31]:

RSP()


# In[32]:

RSP()


# In[33]:

RSP()

