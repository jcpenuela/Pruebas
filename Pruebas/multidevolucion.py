'''
Created on 04/01/2014

@author: jcpenuela
'''

def funcion_multidevolucion():
    return 'A',2

if __name__ == '__main__':
    print(funcion_multidevolucion())
    (a,b)=funcion_multidevolucion()
    print(a)