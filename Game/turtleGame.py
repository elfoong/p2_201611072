print "Move your turtle and gain points"
print "If your score is higher than 10 points, You win!"
print "Your score is 0 points"
import turtle
wn=turtle.Screen()
wn.bgcolor("Lightgreen")
t1=turtle.Turtle()
t2=turtle.Turtle()
t1.shape('turtle')
t1.penup()
t2.penup()
t2.speed(5)
t1.goto(0,-80)
t1.left(90)
t1.pos()
mypos=t1.pos()
point=0
def background():
    t2.setpos(-400,300)
    t2.setheading(0)
    t2.pendown()
    for i in range(0,2):
        t2.fd(800)
        t2.right(90)
       	t2.fd(600)
       	t2.right(90)
    t2.penup()
def drawTriangle():
    t2.setpos(-320,-250)
    t2.setheading(0)
    t2.pendown()
    t2.pencolor('red')
    for i in range(0,3):
        t2.fd(220)
        t2.left(120)
    t2.penup()
def drawOctagon():
    t2.setpos(160,-250)
    t2.setheading(0)
    t2.pendown()
    t2.pencolor('blue')
    for i in range(0,5):
        t2.fd(125)
        t2.left(72)
    t2.penup()
def drawStar():
    t2.setpos(0,250)
    t2.setheading(-108)
    t2.pendown()
    t2.pencolor('yellow')
    for i in range(0,5):
        t2.fd(250)
        t2.left(144)
    t2.penup()
def dotPoints():
    t2.pencolor('black')
    t2.setheading(0)
    t2.goto(-210,-180)
    t2.shape('circle')
    t2.dot()
    t2.write("    1 point")
    t2.goto(0,120)
    t2.dot()
    t2.write("    3 points")
    t2.goto(225,-160)
    t2.dot()
    t2.write("    2 points")
    t2.hideturtle()
def play():
    background()
    drawTriangle()
    drawOctagon()
    drawStar()
    dotPoints()
play()
x=float()
y=float() 
def up():
    t1.fd(20)
    (x,y)=t1.pos() 
    global point
    if (-220<=x<=-200) and (-190<=y<=-170):
        point+=1
	print "You get 1 point!"
        print "Your score is %d points" % point
        t1.goto(mypos)
    if (215<=x<=235) and (-170<=y<=-150):
        point+=2
	print "you get 2 points!"
        print "Your score is %d points" % point
        t1.goto(mypos)
    if (-10<=x<=10) and (110<=y<=130):
        point+=3
	print "you get 3 points!"
        print "Your score is %d points" % point
        t1.goto(mypos)
    if (point>=10):
        print "You Win!"
        input("Press any key or Click screen: ")    
def down():
    t1.bk(20)
def left():
    t1.left(30)
def right():
    t1.right(30)
wn.listen()
wn.onkey(up, "Up")
wn.onkey(down, "Down")
wn.onkey(left, "Left")
wn.onkey(right, "Right")
wn.exitonclick()