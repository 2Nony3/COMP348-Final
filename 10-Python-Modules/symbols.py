'''
Created on Feb 26, 2018

@author: eavis
'''


import boo
import sys
import builtins

x = 43
y = "foo"
def thump():
    print("thump")
    
def noo(x):
    print(x)


print("\nlet's look at symbols...")

print("\nboo symbols: ")
print(dir(boo))


print("\nsys symbols: ")
print(dir(sys))

print("\nlocal symbols: ")
print(dir()) # this is the dir for the current module


print("\nsome default symbols: ")
print("__doc__: ", __doc__) # this is the docstring (which is on created typed at the beginning of this module ) for the current module
print("__file__: ", __file__) # this is the file directory name of the current module
print("\n__builtin__: ", dir(builtins)) # this is the builtins module. Builtins module contains a list of built-in functions, exceptions, and other objects.


