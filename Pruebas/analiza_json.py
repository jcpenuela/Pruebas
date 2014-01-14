import ply.lex as lex

reserved = {'null':'NULL',
            'true':'TRUE',
            'false':'FALSE'}
tokens = ['OP',
          'SIMB',
          'COLON',
          'STRING', 'NUMBER', 'FALSE', 'TRUE', 'NULL'
          'LPAREN','RPAREN',
          'LBRAC','RBRAC',
          'LCURBRAC','RCURBRAC'] + list(reserved.values())

t_COLON = r'\:'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRAC = r'\['
t_RBRAC = r'\]'
t_LCURBRAC = r'\{'
t_RCURBRAC = r'\}'

t_OP = 0
t_SIMB = 0
t_STRING = 0
t_NUMBER = 0
t_FALSE = 
t_TRUE', '
t_NULL'

def t_OP(t):
    r'$'
    pass

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
    
    # Name    Description
    # $or    Joins query clauses with a logical OR returns all documents that match the conditions of either clause.
    # $and    Joins query clauses with a logical AND returns all documents that match the conditions of both clauses.
    # $not    Inverts the effect of a query expression and returns documents that do not match the query expression.
    # $nor    Joins query clauses with a logical NOR returns all documents that fail to match both clauses.
    logical_operators = {
        '$or':'eq',     # { $or: [ { <expression1> }, { <expression2> }, ... , { <expressionN> } ] }
        '$and':'ne',    # { $and: [ { <expression1> }, { <expression2> } , ... , { <expressionN> } ] }
        '$not':'gt',    # { field: { $not: { <operator-expression> } } }
        '$nor':'gte'    # { $nor: [ { <expression1> }, { <expression2> }, ...  { <expressionN> } ] }
        }

    # 
    
    print('Análisis')
    print(query)
    print('Elementos: ', len(query))
    for registro_numero, registro in datos.items():
        print(registro_numero, end='... ')
        # aplicar búsqueda
        for lvalue, rvalue in query.items():
            if lvalue[0] == '$':
                # es un operador
                pass
            else:
                # es un campo
                # según el RVALUE actuamos de una forma u otra
                rvalue_class_name = rvalue.__class__.__name__
                if rvalue_class_name == 'list':
                     
    
    print()



if __name__ == '__main__':
    
    analiza({'ciudad':'sevilla'})
    analiza({'ciudad':['sevilla','huelva']})  
    analiza({'ciudad':['sevilla','huelva'], 'edad':30})    
    analiza({'ciudad':['sevilla','huelva'], 'edad':{'$gte':30}})    
    analiza({'$or':[{'ciudad':'sevilla'}, {'edad':{'$gte':30}}]})
