
import pickle

import clases.fact

f1 = clases.fact.Fact('A')
f1 = clases.fact.Fact('A')

b = pickle.dumps(f1)
print(len(b))
print(b)
fd=pickle.loads(b)

print(hash(f1))
print(hash(fd))

print(f1)
print(fd)

print(f1.hecho)
print(fd.hecho)
fd.hecho='B'
print(fd.hecho)
print(hash(fd))
