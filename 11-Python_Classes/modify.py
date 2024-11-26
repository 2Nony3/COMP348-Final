

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
#print y.dog


#MyClass.pop = "pop"
#y = MyClass()
#print y.pop

#del(x.dog)
#print x.dog  