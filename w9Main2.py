
# coding: utf-8

# In[21]:

import math
import matplotlib 
import matplotlib.pyplot as plt

def shortDis():
    Locations=[
        (37.575755,126.973553),
        (37.576476,126.985436),
        (37.571573,126.976584),
        (37.574561,126.957753),
        (37.565643,126.966499),
        (37.570171,126.983024)
    ]
    x=Locations[0][0]
    y=Locations[0][1]
    dis=list()
    for i in Locations:
        dis.append (math.sqrt((x-i[0])**2+(y-i[1])**2))
    ag=dis[1]
    ghm=dis[2]
    dlm=dis[3]
    sdm=dis[4]
    jg=dis[5]
    print "Gyeongbokgung from Anguk is %s" %ag
    print "Gyeongbokgung from Gwanghwamun is %s" %ghm
    print "Gyeongbokgung from Dongnimmun is %s" %dlm
    print "Gyeongbokgung from Seodaemun is %s" %sdm
    print "Gyeongbokgung from Jonggak is %s" %jg
    print "Shortest distance is %s "%min(ag,ghm,dlm,sdm,jg)
    
def seoulPopul():
    popul=[
        (74425, 76326),
        (61164, 61636),
        (109688, 115744),
        (144796, 146776),
        (174996, 181676),
        (177841, 177434),
        (204630, 205980),
        (223373, 232245),
        (161055, 166130),
        (171576, 176735),
        (279169, 293772),
        (239450, 251066),
        (148690, 156510),
        (182977, 196992),
        (237792, 242641),
        (283869, 296762),
        (209344, 210282),
        (118965, 114441),
        (186503, 186856),
        (195734, 203014),
        (254381, 249472),
        (212401, 229111),
        (271654, 295354),
        (319197, 335045),
        (229829, 231671)
    ]
    man=list()
    woman=list()
    for i in popul:
        man.append(i[0])
        woman.append(i[1])
    mansum=0
    for i in man:
        mansum+=i
    print "Man's sum is %s" %mansum
    womansum=0
    for i in woman:
        womansum+=i
    print "Woman's sum is %s" %womansum
    print "Man's average is %s" %(mansum/len(man))
    print "Woman's average is %s" %(womansum/len(woman))
    x=list()
    for i in popul:
        x.append(i[0]+i[1])
    plt.bar(range(len(x)),x,align='center')
    plt.show()

def lab9():
    shortDis()
    seoulPopul()

def main():
    lab9()
    
if __name__=="__main__":
    main()

