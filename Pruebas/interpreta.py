# interpreta

def evalua(expresion, objeto):
    
    return True

def interpreta(query, datos):
    # {'$or': [{'ciudad': {'$eq': 'Sevilla'}}, {'$not': {'edad': {'$eq': 30}}}]} 
    # {'$not': {'$or': [{'ciudad': {'$eq': 'Sevilla'}}, {'edad': {'$gte': 30}}]}}
    # {'$not': {'$or': [{'ciudad': {'$eq': 'Sevilla'}}, {'edad': {'$gte': 30}}, {'edad': {'$eq': 49}}]}} 
    '''
    '''
    nodes_selected = list()
    # print('query:',query)
    # print('datos:',datos)
    
    k = list(query.items())[0][0]
    v = list(query.items())[0][1]
    
    for ds_id, ds_element in datos.items():
        if cumple(query, ds_element):
            nodes_selected.append({ds_id:ds_element})
        
    return nodes_selected
    
def cumple(query, ds_element):
    # print(query)
    print(ds_element)
    
    for lval,rval in query.items():
        # print('lval:',lval,'rval:',rval)
        if lval in ('$or','$and','$not'): 
            # es operador lógico
            if lval == '$or':
                for i in rval:
                    if cumple(i,ds_element):
                        return True
                return False
            elif lval == '$and':
                for i in rval:
                    if not cumple(i,ds_element):
                        return False
                return True
            else:
                if cumple(rval,ds_element):
                    return False
                else:
                    return True
        else:
            # es campo:expresion
            # exp1 = eval('ds_element.'+lval)
            exp1 = ds_element[lval]
            op = list(rval.items())[0][0]
            exp2 = list(rval.items())[0][1]
            print('lval:', lval, 'op:',op,'valor:',exp2)
            if op == '$eq':
                if exp1 == exp2:
                    return True
            elif op == '$ne':
                if exp1 != exp2:
                    return True
            elif op == '$gt':
                if exp1 > exp2:
                    return True
            elif op == '$gte':
                if exp1 >= exp2:
                    return True
            elif op == '$lt':
                if exp1 < exp2:
                    return True
            elif op == '$lte':
                if exp1 <= exp2:
                    return True
            elif op == '$in':
                for i in exp2:
                    if exp1 == i:
                        return True
            elif op == '$nin':
                for i in exp2:
                    if exp1 == i:
                        return False
                return True
            else:
                raise Exception('interpreta.cumple()','operador de comparación no contemplado:' + rval)

