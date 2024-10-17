#Ejercicios Capitulo 11

#Ejemplo de creación de un archivo CSV
"""
ruta= r'D:\Ejercicios_Dev\Archivo.csv'

import csv

datos= [
    ['Nombre', 'Edad', 'Sexo'],
    ['Juan', 25, 'M'],
    ['Maria', 22, 'F'],
    ['Pedro', 27, 'M'],
    ['Ana', 24, 'F']
]


with open(ruta, mode= 'w', newline= '', encoding= 'utf-8') as archivo:
#newline indica como se manejan los saltos d elinea o evita que haya 
"saltos de linea innnecesarios
    writer= csv.writer(archivo)
    writer.writerows(datos)

print('Archivo creado con éxito')

#Ejemplo de creación de un archivo CSV con delimitador
#Un delimitador es un caracter que se utiliza para separar los campos de un archivo CSV

ruta= r'D:\Ejercicios_Dev\Delimitador.csv'

import csv

datos= [
    ['Nombre', 'Edad', 'Sexo'],
    ['Juan', 25, 'M'],
    ['Maria', 22, 'F'],
    ['Pedro', 27, 'M'],
    ['Ana', 24, 'F']
]


with open(ruta, mode= 'w', newline= '', encoding= 'utf-8') as archivo:
    writer= csv.writer(archivo, delimiter= ';')
    writer.writerows(datos)

print('Archivo creado con éxito')
"""
#####################################################################################

#Ejemplo de lectura de un archivo CSV
"""
ruta= r'D:\Ejercicios_Dev\Archivo.csv'

import csv

with open(ruta, mode= 'r', newline= '', encoding= 'utf-8') as archivo:

    reader= csv.reader(archivo)
    datos= list(reader)

for fila in datos:
    print(fila)
"""

#Ejemplo de lectura de un archivo CSV con delimitador
"""
ruta= r'D:\Ejercicios_Dev\Delimitador.csv'

import csv

with open(ruta, mode= 'r', newline= '', encoding= 'utf-8') as archivo:
    
        reader= csv.reader(archivo, delimiter= ';')
        datos= list(reader)

for fila in datos:
    print(fila)
"""
#####################################################################################

#Ejemplo de creación de un archivo CSV con diccionarios
"""
ruta= r'D:\Ejercicios_Dev\Diccionario.csv'

import csv

datos= [
    {'Nombre': 'Juan', 'Edad': 25, 'Sexo': 'M'},
    {'Nombre': 'Maria', 'Edad': 22, 'Sexo': 'F'},
    {'Nombre': 'Pedro', 'Edad': 27, 'Sexo': 'M'},
    {'Nombre': 'Ana', 'Edad': 24, 'Sexo': 'F'}
]

campos= ['Nombre', 'Edad', 'Sexo']

with open(ruta, mode= 'w', newline= '', encoding= 'utf-8') as archivo:
     
    writer= csv.DictWriter(archivo, fieldnames= campos)
    writer.writeheader()
    writer.writerows(datos)

print('Archivo creado con éxito')

#Ejemplo de lectura de un archivo CSV con diccionarios

ruta= r'D:\Ejercicios_Dev\Diccionario.csv'

import csv

with open(ruta, mode= 'r', newline= '', encoding= 'utf-8') as archivo:
        
        reader= csv.DictReader(archivo)
        datos= list(reader)

for fila in datos:
    print(fila)
"""
#####################################################################################

#Ejemplo de lectura de un archivo CSV de listas con DictReader
"""
ruta= r'D:\Ejercicios_Dev\Archivo.csv'

import csv

with open(ruta, mode= 'r', newline= '', encoding= 'utf-8') as archivo:
     
    reader= csv.DictReader(archivo)
    datos= list(reader)

for fila in datos:
    print(fila)
"""
#####################################################################################

#Ejemplo de lectura de diccionario con Reader
"""
ruta= r'D:\Ejercicios_Dev\Diccionario.csv'

import csv

with open(ruta, mode= 'r', newline= '', encoding= 'utf-8') as archivo:
         
        reader= csv.reader(archivo)
        datos= list(reader)

for fila in datos:
    print(fila)
"""
#####################################################################################

#Dialectos
"""
Los dialectos son un conjunto de reglas que definen 
cómo se deben leer y escribir los archivos CSV.

Los dialectos se pueden personalizar y se pueden utilizar
para simplificar la escritura y lectura de archivos CSV.

Los dialectos se pueden utilizar para definir el delimitador
de campos, el delimitador de texto, el caracter de escape,
el caracter de nueva línea y el caracter de retorno de carro.
"""

#Ejemplo de escritura de un archivo CSV en tab-excel

