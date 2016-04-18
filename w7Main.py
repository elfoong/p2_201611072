
# coding: utf-8

# In[1]:

import turtle
wn=turtle.Screen()
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

def drawSquareFrom(tracks):
    tracks=dict()
    tracks=({0:(-150,150),1:(150,150),2:(150,-150),3:(-150,-150),4:(-150,150)})
    t1.up()
    t1.setpos(tracks[0])
    t1.down()
    for i in range(0,5):    
        t1.goto(tracks[i])
    
def lab7b():
    mytrack=drawSquareAtSave(200,(-100,100))
    print mytrack
    
def lab7c():
    mytracks=drawSquareFrom(0)
    print mytracks
    
def main():
    lab7b()
    lab7c()

main()
wn.exitonclick()

