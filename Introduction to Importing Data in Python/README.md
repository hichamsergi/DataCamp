# 📘 Introduction to Importing Data in Python

---

## 1. Descripción general

En este curso aprenderás las bases para importar datos a Python desde distintos formatos de archivo.
Conocerás cómo leer archivos planos, formatos estructurados como Excel o SAS, y también cómo conectarte a bases de datos relacionales mediante SQL.
Este conocimiento es esencial para cualquier perfil orientado al análisis de datos o ingeniería de datos.

--- 

## 2. Índice de capítulos

1. [Introducción y ficheros planos](#capítulo-1-introducción-y-ficheros-planos)
   - [Manipulación de documentos](#11-manipulación-de-documentos)
   - [Ficheros planos](#12-ficheros-planos)
   - [Importar archivos planos en NumPy](#13-importar-archivos-planos-en-numpy)
   - [Importar archivos planos en Pandas](#14-importar-archivos-planos-en-pandas)
2. [Importar datos de otros tipos de archivos](#capítulo-2-importar-datos-de-otros-tipos-de-archivos)
3. [Trabajar con bases de datos relacionales en Python](#capítulo-3-trabajar-con-bases-de-datos-relacionales-en-python)

---

## 3. Apuntes

### Capítulo 1: **<ins>Introducción y ficheros planos</ins>**

#### 1.1) **<ins>Manipulación de documentos</ins>**:
Para poder leer datos de ficheros planos, lo primero es aprender a manipular archivos en python. La forma de hacerlo es especialmente simple, simplemente los abrimos con la función ```open```. 

```open``` nos permite interactuar con el archivo del modo que le indiquemos como `r`, de *read* para solo leerlo, o `w`, de *write* para poder poder escribir sobre el mismo documento:

```python

filename = 'quijote.txt' # Asignamos el nombre del documento a una variable.

file = open(filename, mode='r') # Abrimos el archivo

texto = file.read() # De esta forma almacenamos todo el texto
                    # contenido en el archivo, dentro de la varible texto
file.close()
```

Como se puede ver en el fragmento de código anterior, al final utilizamos un cierre, `file.close()`. El cierre finaliza la función `open`, por lo que podemos decir que cerramos el fichero que hemos abierto. De esta forma, no solo nos aseguramos que todo los datos se guardan correctamente, sino que tambien ejercemos una buena práctica de programación en python.

Pese a ello, si somos un poco perezosos y no queremos tener que acordarnos de cerrar todos los documentos que abramos, podemos hacerlo con una declaración `with`. Esta nos permite ejecutar comandos dentro de la declaración, con el documento abierto, y además sin necesidad de tener que acordarnos de cerrar el documento una vez estamos fuera de la declaración:

```python
with open('quijote.txt', 'r') as file:
        
    print(file.read()) # Mostramos el contenido de la lectura del fichero.
```

#### 1.2) **<ins>Ficheros planos</ins>**:

Lo primero de todo es entender que es un archivo plano, estos **son archivos de texto basicos que contienen registros, datos de tablas sin relaciones estructuradas**.

Si profundizamos en los **registros**(*record*), veremos que cada uno corresponde a una línea del archivo que contiene diferentes datos, estos datos suelen estar separados por un **delimitador**, como `,` o `;`.

En cambio, las **columnas**(*column*), representan los atributos o campos que describen cada dato dentro de los registros.

Un ejemplo simple para entenderlo sería:

```
usuario,producto,precio
KM37,Teclado,25
PR19,Ratón,18
YU88,Pantalla,132
```

Este fragmento, sería una representación de un documento **CSV**. Los documentos *CSV*, *Comma-Separated values*, repesentan la información separando los valores por comas. Su extensión es `*.csv`.

Aun así, hay multiples tipos de formatos y delimitadores de campos. Dependiendo de que tipo de documento y datos que contenga, podemos llegar a utilizar diferentes *paquetes* con módulos útiles para importar documentos y poder manipular los datos contenidos.

Algunos de los paquetes útiles para la importación y manipulación de datos:

- **Pandas**: Tanto para datos numéricos como para cadenas de texto que queramos almacenar en *DataFrames*, como documentos tipo `*.csv`
    
- **Numpy**: Si el documento consta enteramente de números, que queramos alacenar en una *matriz numpy* como los documentos *MNIST*.

#### 1.3) **<ins>Importar archivos planos en NumPy</ins>**:

Como acabamos de comentar, NumPy es de los mejores paquetes que hay para manipular datos numericos. Aprender a utilizar alguna de sus funciones puede ser esencial dependiendo de la tarea que queramos realizar. Utilizando el caso que comentabamos de los archivos *MNIST*, podemos utilizarlo de la siguiente forma:

```python

import numpy as np # Importamos el paquete y lo renombramos

filename = 'MNIST.txt'

datos = np.loadtxt(filename, delimiter=',') # Utilizamos esta función para cargar los datos
                                            # Tambien definimos el delimitador como ','
```

Tambien nos podemos encontrar con casos en los que el documento tenga encabezados que debamos evitar en la carga de datos. Simplemente utilizamos el parametro `skiprows`, indicandole el número de líneas a evitar:

```python

import numpy as np # Importamos el paquete y lo renombramos

filename = 'MNIST.txt'

datos = np.loadtxt(filename, delimiter=',', skiprows=1) # Evitamos solo la primera línea
```

Otro parametro útil puede ser `usecols`, donde podemos recoger únicamente los datos de los registros contenidos en las columnas especificadas:

```python

import numpy as np # Importamos el paquete y lo renombramos

filename = 'MNIST.txt'

datos = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=[0,2]) # Especificamos que queremos 
                                                                       # la primera y la tercera columna
```

De igual forma, trabajar con otros tipos de datos en NumPy no es dificil tampoco. Podemos especificar el tipo de dato que queremos para que todas las entradas sean como indicamos:

```python

datos = np.loadtext(filename, delimiter=',', dtype=str) # Todos los datos serán strings
```

#### 1.4) **<ins>Importar archivos planos en Pandas</ins>**:

Pandas tambien tiene su forma de 

### Capítulo 2: **<ins>Importar datos de otros tipos de archivos</ins>**

---

### Capítulo 3: **<ins>Trabajar con bases de datos relacionales en Python</ins>**

---

