
# coding: utf-8

# In[2]:

import turtle
t1=turtle.Turtle()
def drawSquareAtSave(size, pos):
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    tracks=list()
    for i in range(0,4):
        tracks.append(t1.pos())
        t1.forward(size)
        t1.right(90)
    return tracks
def lab7b():
    mytrack=drawSquareAtSave(200,(-100,0))
    print mytrack
def main():
    lab7b()


# In[ ]:



