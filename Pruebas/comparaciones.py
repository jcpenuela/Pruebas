'''
Created on 05/01/2014

@author: jcpenuela
'''
from clases import *

a=fact.Fact("A")
b=fact2.Fact2("B")
print(a==b)
b=fact2.Fact2("a")
print(a==b)
b=fact2.Fact2("A")
print(a==b)

l=list()
l.append(a)
l.append(b)
print(a,'\n',b,'\n',l[0],'\n',l[1],'\n')
b=None
print(a,'\n',b,'\n',l[0],'\n',l[1])
print("TRUE: ", l[0]==l[1])

print(a.hashkey())
print(l[0].hashkey())
print(l[1].hashkey())



