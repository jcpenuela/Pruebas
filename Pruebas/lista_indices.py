'''
Created on 05/01/2014

Guardar índices en iccionario

@author: jcpenuela
'''


import clases.fact

items = list()
indexes = dict()


for i in range(0,10):
    o = clases.fact.Fact('A'+str(i))
    items.append(o)

items[4].hecho='A1'
print(items)

indexes['_hash'] = dict() # hash(objeto)
indexes['_hash']['keys'] = dict()
for i,o in enumerate(items):
    k = hash(o)
    if k not in indexes['_hash']['keys']:
        indexes['_hash']['keys'][k] = list() 
    indexes['_hash']['keys'][k].append(i)
print(indexes['_hash'])


indexes['_insert'] = dict() # hash(objeto)
indexes['_insert']['keys'] = dict()

for i,o in enumerate(items):

for i,o in enumerate(items):
    k = hash(o)
    if k not in indexes['_hash']['keys']:
        indexes['_hash']['keys'][k] = list() 
    indexes['_hash']['keys'][k].append(i)
print(indexes['_hash'])

indexes['funcion'] = dict() # objeto.indice_fact()
indexes['funcion']['keys'] = dict()
indexes['funcion']['exp'] = 'indice_fact'
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print(type(items[0].indice_fact))
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for i,o in enumerate(items):
    f = getattr(o,indexes['funcion']['exp'])
    k = f()
    if k not in indexes['funcion']['keys']:
        indexes['funcion']['keys'][k] = list() 
    indexes['funcion']['keys'][k].append(i)
print(indexes['funcion'])
      
indexes['atributo'] = dict() # objeto.hecho
indexes['atributo']['keys'] = dict()
indexes['atributo']['exp'] = 'hecho'
print(type(items[0].hecho))
for i,o in enumerate(items):
    f = getattr(o,indexes['atributo']['exp'])
    k = f
    if k not in indexes['atributo']['keys']:
        indexes['atributo']['keys'][k] = list() 
    indexes['atributo']['keys'][k].append(i)
print(indexes['atributo'])
    




