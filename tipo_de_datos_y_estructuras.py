'''
<class 'int'>:identifica que la variable en un entero
<class 'float'>:identifica que la variable es un numero decimal
<class 'str'>:identifica que la variable en una cadena de texto
<class 'boolean'>:identifica que la variable en un valor tru o false
'''

x=True # true y false son paralabras reservadas del lenguaje 
# print(type(x))


autor='alejandro'
# print(type(autor))

carro="this is andrews' car:"
modelo='1999'
# print(carro + modelo) #el simbolo + permite conectar texo en Python


'''
TIPOS DE ESTRUCTURA DE DATOS Y MÉTODOS

1.conjuntos        +
2.tuplas           ++
3.listas           +++
4.diccionarios     ++

'''
#1. USO DE CONJUNTOS 
'''Los sets o conjuntos son estructuras especiales que nos ayudan a almacenera un grupo
de elementos. Cuando el orden de los elementos no es relevante podemos utilizar sets
en Python
 ademas este metodo permite supremir datos doble
como se define {, , , , , }

'''
set1={"a","b",'c','d'}
# print(type(set1))

set2={"e",'f',"g"}

# * metodos para el tratamiento de conjuntos

#union de conjuntos
# print(set1.union(set2))


set3={"a","b","c","c","d","d"}
# print(set3)

set4=set3.union(set1)
# print(set4)

#interseccion de conjuntos con python

set5={"f", "w", "a", "b"}

# print(set5.intersection(set1))

# print(set5.remove("w"))
# print(set5)

# print(set4.issuperset(set5))

set6={"andres", 5, True}
set7={"andres", 5, True, "Alejandro"}
# print(set6.issuperset(set7)) # False
# print(set7.issuperset(set6)) # True

# print(set6.issubset(set7)) #true
# print(set7.issubset(set6)) #false

'''
***** USO DE TUPLAS
son estruccturas de datos rigidas, que no permiten muchos metodos
se usan cuando queremos resguardar la informacion de (inmutable)
como se define (, , , , , )
si permiten valores duplicados
<class 'tuple'>

'''
tupla1=(1,1,1,1,1,1,2,3,4,5,)
# print(type(tupla1))

#Metodos 
#cont
conteo=tupla1.count(1)
# print(conteo)

#index
indice=tupla1.index(5)
# print(indice) 
'''python es un lenguaje indexado en cero
siempre el primer elemento en una estrucctura de datos tiene
el indice 0, es decir, la posiscion inicial siempre es 0
INDICE: posicion
'''

'''
******USO DE LISTAS
Las listas de python son estrcturas de datos que almacenan elementos de manera ordenada y multiple.
son un tipo de datos nativos del lenguaje de programacion python.
como se define [, , , , , ]
si permiten valores duplicados
<class 'list'>
pueden contener cualquier tipo de dato,
numero, letras,o incluso otras listas
'''
lista1=[8,9,7,5,4,10]
# print(type(lista1))

lista2=[["jhon", "alejandro", "leguin"],["isabel", "juan", "daniel"]]
# print(type(lista2)) # <class 'list'>

# #metodos
# #count
# print(lista1.count(14))

#reverse
lista1.reverse()
# print(lista1)

# #append
lista1.append("20")
# print(lista1)

#remove
lista1.remove(7)
print=(lista 1)


#acceder a los elementos de la lista

lista2=[["jhon", "alejandro", "leguin"],["isabel", "juan", "daniel"]]
print(lista2[0][1])
      




      