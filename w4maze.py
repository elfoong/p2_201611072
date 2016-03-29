
# coding: utf-8

# In[1]:

import turtle


# In[2]:

wn=turtle.Screen()


# In[3]:

t1=turtle.Turtle()


# In[5]:

def drawMaze(size,bigger,sides):
    for i in range(0,sides):
        if(i%2):
            size=size+bigger
            t1.fd(size)
            t1.right(90)


# In[6]:

drawMaze(20,10,50)


# In[7]:

wn.exitonclick()

