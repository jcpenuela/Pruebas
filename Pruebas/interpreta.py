# interpreta
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




def interpreta(query, datos):
    # {'$or': [{'ciudad': {'$eq': 'Sevilla'}}, {'$not': {'edad': {'$eq': 30}}}]} 
    # {'$not': {'$or': [{'ciudad': {'$eq': 'Sevilla'}}, {'edad': {'$gte': 30}}]}}
    # {'$not': {'$or': [{'ciudad': {'$eq': 'Sevilla'}}, {'edad': {'$gte': 30}}, {'edad': {'$eq': 49}}]}} 
    
    
    # IMPORTANTE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
    # class Person(object):
    #     def addattr(self,x,val):
    #        self.__dict__[x]=val
    # Método de añadir de forma dinámica una variable a un objeto
    
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
            # Método usando EVAL
            # exp1 = eval('ds_element.'+lval)
            # Método usando __dict__     
            # exp1 = ds_element.__dict__[lval]
            exp1 = ds_element[lval]
            
            
            op = list(rval.items())[0][0]
            exp2 = list(rval.items())[0][1]
            # print('lval:', lval, 'op:',op,'valor:',exp2)
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

