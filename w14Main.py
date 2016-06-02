class Dog(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        print "my dog's name is",self.name
    def talk(self):
        print "mung mung"
        
class ShihtzuDog(object):
    def talk(self):
        print "si si"
        
class MalteseDog(object):
    def talk(self):
        print "mal mal"

def dogSound():
    mydog=Dog(Dog)
    mydog.talk()
    myshitzu=ShihtzuDog()
    myshitzu.talk()
    mymaltese=MalteseDog()
    mymaltese.talk()
    
def lab14():
    dogSound()

def main():
    lab14()
    raw_input()
    
if __name__=="__main__":
    main()