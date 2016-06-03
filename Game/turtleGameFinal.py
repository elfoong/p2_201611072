import turtle
import random
import math
import time

wn=turtle.Screen()
wn.bgcolor('lightgreen')

t1=turtle.Turtle()
t1.shape('turtle')
t1.pencolor('green')
t1.penup()

score=0
speed=5

print "Eat Foods -> Score up"
print "Eat Traps -> Score down"
print "Higher than 20 score -> End game"
print "Don't eat a Red Food!"
print "-------------------------------------------------------------------------------"

def drawSquare(size, pos):
    t1.pencolor('black')
    t1.setpos(pos)
    t1.pendown()
    for i in range(0,4):
        t1.forward(size)
        t1.right(90)
    t1.penup()    
    t1.home()
    t1.pencolor('green')
    t1.setheading(90)
drawSquare(500,(-250,250))

food=turtle.Turtle()
food.shape('circle')
food.shapesize(1,1,1)
food.penup()
food.setpos(50,50)

trap=turtle.Turtle()
trap.shape('circle')
trap.color('red')
trap.shapesize(1,1,1)
trap.penup()
trap.setpos(-50,-50)

def dontLeave():
    if t1.xcor() > (250.) or t1.xcor() < (-250.):
        print "Don't cross the line!"
        t1.right(180)
        t1.fd(100)
    if t1.ycor() > (250.) or t1.ycor() < (-250.):
        print "Don't cross the line!"
        t1.right(180)
        t1.fd(100)

def reFood():
    d = math.sqrt(math.pow(t1.xcor()-food.xcor(),2) + math.pow(t1.ycor()-food.ycor(),2))
    global score
    if d < 35:
        food.setpos(random.randint(-250,250),random.randint(-250,250))
        score+=1
        print "score up!"
        print "Your score is %d"%score

def reTrap():
    f = math.sqrt(math.pow(t1.xcor()-trap.xcor(),2) + math.pow(t1.ycor()-trap.ycor(),2))
    global score
    if f < 35:
        trap.setpos(random.randint(-250,250),random.randint(-250,250))
        score-=1
        print "score down!"
        print "Your score is %d"%score

def saveScore():
    myscore=open('score.txt', 'a')
    if score>20:
        print "Gteat!"
        name=raw_input("Write your name: ")
        msg='{0}'.format(name +'\t'+ time.strftime('%Y/%m/%d , %H:%M:%S') +'\n')
        print("Your final score is %d")%score
        myscore.write(msg)
        myscore.close()
        print("Click screen -> Close Game")

def turnLeft():
    t1.left(45)
def turnRight():
    t1.right(45)
def keyUp():
    t1.fd(50)
    dontLeave()
    reFood()
    reTrap()
    saveScore()
def turnBack():
    t1.right(180)

turtle.onkey(turnLeft,"Left")
turtle.onkey(turnRight,"Right")
turtle.onkey(keyUp,"Up")
turtle.onkey(turnBack,"Down")
turtle.listen()
wn.exitonclick()
print "Game Start!"