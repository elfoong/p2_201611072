
# coding: utf-8

# In[1]:

def mark():
    marks =input('input your marks: ')
    print "marks: %s" %marks
    if (90<= marks <=100):
        print "grade A"
    elif (80<= marks <90):
        print "grade B"
    elif (70<= marks <80):
        print "grade C"
    elif (60<= marks <70):
        print "grade D"
    else:
        print "grade F"
mark()

