
# coding: utf-8

# In[1]:

def highlow():
    selnum=raw_input('user select number(1-300): ')
    tryc=0
    num=-1
    while (selnum!=num):
        num=raw_input('Guess the number!: ')
        if (selnum>num):
            print "Up"
        elif (selnum<num):
             print "Down"
        tryc=tryc+1
    print ("You win at %s try!"%tryc)


# In[2]:

highlow()


# In[3]:

def lab6():
    highlow()


# In[4]:

def main():
    lab6()


# In[5]:

if __name__=="__main__":
    main()

