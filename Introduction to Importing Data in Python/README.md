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
    - [Archivos Pickled](#21-archivos-pickled)
    - [Archivos Excel](#22-archivos-excel)
    - [Archivos SAS/Stata](#23-archivos-sasstata)
    - [Archivos HDF5](#24-archivos-hdf5)
    - [Archivos MATLAB](#25-archivos-matlab)

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

- **Numpy**: Muy útil si el documento consta enteramente de números que queramos alacenar en una *matriz numpy*, como los documentos *MNIST*.

- **Pandas**: Tanto para datos numéricos como para cadenas de texto que queramos almacenar en *DataFrames*, como documentos tipo `*.csv`.

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

De igual forma, trabajar con otros tipos de datos en NumPy no es difícil. Podemos especificar el tipo de dato que queremos para que todas las entradas sean como indicamos:

```python

datos = np.loadtext(filename, delimiter=',', dtype=str) # Todos los datos cargados serán strings
```

En resumen, NumPy es la herramienta ideal para poder manejar datos númericos dadas las matrices tan eficientes que podemos generar.

#### 1.4) **<ins>Importar archivos planos en Pandas</ins>**:

Pandas tambien tiene su forma de importar archivos planos. Pero su principal atractivo es algo de lo que ya hemos hablado antes, y en lo que ahora profundizaremos, los **DataFrames**. 

Esta estructura de datos organizada en filas y columnas similar a una tabla de base de datos. Y podemos organizar los datos importados de un documento en un **DataFrame**:

```python

import pandas as pd

filename = 'calidad_vino.csv'

datos = pd.read_csv(filename)

datos.head() # Así mostramos los primeros 5 registros.

array_datos = datos.to_numpy() # Convertimos el DataFrame de datos
                               # en una matriz de NumPy
```

Otra forma de indicarle a pandas que queremos un número determinado de registros es con `nrow=*`, donde le indicamos el número que queremos:

```python
data = pd.read_csv(file, nrows=5, header=None)
```

El argumento `header` debe contener el número de líneas que ocupa el encabezado del documento, siendo un argumento posicional. En el caso de no tener ningúno debemos de indicar **None**.

Hay multiples argumentos que podemos indicar en la función de importación de documentos. Desde indicarle el separador de datos, con `sep='*'`, hasta el carácter que interpretamos como comentario, con `comment='*'`, pasando por especificar los strings que podemos considerar como *valores no disponibles(**Na**)*:

```python

file = 'titanic_corrupt.txt'

data = pd.read_csv(file, sep='\t', comment='#', na_values=['Nothing'])
```

En este caso **\t** representa una tabulación, como **\n** podría representar un salto de línea.

### Capítulo 2: **<ins>Importar datos de otros tipos de archivos</ins>**


#### 2.1) **<ins>Archivos Pickled</ins>**:
Como el nombre del capítulo indica, hay otros tipos de archivo a parte de los planos. Podemos empezar, con los **archivos Pickled**, archivos encurtidos. Es un tipo de archivos nativos de python, nace con la necesidad de almacenar diferentes tipos de datos de los que no es tan obio como almacenarlos, como diccionarios o listas. Algun ejemplo:

```python
import pickle

with open('pickled_fruit.pkl','rb') as file:
    
    data = pickle.load(file)

print(data) # {'limon':13, 'manzana':4, 'naranja':11}
```

Es importante indicar el tipo de modo en el que abrimos el archivo para poder interpretar los datos contenidos. En el caso del ejemplo anterior, indicamos el valor `'rb'`, especificando dos cosas:

1. El archivo lo abriremos en modo de **SOLO LECTURA**, `'r*'`. 
2. El archivo es un **binario**, únicamente legible por una máquina, `'*b'`.

#### 2.2) **<ins>Archivos Excel</ins>**:
También tenemos las **hojas de cálculo de Excel**, un tipo de archivo tan extendido y utilizado que no necesita ningún tipo de presentación ni descripción. En este caso nos interesa interpretarlo con *Pandas* dado que podemos generar DataFrames con el contenido de las hojas:

```python
import pandas as pd

file = 'contabilidad.xlsx'

data = pd.ExcelFile(file)

print(data.sheet_names) #['1960-1966','1967-1974','1975-2020']
```

Dado que este tipo de archivos se organizan en hojas, lo primero sería identificar la hoja que queremos utilizar. Podemos acceder a ellas tanto por el nombre como por el indice que ocupan en la lista generada por la función **`data.sheet_names`**:

```python
df1 = data.parse('1960-1966') #Nombre de la hoja, como un string
df2 = data.parse(1) #Indice de la hoja
```

Dado que en ambos ejemplos hemos almacenado la información como DataFrame de la hoja que queremos utilizar, ahora tenemos contenido en las variables `df1` y `df2` únicamente la información que nos interesa. De hecho podemos jugar la función parse y generar DataFrames "personalizados", de forma que la información que contengan esté organizada de la forma que deseemos:

```python

df3 = data.parse(2, usecols=[0], skiprows=[0], names=['Country'])
```

De esta forma hacemos lo siguiente:

- `usecols=[*]`: Utilizamos unicamente las columnas que indicamos, especificado en indice o nombre. 

- `skiprows=[*]`: Evitamos incluír los registros indicados, especificado como el indice que ocupa el registro que queremos evitar.

- `names=['Country']`: Atribuimos un nombre a la columna del DataFrame que queremos evitar.

De esta forma indicamos que únicamente utilizaremos la primera columna de la tercera hoja del libro de Excel contenido en `data`. Además, evitamos la primera fila, dado que contiene el encabezado de la columna, y lo renombramos como *Country*.

---

#### 2.3) **<ins>Archivos SAS/Stata</ins>**:
Los archivos **SAS**, *Statisctical Analysis System*, son habitualmente utilizados para el análisis avanzado, adminitración de datos e inteligéncia de negocios, utilizar los datos para mejorar.

Los archivos SAS más comúnes suelen tener una extensión **sas7bdat**, y los podemos importar de la siguiente forma:

```python

import pandas as pd
from sas7bdat import SAS7BDAT

with SAS7BDAT('urbanpop.sas7bdat') as file:

    df_sas = file.to_data_frame() #De esta forma convertimos los datos SAS7BDAT en un DataFrame
```

Por otro lado los documentos **Stata**, *Statistics data*, que podríamos decir que contienen el mismo tipo de información que los SAS, tienen una extensión **dta**. También se importan de otra manera:

```python
import pandas as pd

data = pd.read_stata('urbanpop.dta')
```

#### 2.4) **<ins>Archivos HDF5</ins>**:

#### 2.5) **<ins>Archivos MATLAB</ins>**:



---
### Capítulo 3: **<ins>Trabajar con bases de datos relacionales en Python</ins>**

---

