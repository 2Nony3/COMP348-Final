#:)

class Bat:

    foo = 99

    def __init__(self):
        self.baz = "baz"
        
    def display(self):
        print("Bat: foo=", self.foo, ", baz=", self.baz)
        

class Bar:

    foo = 99
    
    class Inner:
        foo = 1000

    def __init__(self):
        self.baz = "baz"
        
    def display(self):
        print("Bar: foo=", self.foo, ", baz=", self.baz, ", inner foo=", self.Inner.foo)
  

baz = Bat()
bar = Bar()

baz.display()
bar.display()      

        