ruta= r'D:\Ejercicios_Dev\Excel.csv'

import csv

datos= [
    ['Nombre', 'Edad', 'Sexo'],
    ['Juan', 25, 'M'],
    ['Maria', 22, 'F'],
    ['Pedro', 27, 'M'],
    ['Ana', 24, 'F']
]

with open(ruta, mode= 'w', newline= '', encoding= 'utf-8') as archivo:
        
        writer= csv.writer(archivo, dialect= 'excel-tab')
        writer.writerows(datos)

print('Archivo creado con éxito')

with open(ruta, mode= 'r', newline= '', encoding= 'utf-8') as archivo:
            
            reader= csv.reader(archivo, dialect= 'excel-tab')
            datos= list(reader)

for fila in datos:
    print(fila) 

#####################################################################################

#Ejemplo de escritura de un archivo CSV en unix

"""
Las características del dialecto unix son las siguientes:

Delimitador de campos: ,
- Define qué símbolo separa los diferentes campos (o columnas) 
dentro de una fila en el archivo CSV.
- En el dialecto unix, el separador de campos es la coma `,`. 
Por lo tanto, cada valor en una fila estará separado por una coma.

Delimitador de texto: "
- Cuando los campos contienen comas, saltos de línea o caracteres 
especiales, pueden estar rodeados de un delimitador de texto para 
evitar confusiones.
- En este dialecto, las comillas dobles `"` se utilizan para encerrar 
campos de texto que contienen comas u otros caracteres especiales.
  Ejemplo: `"texto con , coma"` será tratado como un solo campo.

Carácter de escape: \
- Se usa para escapar caracteres especiales dentro de un campo.
- Si hay una comilla dentro de un texto delimitado por comillas, 
el carácter de escape `\` le indica al programa que esa comilla es 
parte del contenido del campo y no el final del delimitador.
  Ejemplo: `"una \"comilla\" dentro del texto"`.

Carácter de nueva línea: \n
- Define cómo se identifica el final de una línea en el archivo CSV.
- En el dialecto unix, el salto de línea es `\n` (nuevo carácter de línea). 
Esto significa que cada fila de datos termina con un `\n` y una nueva 
línea empieza justo después.

Carácter de retorno de carro: \r
- En algunos casos, un archivo CSV puede tener un retorno de carro (`\r`), 
que es un carácter especial que también indica el final de una línea.
- Aunque no se usa tanto en sistemas modernos, este carácter fue común en 
sistemas más antiguos, como los basados en MacOS clásico.

"""

ruta= r'D:\Ejercicios_Dev\Unix.csv'

import csv

datos= [
    ['Nombre', 'Edad', 'Sexo'],
    ['Juan', 25, 'M'],
    ['Maria', 22, 'F'],
    ['Pedro', 27, 'M'],
    ['Ana', 24, 'F']
]

with open(ruta, mode= 'w', newline= '', encoding= 'utf-8') as archivo:
            
            writer= csv.writer(archivo, dialect= 'unix')
            writer.writerows(datos)

print('Archivo creado con éxito')

with open(ruta, mode= 'r', newline= '', encoding= 'utf-8') as archivo:
                    
                    reader= csv.reader(archivo, dialect= 'unix')
                    datos= list(reader)

for fila in datos:
    print(fila)

#Ejemplo del resultado

#['Nombre', 'Edad', 'Sexo']
#['Juan', '25', 'M']
#['Maria', '22', 'F']
#['Pedro', '27', 'M']

"""
La diferencia entre el dialecto unix y el excel-tab es que el primero utiliza 
el caracter de nueva línea \n y el segundo utiliza el tabulador \t como delimitador
de campos.

Además de esto el dialecto unix no utiliza el caracter de retorno de carro \r
como el excel-tab.

En el ejemplo anterior se puede observar que el archivo Unix.csv se creó con el
dialecto unix y se leyó con el mismo dialecto, por lo que se obtuvo el resultado
correcto.
"""

#####################################################################################

#Información de funciones que se trabajan en el módulo csv referentes principalmente 
#con dialectos

"""
csv.register_dialect: Registra un nuevo dialecto para ser utilizado en la escritura
y lectura de archivos CSV.

csv.get_dialect: Obtiene el dialecto que se está utilizando en un archivo CSV.

csv.list_dialects: Obtiene una lista con los dialectos que se pueden utilizar en
la escritura y lectura de archivos CSV.

csv.unregister_dialect: Elimina un dialecto de la lista de dialectos que se pueden
utilizar en la escritura y lectura de archivos CSV.

csv.field_size_limit: Obtiene o establece el tamaño máximo de los campos que se
pueden leer en un archivo CSV.
"""
