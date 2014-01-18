import interpreta
import clases.persona
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


def carga_datos2():
    d = dict()
    p = clases.persona.Persona('S18', 'Sevilla', 18, 45.6)
    d[1] = p
    p = clases.persona.Persona('S30', 'Sevilla', 30, 60.2)
    d[2] = p
    p = clases.persona.Persona('H19', 'Huelva', 19, 75.3)
    d[3] = p
    p = clases.persona.Persona('H25', 'Huelva', 25, 82.6)
    d[4] = p
    p = clases.persona.Persona('C40', 'Córdoba', 40, 59.2)
    d[5] = p
    p = clases.persona.Persona( 'C35', 'Córdoba', 35, 63.1)
    d[6] = p
    p = clases.persona.Persona('Z42', 'Cádiz', 42, 75.5)
    d[7] = p
    p = clases.persona.Persona('Z29', 'Cádiz', 29, 85.8)
    d[8] = p
    return d


if __name__ == '__main__':
    
    datos = carga_datos2()
    # datos = carga_datos()
    queries = ({'ciudad':'Sevilla'},
         {'ciudad':['Sevilla','Huelva']},
         {'ciudad':['Sevilla','Huelva'], 'edad':30},
         [{'ciudad':['Sevilla','Huelva']}, {'edad':30}],
         {'ciudad':['Sevilla','Huelva'], 'edad':{'$gte':30}},
         {'$or':[{'ciudad':'Sevilla'}, {'edad':{'$gte':30}}]},
         {'$not':{'$or':[{'ciudad':'Sevilla'}, {'edad':{'$gte':30}}, {'edad':49}]}},
         {'$or':[{'ciudad':'Sevilla', 'edad':{'$lte':31}}, {'edad':{'$gte':30}}]},
         {'$or':[ {'ciudad':'Sevilla'}, {'edad':{'$gte':30}} ], 'peso':{'$gte':60}},
         {'$or':[{'ciudad':'Sevilla'}, {'edad':{'$gte':30}}],  '$and':[{'peso':{'$gte':60}},{'ciudad':{'$ne':'Córdoba'}}]}
         )
    # normalizar({'$not':{'ciudad':'Sevilla'}})
    # normalizar({'$not':{'ciudad':['Sevilla','Huelva']}})  
    
    for q in queries:
        n = interpreta.select(q,datos)
        print('QUERY:', q)
        print('    Seleccionados:',len(n))
        print(n)
        print()
        