'''
Created on 05/01/2014

@author: jcpenuela
'''
import hashlib
class Fact(object):
    def __init__(self, hecho):
        self.hecho = hecho
        
    def __eq__(self, *args, **kwargs):
        if args[0].hecho == self.hecho:
            return True
        else:
            return False
        
    def __hash__(self):
        return int(hashlib.md5(self.hecho.encode()).hexdigest(),16)
    
    def indice_fact(self):
        return '_' + self.hecho + '_'