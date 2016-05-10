def milkPercent():
    allData=list()
    allData=[
        ["Coffee","Water","Milk","Icecream"],
        ["Espresso","No","No","No"],
        ["Long Black","Yes","No","No"],
        ["Flat White","No","Yes","No"],
        ["Cappuccino","No","Yes - Frothy","No"],
        ["Affogato","No","No","Yes"]
    ]
    data=allData[1:]
    percent=0
    for i in data:
        if i[2]=="No":
            percent=percent
        else:
            print i[0]
            percent+=1
    pro=(percent*100./len(data))
    print "Rate of milk-used coffee is %s percent"%pro

def sumAverage():
    marks=list()
    marks=[
        ["English", 100],
        ["Math", 200],
        ["English", 200],
        ["Math", 200],
        ["English", 100],
        ["Math", 300],
    ]
    english=list()
    math=list()
    for i in marks:
        if i[0].upper()=="ENGLISH":
            english.append(i[1])
        else:
            math.append(i[1])
    ensum=0
    masum=0
    for en in english:
        ensum+=en
    for ma in math:
        masum+=ma
    en=float(ensum)
    ma=float(masum)
    enaver=en/len(english)
    maaver=ma/len(math)
    print "English sum is %s"%en
    print "Math sum is %s"%ma
    print "English average is %s"%enaver
    print "Math average is %s"%maaver

def greatestWord():
    lyrics=list()
    lyrics=[
    "when I find myself in times of trouble",
    "mother Mary comes to me",
    "speaking words of wisdom let it be",
    "and in my hour of darkness",
    "she is standing right in front of me",
    "speaking words of wisdom let it be",
    "let it be let it be",
    "let it be let it be",
    "whisper words of wisdom let it be",
    "and when the broken-hearted people",
    "living in the world agree",
    "there will be an answer let it be",
    "for though they may be parted",
    "there is still a chance that they will see",
    "there will be an answer let it be",
    "let it be let it be",
    "let it be let it be",
    "yeah there will be an answer let it be",
    "let it be let it be",
    "let it be let it be",
    "whisper words of wisdom let it be",
    "let it be let it be",
    "ah let it be yeah let it be",
    "whisper words of wisdom let it be",
    "and when the night is cloudy",
    "there is still a light that shines on me",
    "shine on until tomorrow let it be",
    "I wake up to the sound of music",
    "mother Mary comes to me",
    "speaking words of wisdom let it be",
    "let it be let it be",
    "let it be yeah let it be",
    "oh there will be an answer let it be",
    "let it be let it be",
    "let it be yeah let it be",
    "whisper words of wisdom let it be"
    ]
    doc=lyrics
    d=dict()
    for line in doc:
        words=line.split()
        for c in words:
            if c not in d:
                d[c]=1
            else:
                d[c]+=1
    for i in d:
        if d[i]>20:
            print i,d[i]
    print "The greatest number of words is be "

def lab10():
    milkPercent()
    sumAverage()
    greatestWord()

def main():
    lab10()
    
if __name__=="__main__":
    main()