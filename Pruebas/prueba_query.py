import analiza
import interpreta
def carga_datos():
    d = dict()
    d[1] = {'nombre': 'S18', 'ciudad':'Sevilla', 'edad':18, 'peso':45.6 }
    d[2] = {'nombre': 'S30', 'ciudad':'Sevilla', 'edad':30, 'peso':60.2 }
    d[3] = {'nombre': 'H19', 'ciudad':'Huelva', 'edad':19, 'peso':75.3 }
    d[4] = {'nombre': 'H25', 'ciudad':'Huelva', 'edad':25, 'peso':82.6 }
    d[5] = {'nombre': 'C40', 'ciudad':'Córdoba', 'edad':40, 'peso':59.2 }
    d[6] = {'nombre': 'C35', 'ciudad':'Córdoba', 'edad':35, 'peso':63.1 }
    d[7] = {'nombre': 'Z42', 'ciudad':'Cádiz', 'edad':42, 'peso':75.5 }
    d[8] = {'nombre': 'Z29', 'ciudad':'Cádiz', 'edad':29, 'peso':85.8 }
    return d

if __name__ == '__main__':
    
    d = carga_datos()
    # normalizar({'$not':{'ciudad':'Sevilla'}})
    # normalizar({'$not':{'ciudad':['Sevilla','Huelva']}})  
    q = analiza.normalizar({'ciudad':'Sevilla'})
    print(q)
    n = interpreta.interpreta(q,d)
    print(n)
    print()
    # normalizar({'ciudad':['Sevilla','Huelva']})  
    q = analiza.normalizar({'ciudad':['Sevilla','Huelva']})
    print(q)
    n = interpreta.interpreta(q,d)
    print(n)
    print()
    
    
    # normalizar({'ciudad':['Sevilla','Huelva'], 'edad':30})
    q = analiza.normalizar({'ciudad':['Sevilla','Huelva'], 'edad':30})
    print(q)
    n = interpreta.interpreta(q,d)
    print(n)
    print()
    
    # normalizar([{'ciudad':['Sevilla','Huelva']}, {'edad':30}])
    q = analiza.normalizar([{'ciudad':['Sevilla','Huelva']}, {'edad':30}])
    print(q)
    n = interpreta.interpreta(q,d)
    print(n)
    print()

    # normalizar({'ciudad':['Sevilla','Huelva'], 'edad':{'$gte':30}})    
    q = analiza.normalizar({'ciudad':['Sevilla','Huelva'], 'edad':{'$gte':30}})
    print(q)
    n = interpreta.interpreta(q,d)
    print(n)
    print()
    
    # normalizar({'$or':[{'ciudad':'Sevilla'}, {'edad':{'$gte':30}}]})
    q = analiza.normalizar({'$or':[{'ciudad':'Sevilla'}, {'edad':{'$gte':30}}]})
    print(q)
    n = interpreta.interpreta(q,d)
    print(n)
    print()
    
    # q = analiza.normalizar({'$not':{'$or':[{'ciudad':'Sevilla'}, {'edad':{'$gte':30}}, {'edad':49}]}})
    q = analiza.normalizar({'$not':{'$or':[{'ciudad':'Sevilla'}, {'edad':{'$gte':30}}, {'edad':49}]}})
    print(q)
    n = interpreta.interpreta(q,d)
    print(n)
    print()
    
    
    # n = interpreta.interpreta(q,d)
    # print(n)
    # normalizar({'$or':[{'ciudad':'Sevilla', 'edad':{'$lte':31}}, {'edad':{'$gte':30}}]})
    q = analiza.normalizar({'$or':[{'ciudad':'Sevilla', 'edad':{'$lte':31}}, {'edad':{'$gte':30}}]})
    print(q)
    n = interpreta.interpreta(q,d)
    print(n)
    print()
    
    # normalizar({'$or':[ {'ciudad':'Sevilla'}, {'edad':{'$gte':30}} ], 'peso':{'$gte':60}})
    q = analiza.normalizar({'$or':[ {'ciudad':'Sevilla'}, {'edad':{'$gte':30}} ], 'peso':{'$gte':60}})
    print(q)
    n = interpreta.interpreta(q,d)
    print(n)
    print()
    
    # normalizar({'$or':[{'ciudad':'Sevilla'}, {'edad':{'$gte':30}}],  '$and':[{'peso':{'$gte':60}},{'ciudad':{'$ne':'Córdoba'}}]})
    q = analiza.normalizar({'$or':[{'ciudad':'Sevilla'}, {'edad':{'$gte':30}}],  '$and':[{'peso':{'$gte':60}},{'ciudad':{'$ne':'Córdoba'}}]})
    print(q)
    n = interpreta.interpreta(q,d)
    print(n)
    print()
    
    