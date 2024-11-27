

class Baz:
    x = 43
    
    def __init__(self):
        self.y = 99
        
m = Baz()
p = Baz()

print("m.x: ", m.x)
print("m.y: ", m.y)
print("p.x: ", p.x)
print("p.y: ", p.y)

print("\nafter updates...")
m.x = "rooster"
m.y = "doodle"

print("m.x: ", m.x)
print("m.y: ", m.y)
print("p.x: ", p.x)
print("p.y: ", p.y)




print ("\nafter 2nd updates...")
del m.x # this will delete the instance variable x from m and when we try to access it will get the class variable x and modify the value for all constructor
Baz.x = "test"

print ("m.x: ", m.x)
print ("m.y: ", m.y)
print ("p.x: ", p.x)
print ("p.y: ", p.y)

