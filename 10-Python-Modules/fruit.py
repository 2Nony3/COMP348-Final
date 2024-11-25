'''
Created on Nov. 5, 2019

@author: toddeavis
'''

from foo import *

import grape.foo

from orange import foo as ofoo # ofoo is an alias for foo, we named it so we can use it in the code below


up()
down()

grape.foo.up()
grape.foo.down()

ofoo.up()
ofoo.down()


