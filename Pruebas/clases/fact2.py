'''
Created on 05/01/2014

@author: jcpenuela
'''

class Fact2(object):
    '''
    classdocs
    '''


    def __init__(self, hecho):
        '''
        Constructor
        '''
        self.hecho = hecho
        
    def __eq__(self, *args, **kwargs):
        if args[0].hecho == self.hecho:
            return True
        else:
            return False
    
    def __hash__(self):
        return hash(self.hecho)
        
    def hashkey(self):    
        return hash(self.hecho)
    
    def indice_fact2(self):
        return self.hecho + 'X'
    
    