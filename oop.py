class Square():
    def __init__(self,par1,par2):
        self.par1=par1
        self.par2=par2
    
    def area(self):
        return(self.par1*self.par2)


mySquare = Square(2,3)
print(mySquare.area())