
# coding: utf-8

# In[1]:

def Multiplus():
    sum=0
    for i in range(0,1000):
        if i%3==0 or i%5==0:
            sum=sum+i
    print sum


# In[2]:

Multiplus()

