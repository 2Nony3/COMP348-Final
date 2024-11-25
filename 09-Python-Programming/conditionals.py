print("Loop 1: simple While countdown")
x = 10
while(x): # this while loop will run until x is 0
    print(x)
    x -= 1   
    
print("\n\nloop 2: For list")
for x in ['dog', 'bird', 'bear', 'cat']:
    print (x)
  
  
# the range function is quite useful   
print("\n\nloop 3: simple range")
for x in range(10): # this will loop 10 times
    print(x) 
   
   
# the range function is quite useful   
print("\n\nloop 4: complex range")
for x in range(10,100,5):
    print (x) 
   
   
print("\n\nloop 5: char string")  
for x in 'dog house':
    print(x) 
    
    
    
#simple IF
foo = 10
bar = 4

print("\n\nIF test...")
if foo < 0  and bar < 0:
    print("small values in IF ")
elif foo > 10 and bar > 4:
    print("big value in ELIF")
else:
    print("medium values in ELSE")
    
