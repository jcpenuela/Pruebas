
import pickle

import clases.fact

f1 = clases.fact.Fact('A')
f2 = clases.fact.Fact('A')
f1.otro = f2
f2 = None

b = pickle.dumps(f1)
frecuperado=pickle.loads(b)

print('longitud del pickle.dumps:',len(b))
print('contenido del pickle.dumps:',b)
print()

print('hash de f1:',hash(f1))
print('hash de frecuperado:',hash(frecuperado))
print('los dos hash deben ser iguales')
print()

print('f1:',f1)
print('frecuperado:',frecuperado)
print('las dos diferencias deben ser distintas')
print()

print('f1.hecho:',f1.hecho)
print('frecuperado.hecho:', frecuperado.hecho)
print('los dos hechos deben ser iguales')
print()

frecuperado.hecho='B'
print('f1.hecho:',f1.hecho)
print('frecuperado.hecho:', frecuperado.hecho)
print('los dos hechos deben ser distintos')
print()

print('hash de f1:',hash(f1))
print('hash de frecuperado:',hash(frecuperado))
print('los dos hash deben ser diferentes')
print()
