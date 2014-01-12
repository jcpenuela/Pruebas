'''
Created on 11/01/2014

@author: jcpenuela
'''
import clases.fact

def prueba():
    f = clases.fact.Fact('uno')
    f2 = clases.fact.Fact('uno')
    print(hash(f))
    print(hash(f2))

if __name__ == '__main__':
    prueba()