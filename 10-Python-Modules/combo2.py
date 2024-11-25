
import combo

def that():
    print("combo2.that")
  
def name():
    print("combo2 name: ", __name__)  

print("in combo.2...")
name()
combo.woop()
combo.name()


# in combo.3... TODO this will print becaucase this module imports combo and combo import comb3, so it is automatically executed
# in combo.2...
# combo2 name:  __main__
# combo.woop
# combo name:  combo
#
# Process finished with exit code 0