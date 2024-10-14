from graphics import *
from tk import *

# def main():
#     win = GraphWin('My Circle', 1500,1500) # My circle ger titel och 1000x1000 ger storlek
#     c = Circle(Point(150,150), 90)
#     c.draw(win)
#     p =Circle(Point(500,500), 50)
#     p.draw(win)
#     p.move(50,40)
#     c.setFill('turquoise')
#     p.setFill('turquoise')
#     a = Text(Point(200,200), 'Hello!')
#     a.draw(win)
#     h = c.clone()
#     h.move(100,100)
#     h.setFill('white')
#     h.draw(win)
#     win.getMouse()
#     win.close()

# main()

# def main1():

#     def chess():
#         class Square:
#             def __init__(sq, lenght, height, colour):
#             sq.lenght = lenght

                
#     win = GraphWin('Chessboard',800,800)

# BILLLL

def car():

    win = GraphWin('Cargame', 640,480, autoflush=False)
    win.setCoords(-320,-240,320,240) #Gör att (0,0) är i mitten

    class Racer:
        def __init__(self,win):
            self.circle = Circle(Point(0,0),10)
            self.circle.setFill('pink')
            self.circle.draw(win)

            self.xvelocity = 0
            self.yvelocity = 0

    racer = Racer(win)
            
    
    xvelocity = 0
    yvelocity = 0

    speedLimit = 20


    while True:
        
        key = win.checkKey()
        if key == 'Up':
            yvelocity +=1
        elif key == 'Down':
            yvelocity -= 1
        elif key == 'Right':
            xvelocity =+1
        elif key == 'Left':
            xvelocity-=1
        elif key == 'space':
            xvelocity*=0.6
            yvelocity*=0.6
        elif key == 'BackSpace':
            circle.move(-circle.getCenter().getX(), -circle.getCenter().getY())
            xvelocity = 0
            yvelocity = 0
        
        yvelocity = min(speedLimit, yvelocity)
        yvelocity = max(-speedLimit, yvelocity)
        xvelocity = min(speedLimit, xvelocity)
        xvelocity = max(-speedLimit, xvelocity)


        

        circle.move(xvelocity,yvelocity)
        update(10)

    animationSpeed = 50

    win.getMouse()
    win.close()


car()

class Person: # Skapar en klass (istället för def för funktioner)
    def __init__(self,firstName, lastName): #init används för att kunna skapa konstruerare, self är endast ett alias
        self.fName = firstName
        self.lName = lastName
        self.spouse = None # i konstruktorn

        #Ändra namn med hjälp av metod:
        def setFirstName(self, name):
            Person.fName = name

# Efter konstrueraren läggs metoderna till
    def getFirstName(self):
        return self.fName

    def getFullName(self):
        return self.fName +' '+ self.lName # Hade också kunnat skriva return getFirstName +
    
    def isMarried(self):
        return self.spouse is not None
    
    def getSpouse(self): #Enkel gettermetod
        return self.spouse

    def marry(self, other):
        if (self.isMarried()) or other.isMarried():
            return False
        if (self == other):
            return False
        self.spouse = other # other är också ett objekt i person
        other.spouse = self #Refererar till varandra
        return True



#prototyp:

# p1 = Person('Moa', 'Pettersson')
# p2 = Person('Erik', 'Lång')
# p3 = Person('Anna', 'Anka')

# p1.marry(p2)

# def marriageStatus(p):
#     if (p.isMarried()):
#         spouse = p.getSpouse()
#         return p.getFullName() + ' is married to ' + spouse.getFullName()
#     else:
#         return p.getFullName() + ' is not married '
    

# print(marriageStatus(p3))
# # print(marriageStatus(p2))