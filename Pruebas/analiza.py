def normalizar(nodo, nivel=1):
    '''
    Convierte la consulta en un árbol
    '''
    logical_operators = {
                '$or':'list',     # { $or: [ { <expression1> }, { <expression2> }, ... , { <expressionN> } ] }
                '$and':'list',    # { $and: [ { <expression1> }, { <expression2> } , ... , { <expressionN> } ] }
                '$not':'one',    # { field: { $not: { <operator-expression> } } }
                '$nor':'list'    # { $nor: [ { <expression1> }, { <expression2> }, ...  { <expressionN> } ] }
                }
    
    if len(nodo)>1:
        # Hay un AND de algún tipo no reflejado con operador lógico
        # {'ciudad':['Sevilla','Huelva'], 'edad':30} o
        # [{'ciudad':['Sevilla','Huelva'], 'edad':30}] =>
        # {'$and':[{'ciudad':['Sevilla','Huelva']}, {'edad':30}]}
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
        # ¿es operador lógico?
        if k not in logical_operators: #('$and','$or','$not'):
            # es un operador de expresión de comparación
            # tratamos los valores a asignar
            if isinstance(v,list):
                # normalizar lista $in
                nv = dict()
                nv['$in'] = list()
                for i in v:
                    nv['$in'].append(i)
                return { k: nv }
            elif isinstance(v,dict):
                # se supone que es un par clave:valor
                return { k: v}
            else:
                # DEBUG:
                return { k: {'$eq':v} }
        else:
            # es operador lógico
            # Si la lista que acompaña al operador solo tiene un elemento
            # contamos, de momento, con que los operadores son de lista de elementos
            # teniendo en cuenta que tenemos que introducir operadores unarios {'$not':{'ciudad':'sevilla'}}
            if logical_operators[k] == 'one':
                # es operador lógico unario
                return { k: normalizar(v, nivel+1)}
            else: # es un operador cuyo operando es una lista de elementos ($and o un $or)
                # es operador lógico binario
                if isinstance(v,list) or isinstance(v,tuple) or isinstance(v,set) or isinstance(v,dict):            
                    if len(v) == 1: # si solo tiene un elemento en esa lista, quitamos el operador
                        # Por ejemplo: {'$or':[{'ciudad':'Sevilla'}]}
                        # Pasa a convertirse en {'ciudad':'Sevilla'}
                        if isinstance(v,list) or isinstance(v,tuple) or isinstance(v,set):
                            return normalizar(v[0], nivel+1)
                        else:
                            # en caso de tupla se recoje como un elemento suelto... no se por qué!
                            return normalizar(v, nivel+1)
                    else:
                        # el operador trae una lista como parámetros de entrada
                        nv = dict()
                        nv[k] = list() # Elemento con el operador como clave
                        # pasamos a formar la lista con cada elemento 
                        # normalizado
                        for i in v:
                            nv[k].append(normalizar(i, nivel+1))
                        return nv
                else:
                    # un operador de lista debe llevar una lista
                    raise Exception('¿¿Pero esto que es...??','{<OperadorLógico>:<lista>|<dict>|<set>|<tupla>}')
