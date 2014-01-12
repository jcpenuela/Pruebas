'''
Created on 06/01/2014

@author: jcpenuela
'''
def modifica(lista):
    lista[0]=100
    
def original():
    lista = [0,1,2,3]
    print(lista)
    modifica(lista)
    print(lista)
    
if __name__ == '__main__':
    print('prueba')
    original()
    
