

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




#print "\nafter 2nd updates..."
#del(m.x)
#Baz.x = "test"

#print "m.x: ", m.x
#print "m.y: ", m.y
#print "p.x: ", p.x
#print "p.y: ", p.y

