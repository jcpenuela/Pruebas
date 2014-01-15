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

    
    
def analiza(query):
    datos = carga_datos()
    # print(datos)
    comparison_operators = {
        '$eq':'eq',     # { field: {$eq: value} }
        '$ne':'ne',     # { field: {$ne: value} }
        '$gt':'gt',     # { field: {$gt: value} }
        '$gte':'gte',   # { field: {$gte: value} }
        '$lt':'lt',     # { field: {$lt: value} }
        '$lte':'lte',   # { field: {$lte: value} }
        '$in':'in',     # { field: {$in: [<value1>, <value2>, ... <valueN> ]} }
        '$nin':'nin'    # { field: {$nin: [ <value1>, <value2> ... <valueN> ]} }
        }
    logical_operators = {
        '$or':'eq',     # { $or: [ { <expression1> }, { <expression2> }, ... , { <expressionN> } ] }
        '$and':'ne',    # { $and: [ { <expression1> }, { <expression2> } , ... , { <expressionN> } ] }
        '$not':'gt',    # { field: { $not: { <operator-expression> } } }
        '$nor':'gte'    # { $nor: [ { <expression1> }, { <expression2> }, ...  { <expressionN> } ] }
        }
    print('----------------------------------------------------------')
    print('Análisis:', query)
    print('Elementos: ', len(query))
    print('Normalizando....')
    query = normalizar(query)
    print('Normalizada:',query)
    # for registro_numero, registro in datos.items():
    #    print(registro_numero, end='... ')
        # aplicar búsqueda
        

    print('\nFin análisis....\n')

def normalizar(nodo, nivel=1):
    
    print('.'*nivel, end='')
    print('- nomalizando nodo=',nodo)
    
    if len(nodo)>1:
        # Hay un AND
        # {'ciudad':['Sevilla','Huelva'], 'edad':30} =>
        # [{'ciudad':['Sevilla','Huelva'], 'edad':30}] =>
        # {'$and':[{'ciudad':['Sevilla','Huelva']}, {'edad':30}]}
        print('.'*nivel, end='')
        print('- nodo es: ', nodo.__class__.__name__, ' y tiene elementos:',len(nodo))
        nq = dict()
        nq['$and'] = list()
        
        if isinstance(nodo, list) or isinstance(nodo, set) or isinstance(nodo, tuple):
            for v in nodo:
                nq['$and'].append(normalizar(v,nivel+1))
        
        elif isinstance(nodo, dict):
            for k,v in nodo.items():
                nq['$and'].append(normalizar({k: v},nivel+1))
        return nq
    
    else:
    
        k = list(nodo.items())[0][0]
        v = list(nodo.items())[0][1]
        print('.'*nivel, end='')
        print('- k,v:',k,v)    
        # ¿es operador lógico?
        if k not in ('$and','$or'):
            # es un field
            print('.'*nivel, end='')
            print('- k es field')
            if isinstance(v,list):
                # normalizar lista $in
                print('.'*nivel, end='')
                print('- v es lista')
                nv = dict()
                nv['$in'] = list()
                for i in v:
                    nv['$in'].append(i)
                return { k: nv }
            elif isinstance(v,dict):
                print('.'*nivel, end='')
                print('- v es expresión comparación')
                return { k: v }
            else:
                print('.'*nivel, end='')
                print('- v es elemento')
                return { k: {'$eq':v} }
        else:
            # es operador lógico
            print('.'*nivel, end='')
            print('- k es operador lógico')
            # Si la lista que acompaña al operador solo tiene un elemento
            # contamos, de momento, con que los operadores son de lista de elementos
            # teniendo en cuenta que tenemos que introducir operadores unarios {'$not':{'ciudad':'sevilla'}}
            
            if isinstance(v,list) or isinstance(v,tuple) or isinstance(v,set) or isinstance(v,dict):            
                if len(v) == 1:
                    # Por ejemplo: {'$or':[{'ciudad':'Sevilla'}]}
                    # Pasa a convertirse en {'ciudad':'Sevilla'}
                    print('.'*nivel, end='')
                    print('- v es de tipo ', v.__class__.__name__)
                    if isinstance(v,list) or isinstance(v,tuple) or isinstance(v,set):
                        return normalizar(v[0], nivel+1)
                    else:
                        # en caso de tupla se recoje como un elemento suelto... no se por qué!
                        return normalizar(v, nivel+1)
                else:
                    # el operador trae una lista como parámetros de entrada
                    nv = dict()
                    nv[k] = list() # Elemento con el operador como clave
                    print('.'*nivel, end='')
                    print('- v`s a normalizar (', len(v),'):', v)
                    for i in v:
                        print('.'*nivel, end='')
                        print('  - elemento i para norm:',i)
                        nv[k].append(normalizar(i, nivel+1))
                    return nv
            else:
                print('ERROR: v debe ser un valor iterable')
                raise Exception('¿¿Pero esto que es...??','{<OperadorLógico>:<lista>|<dict>|<set>|<tupla>}')
    
def xnormaliza_raiz(query):    
    nq = dict()
    if len(query)>1:
        # Hay un AND
        # {'ciudad':['Sevilla','Huelva'], 'edad':30} =>
        # {'$and':[{'ciudad':['Sevilla','Huelva']}, {'edad':30}]}
        nq['$and'] = list()
        for k,v in query.items():
            nq['$and'].append({k: v})
    else:
        nq = query
    return normalizar(nq)
    
    
if __name__ == '__main__':
    
    analiza({'ciudad':'Sevilla'})
    analiza({'ciudad':['Sevilla','Huelva']})  
    analiza({'ciudad':['Sevilla','Huelva'], 'edad':30})
    # print('>>>>>>>>>>>>>>')
    analiza([{'ciudad':['Sevilla','Huelva']}, {'edad':30}])
    analiza({'$or':({'ciudad':'Sevilla'},{'edad':30})})
    # analiza({'$or':1})
    
    analiza({'ciudad':['Sevilla','Huelva'], 'edad':{'$gte':30}})    
    analiza({'$or':[{'ciudad':'Sevilla'}, {'edad':{'$gte':30}}]})
    # print('>>>>>>>>>')
    analiza({'$or':[{'ciudad':'Sevilla', 'edad':{'$lte':31}}, {'edad':{'$gte':30}}]})
    analiza({'$or':[ {'ciudad':'Sevilla'}, {'edad':{'$gte':30}} ], 'peso':{'$gte':60}})
    analiza({'$or':[{'ciudad':'Sevilla'}, {'edad':{'$gte':30}}],  '$and':[{'peso':{'$gte':60}},{'ciudad':{'$ne':'Córdoba'}}]})
    
    