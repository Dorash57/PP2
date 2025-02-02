class String:
    def getString(self):
        self.sentence=input("Sentense:")
    def printString(self):
        print("With upper case:"+self.sentence.upper())
        
mystring=String()
mystring.getString()
mystring.printString()
