

#Ejercicio 2.1

'''Cree una variable llamada cadena que contenga una cadena de texto “Python puro”. '
' Al crearla verifique el tipo de dato que queda guardado en memoria utilizando la función type.'''

# cadena_de_texto= "python puro"
# print(type(cadena_de_texto)) # <class 'str'> "es str ya que se trata de una variable de solo texto"

#ejercicio 2.2

'''Utilice un método que le permita poner en mayúscula la palabra puro.'''

# x="puro"
# print(x.upper()) # upper para cambiar las palabras a mayusculas

#ejercicio 2.3

'''Qué diferencia encuentra entre el método titlle y el método capitalize.'''

#capitalize
"covierte unicamente la primera letra de cadena a mayuscula y convierte el resto a minuscula"

# texto="python ES asombroso"
# print(texto.capitalize())

# titlle
"convierte la primera letra de cada palabra en mayuscula y convierte el resto de las letras decada"
"parala en minusculas"

# texto="python es asombroso"
# print(texto.title())

# ejercicio 2.4

'''Aplique un método para verificar si la letra o es la que finaliza la cadena de caracteres.'''
# texto= "python pura"
# print(texto.endswith("o")) # es un buleano

#ejercicio 2.5

'''Investigue cómo utilizar el método casefold sobre la cadena de texto y para qué serviría.'''

# texto= "python pura"
# print(texto.casefold()) # nos permite identificar que contiene una variable

"este metodo se utiliza para realizar comparaciones de texto que no distinga mayusculas y minusculas, "
"es mas potente por que meneja ciertos idionas y caracteres especiales"
'''proposito: sirve para comparar cadenas de texto de manera insensible a las diferencias de caso,
util en validaciones o busqueda'''

# ejercicio 2.6

'''Cree un programa que defina una lista con las primeras cinco letras del alfabeto en minúscula.
 Posterior a la creación de la lista,
 aplique un método para insertar en la posición 2 la letra a. Ahora,
 aplique un método para contar el número de veces que la letra a se encuentra en la lista creada.'''

# letras=["a", "b", "c", "d", "e"]
# letras.insert(2,"a")
# print(letras)

# print(letras.count("a"))

# ejercicio 2.7

'''Utilizando la lista creada en el punto anterior aplique el método que le permita eliminar 
la letra c que se encuentra en la posición 3. Confirme que el método utilizado devuelva 
la letra eliminada y que al llamar nuevamente la lista el elemento no se encuentre en
 la posición indicada.'''

# letras=["a", "b", "a", "c", "d", "e"]
# letras.pop(3)
# print(letras)
# letras.append("c")
# print(letras)

#ejercicio 2.8

'''Cree una lista con los números del 1 al 10 considerando el orden de su preferencia.
 Llame a la lista valores. Aplique un método que le permita ordenar los valores desde el mayor al menor.
 Si ahora utiliza la función sorted sobre la lista,
 ¿qué diferencia encuentra?.''' 
 # sort= modifica la lista de la posision mayor a la posision menor
 #sorted= ordena nuevamente la lista de menor a mayor

# valores=["1", "3", "5", "2", "10", "9", "8", "7", "4", "6"]
# valores.sort(reverse=True)
# print(valores)

# valores=sorted(valores)
# print(valores)

# ejercicio 2.9

'''
Considere la creación de una nueva lista llamada duplicada que sea una copia de la lista valores.
 Posteriormente ejecute una instrucción para que la copia 
 quede ordenada desde los valores más bajos a los más altos.
'''

# duplicada=valores.copy()
# print(valores)

# duplicada.sort()
# print(duplicada)

# ejercicio 2.10
'''
Cree una tupla llamada ventas que considere en la primera posición el nombre de un producto y su precio.
 Para el ejemplo puede considerar leche como el nombre y su precio 5.
   Utilice el método index para consultar el índice correspondiente al precio.
     Ahora en otra instrucción y utilizando el índice intente reemplazar el elemento 
     asignándole un nuevo valor 8.
 ¿Qué interpreta del error que sale al ejecutar la instrucción?'''
# el error ecurre por q las tuplas son inmutables, lo que significa que no pueden ser modificadas despues
# de ser creadas, esto es diferente a una lista que si permite cambio a sus elementos

# ventas=("leche", 5)
# ventas.index(5)
# ventas.index(8)
# print(ventas)



