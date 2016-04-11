
# coding: utf-8

# In[29]:

def sumList(aList):
    x=list()
    for i in range(0,aList):
        if (i%4==0 and i%5!=0):
            x.append(i)
    sum=0
    for s in range(0,len(x)):
        sum+=x[s]
    mysum=sum
    return mysum


# In[30]:

def lab6():
    """aList 값에 따라 계산값이 달라진다"""
    aList=1001
    labsum=sumList(aList)
    print labsum


# In[31]:

def main():
    lab6()


# In[32]:

if __name__=="__main__":
        main()

