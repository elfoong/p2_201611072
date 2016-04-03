
# coding: utf-8

# In[1]:

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


# In[2]:

RSP()

