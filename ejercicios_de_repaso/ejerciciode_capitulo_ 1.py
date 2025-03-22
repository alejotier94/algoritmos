



#ejercicio 1.1
'''Escriba un programa que defina inicialmente x=4,
utilice la función input para capturar del usuario un
valor y. Calcule con x y con y la suma de los valores
y guárdelo en una variable z. Al ejecutar, el
programa debe entregar un print con el siguiente
texto: “El resultado es: “, y el valor resultante de z.'''

# x=4
# y=int(input ('introduce un valor para y:'))
# z=x+y
# print('el resultado es: ', z) 

#ejercicio 1.2
'''Escriba un programa que defina inicialmente x=4,
utilice la función input para capturar del usuario un
valor y. Calcule con x y con y la resta de los valores
y guárdelo en una variable z. Al ejecutar, el
programa debe entregar un print con el siguiente
texto: “El resultado de la resta es: “, y el valor
resultante de z.'''

# x=4
# y=int(input("introduce un valor para y:"))
# z=x-y
# print("El resultado de la resta es:",z)


#ejercicio 1.2

'''Escriba un programa que defina inicialmente x=8,
utilice la función input para capturar del usuario un
valor y. Calcule con x y con y la división de los
valores y guárdelo en una variable z. Al ejecutar, el
programa debe entregar un print con el siguiente
texto: “El resultado es: “, y el valor resultante de z'''

# x=8
# y=float(input("intruduzca un valor :"))
# if y !=0:
#  z=x/y
#  print("el resultado es :", z)
# else:
#  print("error: no se puede dividir entre 0")

 #ejercicio 1.4


'''Escriba un programa que capture del usuario dos
valores a y b en dos inputs sucesivos. Pida al
usuario desde la función input que los valores a
ingresar deben contener al menos un número
decimal. Al ejecutar, el programa debe realizar la
multiplicación entre los dos valores y entregar la
respuesta en un formatted string que contenga
una variable llamada resultado y el texto de su
preferencia.'''

# a=float(input("introduzca un numero entero o decimal"))
# b=float(input("introduzca un valor decimal"))
# resultado=a*b
# print(f"el resultado es:{resultado}")

#ejercicio 1.5
'''
Escriba un programa que realice la comprobación
de la división. Recuerde:
Divisor * Cociente + Residuo = Dividendo
Tome como entrada dos números, realice la
división entre ellos y entregue al usuario un texto
descriptivo con la comprobación de la división.
'''
# dividendo=int(input("ingrese el primer numero"))
# divisor=int(input("ingrese el segundo numero"))

# #calculo
# cociente=dividendo/divisor
# residuo=dividendo%divisor
# print(f"la comprobacion de la division es {divisor} por {cociente} mas {residuo} igual a {dividendo}")

# jercicio 1.6

''' calcule el residuo con el símbolo de módulo % y entregue la
comprobación con los valores resultantes de dividir
dos números entregados por el usuario del
programa.'''

# a=int(input("introduzca el dividendo a:"))
# b=int(input("introduzca el divisor b:"))
# if b !=0:
#  cociente=a//b
#  residuo=a%b
#  comprobacion=(b*cociente) + residuo
#  print(f"dividendo: {a}, divisor:{b}")
#  print(f"cociente: {cociente}, residuo: {residuo}")
#  print(f"comprobacion: {b} * {cociente} + {residuo} = {comprobacion}")
#  if comprobacion == a:
#        print("la comprobacion es correcta")
#  else:
#     print("la comprobacion es incorrecta")
# else:
#    print("error: el divisor no puede ser 0")

#ejercicio 1.7

'''Compruebe en un programa si el valor 29.0 es igual
a 29 utilizando el operador de comparación
correspondiente.
'''
#difinir los valores

# x=29.0
# y=29
# es_igual= x==y
# #comprovar si son iguales 

# print(f"son iguales los valores? {es_igual}")

#ejercicio 1.8
'''Compruebe en un programa si la expresión “true”
es igual a “True” mediante el operador de
comparación correspondiente.'''

# x="True"
# y="true"
# es_igual= x==y
# #comprovar si son iguales 

# print(f"son iguales los valores? {es_igual}") 

# ejercicio 1.9   

'''Compruebe mediante el operador de identidad
correspondiente si la letra w se encuentra en la
expresión “Python es un lenguaje de programación
muy popular”. Utilice un input para consultar lo
mismo y comprobar según la entrada que dé el
usuario. '''

texto= "Python es un lenguaje de programación muy popular"
letra_w="w" in texto
print(f"la letra w esta en el texo {letra_w}")