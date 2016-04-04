
# coding: utf-8

# In[1]:

def bmi():
    weight=input ("Input your wieght(kg): ")
    height=input ("Input your height(m): ")
    print "your weight is %s kg"%weight,"and your height is %s m"%height
    bmi=weight/height/height
    print "your bmi is %s"%bmi
    if bmi < 18.5:
        res ="underweight"
    elif bmi >= 18.5 and bmi <25:
        res ="normal weight"
    elif bmi >= 25 and bmi <30:
        res ="overweight"
    else:
        res ="obesity"
    return res
    print res


# In[2]:

bmi()

