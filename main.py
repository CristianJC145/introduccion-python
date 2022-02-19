listaDinamica = [0,'hola',12.5, [0,1]]

print(listaDinamica[3][1]) #imprimir 1

#Diccionarios -JSON -Objects
persona= {
    'nombre': "Cristian",
    'apellido': 'Jamioy',
    'edad': 27,
    'materias': ['Base de datos II', 'Lenguaje de cuarta generacion'],
}
print(persona['nombre'])#
print(persona['materias'][1])

#lista de diccionarios
personas = [
    {
        'nombre': "Alexander",
        'apellido': 'Checa',
        'edad': 18,
        'materias': ['Base de datos II', 'Lenguaje de cuarta generacion'],
    },

    {
        'nombre': "Cristian",
        'apellido': 'Jamioy',
        'edad': 27,
        'materias': ['Base de datos II', 'Lenguaje orientado a objetos'],
    },

    {
        'nombre': "Andres",
         'apellido': 'Gomez',
        'edad': 17,
         'materias': ['Lenguaje orientdo a eventos'],
    }
]
print(personas[2]['materias'][0])

for per in personas:
    print(per['nombre'])

nombrePersona = 'roberto'
