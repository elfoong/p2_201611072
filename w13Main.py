
# coding: utf-8

# In[ ]:

import turtle
t1=turtle.Turtle()
wn=turtle.Screen()

def appendFile():
    try:
        fin1=open('python.txt', 'a')
        fin2=open('outputNumber.txt', 'r')
        for line in fin2:
            fin1.write(line)
        fin1.close()
        fin2.close()
    except Exception as e:
        print e

def writeReccoords():
    frec=open('reccoords.txt','w')
    frec.write('0,0,100,100'+'\n')
    frec.write('200,200,150,150')
    frec.close()

def getCoordsFromFile(aFile):
    frec=open(aFile)
    mycoords=[]
    for line in frec:
        line1=line.split(',')
        mycoords.append([(line1[0],line1[1]),(line1[2],line1[3].strip())])
    return mycoords
    frec.close()

def drawSquareWithCoords(coords):
    for coord in coords:
        x1=int(coord[0][0])
        x2=int(coord[1][0])
        y1=int(coord[0][1])
        y2=int(coord[1][1])
        t1.penup()
        t1.goto(x1,y1)
        t1.pendown()
        t1.goto(x2,y1)
        t1.goto(x2,y2)
        t1.goto(x1,y2)
        t1.goto(x1,y1)

def lab13():
    appendFile()
    writeReccoords()
    getCoordsFromFile('reccoords.txt')
    aFile=getCoordsFromFile('reccoords.txt')
    drawSquareWithCoords(aFile)
    
def main():
    lab13()
    wn.exitonclick()

if __name__=="__main__":
        main()


# In[ ]:



