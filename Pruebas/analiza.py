def operadores():
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

def normalizar(nodo, nivel=1):
    '''
    Convierte la consulta en un árbol
    '''
    # DEBUG:
    # print('.'*nivel, end='')
    # print('- nomalizando nodo=',nodo)
        
    
    if len(nodo)>1:
        # Hay un AND de algún tipo no reflejado con operador lógico
        # {'ciudad':['Sevilla','Huelva'], 'edad':30} =>
        # [{'ciudad':['Sevilla','Huelva'], 'edad':30}] =>
        # {'$and':[{'ciudad':['Sevilla','Huelva']}, {'edad':30}]}
        
        # DEBUG:
        # print('.'*nivel, end='')
        # print('- nodo es: ', nodo.__class__.__name__, ' y tiene elementos:',len(nodo))
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
        # tomamos el nodo y su parámetro (valor)
        k = list(nodo.items())[0][0]
        v = list(nodo.items())[0][1]
        
        # DEBUG:
        # print('.'*nivel, end='')
        # print('- k,v:',k,v)    
        
        # ¿es operador lógico?
        if k not in ('$and','$or','$not'):
            # es un field o un un operador unario
            
            # DEBUG:
            # print('.'*nivel, end='')
            # print('- k es field')
            
            # tratamos los valores a asignar
            if isinstance(v,list):
                # normalizar lista $in
                # DEBUG:
                # print('.'*nivel, end='')
                # print('- v es lista')
                nv = dict()
                nv['$in'] = list()
                for i in v:
                    nv['$in'].append(i)
                return { k: nv }
            elif isinstance(v,dict):
                # se supone que es un par clave:valor
                # DEBUG:
                # print('.'*nivel, end='')
                # print('- v es expresión comparación')
                return { k: v}
            else:
                # DEBUG:
                # print('.'*nivel, end='')
                # print('- v es elemento')
                return { k: {'$eq':v} }
            
            
        else:
            # es operador lógico
            # DEBUG:
            # print('.'*nivel, end='')
            # print('- k es operador lógico')
            # Si la lista que acompaña al operador solo tiene un elemento
            # contamos, de momento, con que los operadores son de lista de elementos
            # teniendo en cuenta que tenemos que introducir operadores unarios {'$not':{'ciudad':'sevilla'}}

            if k == '$not':
                # es operador lógico unario
                return { k: normalizar(v, nivel+1)}
            
            
            else: # $and y $or
                # es operador lógico binario
                if isinstance(v,list) or isinstance(v,tuple) or isinstance(v,set) or isinstance(v,dict):            
                    if len(v) == 1:
                        # Por ejemplo: {'$or':[{'ciudad':'Sevilla'}]}
                        # Pasa a convertirse en {'ciudad':'Sevilla'}
                        # DEBUG:
                        # print('.'*nivel, end='')
                        # print('- v es de tipo ', v.__class__.__name__)
                        if isinstance(v,list) or isinstance(v,tuple) or isinstance(v,set):
                            return normalizar(v[0], nivel+1)
                        else:
                            # en caso de tupla se recoje como un elemento suelto... no se por qué!
                            return normalizar(v, nivel+1)
                    else:
                        # el operador trae una lista como parámetros de entrada
                        nv = dict()
                        nv[k] = list() # Elemento con el operador como clave
                        # DEBUG:
                        # print('.'*nivel, end='')
                        # print('- v`s a normalizar (', len(v),'):', v)
                        for i in v:
                            # DEBUG:
                            # print('.'*nivel, end='')
                            # print('  - elemento i para norm:',i)
                            nv[k].append(normalizar(i, nivel+1))
                        return nv
                else:
                    # DEBUG:
                    # print('ERROR: v debe ser un valor iterable')
                    raise Exception('¿¿Pero esto que es...??','{<OperadorLógico>:<lista>|<dict>|<set>|<tupla>}')
    
    
if __name__ == '__main__':
    
    # analiza({'$not':{'ciudad':'Sevilla'}})
    # analiza({'$not':{'ciudad':['Sevilla','Huelva']}})  
    # analiza({'ciudad':'Sevilla'})
    # analiza({'ciudad':['Sevilla','Huelva']})  
    # analiza({'ciudad':['Sevilla','Huelva'], 'edad':30})
    # analiza([{'ciudad':['Sevilla','Huelva']}, {'edad':30}])
    nq = normalizar({'$or':({'ciudad':'Sevilla'},{'$not':{'edad':30}})})
    print(nq)
    # analiza({'$or':1})
    # analiza({'ciudad':['Sevilla','Huelva'], 'edad':{'$gte':30}})    
    # analiza({'$or':[{'ciudad':'Sevilla'}, {'edad':{'$gte':30}}]})
    nq = normalizar({'$not':{'$or':[{'ciudad':'Sevilla'}, {'edad':{'$gte':30}}]}})
    print(nq)
    nq = normalizar({'$not':{'$or':[{'ciudad':'Sevilla'}, {'edad':{'$gte':30}}, {'edad':49}]}})
    print(nq)
    # analiza({'$or':[{'ciudad':'Sevilla', 'edad':{'$lte':31}}, {'edad':{'$gte':30}}]})
    # analiza({'$or':[ {'ciudad':'Sevilla'}, {'edad':{'$gte':30}} ], 'peso':{'$gte':60}})
    # analiza({'$or':[{'ciudad':'Sevilla'}, {'edad':{'$gte':30}}],  '$and':[{'peso':{'$gte':60}},{'ciudad':{'$ne':'Córdoba'}}]})
    
    