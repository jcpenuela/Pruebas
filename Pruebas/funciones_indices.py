'''
Created on 05/01/2014

@author: jcpenuela
'''

import clases.fact
import clases.fact2

f1=clases.fact.Fact("A")
f2=clases.fact.Fact("A")
f3=clases.fact.Fact("A")
g1=clases.fact2.Fact2("A")
g2=clases.fact2.Fact2("A")
g3=clases.fact2.Fact2("A") 

l = dict()

l[1]=dict()
l[1]['exp']=f1.indice_fact
l[2]=dict()
l[2]['exp']=g1.indice_fact2


print(l[1])
print(l[2])
f1=None
g1=None
print(l[1]['exp']())
print(l[2]['exp']())
print(l[1])
print(l[2])

l[2]['exp']()

ff = l[2]['exp']
# __self__ devuelve el objeto del método enlazado
print(ff.__self__.hashkey())
print(hash(ff.__self__))
print(hash(f2))
f2.hecho='B'
print(hash(f2))
f2.hecho='A'
print(hash(f2))







