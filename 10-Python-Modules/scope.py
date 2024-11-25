'''
Created on Feb 26, 2018

@author: eavis
'''


woo = "woohoo"

def run():
    print("woo inside run: ", woo)
    

def hop():
    #print "woo inside hop 1: ", woo
    woo = 99
    print("woo inside hop 2: ", woo)


def jump():
    #print "woo inside 1: ", woo
    global woo
    print("woo inside 2: ", woo)
    woo = 43



#main code
print("woo at start: ", woo)

run()
print("woo after run: ", woo)

hop()
print("woo after hop: ", woo)

jump()
print("woo after jump: ", woo)

