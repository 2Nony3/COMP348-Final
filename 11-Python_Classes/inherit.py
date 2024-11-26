
class Baz:
    pip = 24
    pop = "pop"
    
    def __init__(self):
        self.plop = 999
        
    def get_pip(self):
        return self.pip
    
    def get_pop(self):
        return self.pop
    
    def get_plop(self):
        return self.plop
    

class Foo(Baz):
    
    duck = 11
    
    def __init__(self):
        self.duck = "duck"
        
    def get_duck(self):
        return self.duck
 
    
class Bart(Baz):
    
    def __init__(self):
        Baz.__init__(self)
        
        
myBaz = Baz()
print("\nBaz.pip:", myBaz.get_pip())
print("Baz.plop:", myBaz.get_plop())

myFoo = Foo()
print("\nFoo.pip:", myFoo.get_pip())
print("Foo.duck:", myFoo.get_duck())
# try this
#print "Foo.plop:", myFoo.get_plop()

myBart = Bart()
print("\nBart.pip:", myBart.get_pip())
print("Bart.plop:", myBart.get_plop())

        