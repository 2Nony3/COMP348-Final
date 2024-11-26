

class Baz:
    
    bop = 49
    
    def __init__(self):
        self.bat = 99
        
    def set_bat(self, bat):
        self.bat = bat
        
    def display(self):
        print("Baz.bop:", self.bop, "Baz.bat:", self.bat)
        

class Flip:
    
    x = 77
    y = 99
    
    def __init__(self, stuff, thing="thing"):
        self.stuff = stuff
        self.thing = thing
        
    def set_thing(self, thing):
        self.thing = thing

    def display(self):
        print("Flip.x:", self.x, "Flip.y:", self.y, "Flip.stuff:", self.stuff, "Flip.thing:", self.thing)


myBaz = Baz()
myBaz.display()

# try this
#myFlip1 = Flip()
#myFlip1.display()

myFlip2 = Flip(9999)
myFlip2.display()

myFlip3 = Flip(65, 64)
myFlip3.display()



