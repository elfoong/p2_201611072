
# coding: utf-8

# In[13]:

def leapyear():
    year=input("user input year: ")
    if (year%4 == 0) and (year%100 !=0 or year%400==0):
        res="This year is leap year"
    else:
        res="This year is not leap year"
    print res


# In[14]:

leapyear()


# In[15]:

def lab6():
    leapyear()


# In[16]:

def main():
    lab6()


# In[17]:

if __name__=="__main__":
    main()

