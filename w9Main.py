import matplotlib
import matplotlib.pyplot as plt

def charCount(word):
    d=dict()
    word='sangmyung university'
    for c in word:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()

def countDigitsLetters(word):
    d=dict()
    d={"number":0, "word":0}
    for c in word:
        if c.isdigit()==True:
            d["number"]+=1
        elif c.isdigit()==False:
            d["word"]+=1
    plt.bar(range(0,len(d)),d.values(), align='center')
    plt.xticks(range(0,len(d)),list(d.keys()))
    plt.show()

def compareFurniture():
    mh=set()
    fh=set()
    mh={'TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder'}
    fh={'coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder'}
    print "Furniture in my home is ",mh
    print "Furniture in friend's home is ",fh
    print "Furniture only in my home is ",mh.difference(fh)
    print "Furniture only in friend's home is ",fh.difference(mh)
    print "Furniture both we have is ",mh.intersection(fh)
    print "Furniture all things we have is ",mh.union(fh)
    d=dict()
    for c in mh:
       if c not in d:
          d[c]=1
       else:
          d[c]+=1
    for c in fh:
       if c not in d:
          d[c]=1
       else:
          d[c]+=1
    print "A number of furniture is ",d

def lab9_5():
    word='sangmyung university'
    charCount(word)

def lab9_6():
    word='7 hongjidong'
    countDigitsLetters(word)

def lab9_7():
    compareFurniture()

def main():
    lab9_5()
    lab9_6()
    lab9_7()

if __name__=="__main__":
    main()