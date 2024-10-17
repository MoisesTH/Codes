#Ejercicios Capitulo 9

#Closure

"""
Objeto de tipo función que guarda el estado de una variable
en el momento de su creación y la mantiene a lo largo de su
vida útil.

Se usa principalmente de base para entender las estructuras de las funciones anidadas
"""
"""
Cuando hablamos de Closures
necesitamos considerar dos funciones que contendran un parametro en cada una de ellas

En el siguiente ejemplo los parametros son 'n' para la funcion exterior, y 'x' para la funcion interior.

El objetivo de la funcion será multiplicar los dos parametros llevando a cabo la operacion de manera 
interna sin la necesidad de crear alguna otra función o llevar a cabo la multiplicacion por medio de operadores.

"""
#Ejemplo

"""def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

#Necesitamos pasar dos parametros siguiendo 
#la estructura para esto utilizaremos la asginacion de la funcion y le pasaremos dos parametros

#Primero a través de la funcion
times3 = make_multiplier_of(3)
#Segundo a través de la asignacion que hicimos
print(times3(9))"""

#Alternativas para la asignación de parametros
"""
#Pasar los dos valores directos
times3 = make_multiplier_of(5)(8)
print(times3) #Resultado
"""
"""
#Los valores exteriores se pueden asignar sin tener que colocar de inmediato el segundo valor a usar.
#Funciones para almacenar el primer valor
times3 = make_multiplier_of(9)
times2 = make_multiplier_of(3)

#Aqui colocaremos los siguientes valores
print(times3(9), times2(9))
"""
###################################################################################

#Lambda

"""
Funciones anónimas que se pueden usar para simplificar el código.

Uso principal en situaciones en las que no se requiere una función
compleja, sino una función simple que se puede definir en una sola línea.
"""

#Ejemplo
#lambda argumentos: expresión

"""
Similar a la estructura de las listas por comprension lambda nos permite 
generar comportamientos en la variable o las variables que
colocamos inmediato a lambda para posteriormente generar el comportamiento después 
de los dos puntos permitendo usarla como asignacion a una variable
"""
"""
ff= lambda x: x*2
print(ff(3))

gg= lambda x, y: x + y
print(gg(2, 3))

#El siguiente ejercicio trabaja con colecciones
#Debido al uso de indices

hh= lambda a: a[0] + a[1]
#Ejecutando una tupla
print(hh((10, 30)))
#Ejecutando una lista
print(hh([10, 30]))

#Ejemplo de lambda con valores booleanos

f = lambda x: x ** .5 == int(x ** .5)
print(f(4))
print(f(5))

#Ejemplo de lambda con más de un argumento
resta = lambda x, y: x - y
print(resta(10, 3))  # Imprime 7


#Ejemplo con map
def cuadro(n):
    return n ** 2

#Ejemplo con map
#map genera una lista de resultados de aplicar
# una función a cada elemento de un iterable

#Ejemplo usando rango
ss = list(map(cuadro, range(10)))
print(ss)

#Ejemplo con lambda y rango

ss = list(map(lambda x: x ** 2, range(10)))
print(ss)

"""

#Ejemplo filter
#filter(función, iterable)
"""
filter() es una función que devuelve un iterador que produce los elementos
para los que la función devuelve True

#Filtra
"""

#Ejemplo con función normal y filter
"""def es_par(n):
    return n % 2 == 0

pares = list(filter(es_par, range(10)))
print(pares)

#Ejemplo con lambda y filter

pares = list(filter(lambda x: x % 2 == 0, range(10)))
print(pares)"""

###################################################################################

"""
Las funciones anidadas buscan generar una relación entre dos funciones diferentes 
permitiendo que haya una interaccion entre los parametros de ambas o las acciones de estas

"""

#Funciones Anidadas

#El siguiente ejercicio devuelve dos mensajes de dos funciones pero solo teniendo que llamar a una

"""def outer_function():
    print("Outer function")
    def nested_function():
        print("Nested function")
    nested_function()

#Llamando solo a la primer funcion estaríamos obteniendo ambas
outer_function()"""


#En el siguiente ejemplo se trabaja el parametro de la primer funcion en la segunda
"""
def outer_fun(msg):
    def inner_fun():
        print(f'Message is: {msg}')
    inner_fun()

outer_fun("Hello")"""


#Encapsulamiento
#Caso especifico

"""
Consiste en ocultar los detalles de implementación de un objeto
y mostrar solo los detalles que sean necesarios para interactuar
con él.

La diferencia principal radica en los parametros que necesita un objeto
para funcionar correctamente en el caso de la función anidada, no necesita
ningun parametro para funcionar en el caso de la funcion externa.
"""

#El siguiente es un ejemplo normal de un closure, lo tomaremos de base para observar después el encapsulamiento
"""
def crear_closure(valor):
    def closure(numero):
        return valor + numero
    return closure

mi_closure = crear_closure(10)

print(mi_closure(5))  # Imprime 15


#Encapsulamiento ejemplo

# La variable `valor` está capturada en el closure.
#Recuerda el tema de Variables Locales
def otro_closure():
    valor = 20
    def closure(numero):
        return valor + numero
        #return valor = 5 # Esto no funcionará
    return closure

mi_otro_closure = otro_closure()

print(mi_otro_closure(5))  # Imprime 25

"""
#NOTA
#No podemos modificar el valor de la variable valor en el closure
#No son válidas las asginaciones "="
#pero sí podemos modificar el valor de la variable como se ve 
#en el ejemplo anterior


#Encapsulamiento con variables globales
#Modificación de variables usando asignación
def contenedor():
    global valor
    valor = 10

    def closure():
        global valor
        valor += 5  # Esto ahora funcionará
   
    return closure

mi_closure = contenedor()
mi_closure()
print(valor)  # Imprime 15

#NOTA
#Nosotros podemos ingresar a la variable valor en 
# cualquier momento una vez que hemos creado el objeto en este caso "mi_closure"

#Decorador

"""
Un decorador es una función que recibe otra función y retorna una nueva función
que modifica el comportamiento de la función original.

La funcion decorada es la que se ejecuta con el decorador de manera interna

Se usa principalmente para extender el comportamiento de una función sin modificarla

"""

#Ejemplo sin usar arroba

def decorador(funcion):
    def nueva_funcion(): #Extiende las propiedades de la función
        print("Código antes de ejecutar la función")
        funcion()
        print("Código después de ejecutar la función")
    return nueva_funcion #Retorna la función extendida con el decorador

def funcion_a_decorar():
    print("Función a decorar")

funcion_decorada = decorador(funcion_a_decorar)
funcion_decorada()
funcion_a_decorar()

print("#"*50)

"""
En este caso podemos usar esta estructura para decorar una función
y a su vez nos permite poder llamar a la funcion
decorada de manera directa
"""

"""
A continuación se observa un ejemplo de un decorador utilizando el arroba
para poder decorar la función de manera directa

No se necesita forzosamente utilizar la palabra decorador para poder
decorar una función, pero en este caso se utiliza para poder entender
"""

#Ejemplo con arroba

def decorador(funcion):
    def nueva_funcion():
        print("Código antes de ejecutar la función")
        funcion()
        print("Código después de ejecutar la función")
    return nueva_funcion

@decorador
def funcion_a_decorar():
    print("Función a decorar")

funcion_a_decorar()
print("#"*50)

"""
Para este caso se usa el arroba para poder decorar la función
de manera directa, sin necesidad de llamar a la función decorada

Si necesitaramos llamar a la función decorada de manera directa
no tenemos una alternativa para poder hacerlo sin tener que usar
un módulo especializado.
"""
