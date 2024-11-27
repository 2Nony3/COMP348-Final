

class MyClass(object):
    
    foo = 99


    def __init__(self):
        self.bar = 43
     

x = MyClass()
print(x.foo)
print(x.bar)

x.dog = "dog"
print(x.dog)  


#y = MyClass()
#print (y.dog) # this will throw an error as dog is not a class variable


MyClass.pop = "pop"
y = MyClass()
print (y.pop) # some ides may not recognize dynamically added attributes

del(x.dog)
#print (x.dog) # this will throw an error as dog is deleted from x