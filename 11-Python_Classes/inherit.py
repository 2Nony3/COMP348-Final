
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
    

class Foo(Baz): # this is how we inherit a class in python
    
    duck = 11
    
    def __init__(self):
        super().__init__()
        self.duck = "duck"
        
    def get_duck(self):
        return self.duck
 
    
class Bart(Baz):
    
    def __init__(self):
        Baz.__init__(self) # this is how we call the constructor of the parent class, in java we use super()
        
        
myBaz = Baz()
print("\nBaz.pip:", myBaz.get_pip())
print("Baz.plop:", myBaz.get_plop())

myFoo = Foo()
print("\nFoo.pip:", myFoo.get_pip())
print("Foo.duck:", myFoo.get_duck())
# try this
print ("Foo.plop:", myFoo.get_plop()) # this will throw an error as Foo overrides the constructor of Baz, it does not call the constructor of BAz
#means that the self.plop is never initialized in Foo to fix it -> super().__init__()

myBart = Bart()
print("\nBart.pip:", myBart.get_pip())
print("Bart.plop:", myBart.get_plop())

        