
# coding: utf-8

# In[ ]:

import turtle


# In[ ]:

wn=turtle.Screen()


# In[ ]:

t1=turtle.Turtle()


# In[ ]:

def drawMaze(size,bigger,sides):
    for i in range(0,sides):
        if(i%2):
            size=size+bigger
            t1.fd(size)
            t1.right(90)


# In[ ]:

drawMaze(20,10,50)


# In[ ]:

wn.exitonclick()

