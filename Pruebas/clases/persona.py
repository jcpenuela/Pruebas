'''
Created on 05/01/2014

@author: jcpenuela
'''
import hashlib
class Persona(object):
    def __init__(self, nombre, ciudad = None, edad = None):
        self.nombre = nombre
        self.ciudad = ciudad
        self.edad = edad
        
    def __eq__(self, *args, **kwargs):
        return args[0].key == self.key()
    
    def key(self):    
        return (self.nombre, self.ciudad, self.edad)
    
    def __hash__(self):
        return int(hashlib.md5(self.key).hexdigest(),16)
