
# coding: utf-8

# In[10]:

def leapyear():
    year=input("user input year: ")
    if (year%4 == 0) and (year%100 !=0 or year%400==0):
        res="This year is leap year"
    else:
        res="This year is not leap year"
    print res


# In[11]:

def highlow():
    import random
    selrange=raw_input('user select range(1~n): ')
    n=int(selrange)
    num=random.randint(1,n)
    print "range is 1~%s"%n
    trycount=0
    gs=0
    while (num!=gs):
        gs=int(input('Guess the number!: '))
        if (num>gs):
            print "Up"
        elif (num<gs):
            print "Down"
        trycount+=1
    print ("You win at %s tries!"%trycount)


# In[12]:

def lab6():
    leapyear()
    highlow()


# In[13]:

def main():
    lab6()


# In[14]:

if __name__=="__main__":
    main()

