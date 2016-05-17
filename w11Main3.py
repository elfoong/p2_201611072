import turtle
import math
wn=turtle.Screen()
t1=turtle.Turtle()
wn.bgpic("C:\Users\Administrator\Desktop\myMaze.gif")

def keyup():
    curpos=t1.pos()
    t1.forward(45)
    isInRectangle(curpos,coord)
    isOnLine(curpos,pos1,pos2)
    isInCircle(curpos,radious,circlepos)
def keydown():
    curpos=t1.pos()
    t1.back(45)
    isInRectangle(curpos,coord)
    isOnLine(curpos,pos1,pos2)
    isInCircle(curpos,radious,circlepos)
def keyright():
    t1.right(45)
def keyleft():
    t1.left(45)
def mousegoto(x,y):
    t1.setpos(x,y)
    curpos=t1.pos()
    isInRectangle(curpos,coord)
    isOnLine(curpos,pos1,pos2)
    isInCircle(curpos,radious,circlepos)
    
def addkeys():
    wn.onkey(keyup, "Up")
    wn.onkey(keydown, "Down")
    wn.onkey(keyright, "Right")
    wn.onkey(keyleft, "Left")
    wn.onkey(wn.bye, "q")
def addmouse():
    wn.onclick(mousegoto)

coord=[(100,100),(200,200)]
x1=coord[0][0]
x2=coord[1][0]
y1=coord[0][1]
y2=coord[1][1]

line1=[(50,300),(150,300)]
x1=line1[0][0]-5
y1=line1[0][1]-5
x2=line1[1][0]+5
y2=line1[1][1]+5
pos1=(x1,y1)
pos2=(x2,y2)

cirpos=((0,100)

def drawRectangle():
    t1.penup()
    t1.goto(100,100)
    t1.pendown()
    t1.setheading(0)
    for i in range(0,4):
        t1.fd(100)
        t1.left(90)
    t1.penup()

def drawRedRectangle():
    t1.penup()
    t1.goto(100,100)
    t1.pendown()
    t1.pencolor("red")
    t1.setheading(0)
    for i in range(0,4):
        t1.fd(100)
        t1.left(90)
    t1.penup()

def drawLine():
    t1.penup()
    t1.goto(50,300)
    t1.pendown()
    t1.setheading(0)
    t1.fd(100)
    t1.penup()

def drawRedLine():
    t1.penup()
    t1.goto(50,300)
    t1.pendown()
    t1.pencolor("red")
    t1.setheading(0)
    t1.fd(100)
    t1.penup()

def drawCircle():
    t1.penup()
    t1.home()
    t1.pendown()
    t1.setheading(0)
    t1.circle(100)
    t1.penup()

def drawRedCircle():
    t1.penup()
    t1.home()
    t1.pendown()
    t1.pencolor("red")
    t1.setheading(0)
    t1.circle(100)
    t1.penup()

def isInRectangle(curpos,coord):
    if xs<=curpos[0]<=xe and ys<=curpos[1]<=ye:
        drawRedRectangle()

def isOnLine(curpos,pos1,pos2):
    if x1<=curpos[0]<=x2 and y1<=curpos[1]<=y2:
        drawRedLine()

def isinCircle(curpos,cirpos):
    if math.sqrt(math.pow(curpos[0]-cirpos[0],2) + math.pow(curpos[1]-cirpos[1],2))<=100:
        drawRedCircle()

def drawBackground():
    drawRectangle()
    drawLine()
    drawCircle()

drawBackground
t1.home()

addkeys()
addmouse()
wn.listen()