
# coding: utf-8

# In[4]:

def charCount(word):
    sentence='sangmyung university'
    sentence.split()
    list(sentence)
    allchars=list(sentence)
    d=dict()
    for c in allchars:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
def drawGraph():    
    import matplotlib
    import matplotlib.pyplot as plt
    
    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()

def lab8():
    global word
    word="sangmyung university"
    charCount(word)
    drawGraph()
    
def main():
    lab8()
    
if __name__=="__main__":
    main()


# In[ ]:



