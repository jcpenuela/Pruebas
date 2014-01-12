'''
Cómo aplicamos un passthrough a un objeto para aplicar una búsqueda 
'''
import clases.persona

def carga_datos():
    d = dict()
    d[1] = clases.persona.Persona('Uno','Sevilla',18)
    d[2] = clases.persona.Persona('H27','Huelva',27)
    d[3] = clases.persona.Persona('M15','Madrid',15)
    d[4] = clases.persona.Persona('S30','Sevilla',30)
    d[5] = clases.persona.Persona('C19','Córdoba',19)
    d[6] = clases.persona.Persona('H45','Huelva',45)
    d[7] = clases.persona.Persona('S42','Sevilla',42)
    d[8] = clases.persona.Persona('C40','Córdoba',40)
    return d

def busca(funcion_buscar):
    datos = carga_datos()
    print(funcion_buscar)
    seleccionados = dict()
    for registro_numero, registro in datos.items():
        # aplicar búsque
        if funcion_buscar(registro):
            print(registro_numero, end=' ')
            seleccionados[registro_numero]=registro
              
    print()
    print(seleccionados)
    print()



if __name__ == '__main__':
    
    busca(lambda x: x.ciudad == 'Sevilla')
    q = "x.ciudad == 'Sevilla'"
    fl = eval("lambda x:" + q)
    busca(fl)
    busca(lambda x: x.ciudad in ('Sevilla','Huelva'))
    busca(lambda x: x.ciudad in ('Sevilla','Huelva') and x.edad==30)
    busca(lambda persona: persona.ciudad in ('Sevilla','Huelva') and persona.edad >= 30)
    busca(lambda persona: persona.ciudad == 'Sevilla' or persona.edad >= 30)
    def f(x):
        return x.ciudad == 'Córdoba'
    busca(f)