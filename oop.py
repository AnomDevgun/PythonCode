class Square():

    #CLASS OBJECT ATTRIBUTE
    #SAME FOR ANY INSTANCE OF THE CLASS
    sides = 4

    def __init__(self,par1,par2):
        self.par1=par1
        self.par2=par2
    
    def area(self):
        return(self.par1*self.par2)

class Circle():

    #class object attribute
    pi=3.14

    def __init__(self,radius=1):
        self.radius = radius

    #METHOD
    def get_circum(self):
        return self.radius*self.pi*2

mySquare = Square(2,3)
print(mySquare.area())
print(f"A square always has {mySquare.sides} sides")

myCircle = Circle(2)
print(myCircle.pi)
print(myCircle.radius)
print(myCircle.get_circum())





#Methods are functions defined in the body of a class and perform ops that use attributes of the object through use of self keyword.
#attributes dont need paranthesis, they are not being executed, just accessed.