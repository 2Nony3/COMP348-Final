# functions (without objects) and methods (inside objects)
# are very easy to define. We use the "def" keyword, a colon (":")
# at the end of the line, and we indent once for each new block
# of code. No brackets are ever used to define code blocks. In
# addition, no types are ever defined.


# primitive arguments (int, float, etc) are passed as a copy.
# As a result, their original values are not affected
def send_number(number):
    number = 999
  
# complex objects are passed as a copy of the reference. As seen below,
# the original object cannot be re-assigned by changing the reference TODO
# inside the method.   
def swap_list(list1):
    list1 = ['dog', 'cat', 'bird']    
        
   
# We can, however, change data within the object since the original
# reference and the copy of the reference point to the same thing.  #TODO
def update_list(list1):
    list1[0] = ['dog']
  
# we can also return values if we want.   
def get_num():
    return 555


# try out the various functions
print("original values")
number = 11
list1 = [1,2,3]
print(number)
print(list1)

print("\n\nafter send_number function call")
send_number(number)
print(number)

print("\n\nafter swap_list function call")
swap_list(list1)
print(list1)

print("\n\nafter update_list function call")
update_list(list1)
print(list1)

print("\n\nafter get_num function call")
print(get_num())


