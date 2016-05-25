import time
def eidtFile():
    myfile=open('output.txt', 'w')
    line1='first line\n'
    myfile.write(line1)
    line2='\tsecond line\n'
    myfile.write(line2)
    line3='third'
    myfile.write(line3)
    myfile.close()
    msg='[psh edited {0}]'.format(time.strftime('%Y.%m.%d, %H:%M:%S'))
    fin=open('output.txt', 'r')
    fout=open('outputUpper.txt','w')
    for line in fin:
        words=line.split()
        fout.write(msg)
        fout.write('\t')
        for i in words:
            if i == 'line':   
                word=word.upper()
            fout.write(word)
        fout.write('\n')
    fin.close()
    fout.close()
    
def meta():
    data=[1,2,3,4,5,6,7,8,9,10]
    fout=open('number.txt', 'w')
    for i in data:
        str="{0}\t".format(i)
        fout.write(str)
        if i%2==0:
            fout.write('\n')
    fout.close()

def lab12():
    editFile()
    meta()

def main():
    lab12()

if __name__=="__main__":
    main()