

import combo3

def woop():
    print("combo.woop")
    
def dedoo():
    print("combo.dedoo")
    
def name():
    print("combo name: ", __name__)
   
def main():   
    print("running combo as driver...")
    name()
    combo3.that()
    
if __name__ == "__main__":
    main()
    
