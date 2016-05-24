import os
mydir=os.getcwd()
def readFile():
    filename='python.txt'
    myfilename=os.path.join(mydir,filename)
    myfile=open(myfilename,'r')
    try:
        myfile=open(myfilename,'r')
        contents=myfile.readlines()
        for line in range(0,len(contents)):
            if contents[i].find('Python')>=0:
                print contents[i]
        myfile.close()
    except IOError as e:
        print e
        
def writeFile():
    myfile=open('output.txt','w')
    line1='first line\n'
    myfile.write(line1)
    line2='\tsecond line\n'
    myfile.write(line2)
    line3='third'
    myfile.write(line3)
    myfile.close()
    myfile=open('output.txt','r') 
    contents=myfile.readlines() 
    for i in range(0,len(contents)):
        if contents[i].find('line')>=0:
            res=contents[i].split()
        for i in range(0,len(res)):
            if res[i].find('line')>=0:
                print res[i].upper() 
    myfile2.close()
    
def lab13():
    readFile()
    writeFile()

def main():
    lab13()
    
if __name__=="__main__":
    main()