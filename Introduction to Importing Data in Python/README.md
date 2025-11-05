# 📘 Introduction to Importing Data in Python

---

## 1. Descripción general

En este capítulo aprenderás las bases para importar datos a Python desde distintos formatos de archivo.
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
    - [Introducción a las Bases de Datos Relacionales](#31-introducción-a-las-bases-de-datos-relacionales)
    - [Consultas en Bases de Datos Relacionales](#32-consultas-en-bases-de-datos-relacionales)
    - [Consultar bases de datos con Pandas](#33-consultar-bases-de-datos-con-pandas)
    - [JOINing tablas](#34-joining-tablas)

---

## 3. Apuntes

### Capítulo 1: **<ins>Introducción y ficheros planos</ins>**

#### 1.1) **<ins>Manipulación de documentos</ins>**:
Para poder leer datos de ficheros planos, lo primero es aprender a manipular archivos en Python. La forma de hacerlo es especialmente simple, simplemente los abrimos con la función ```open```. 

```open``` nos permite interactuar con el archivo del modo que le indiquemos como `r`, de *read* para solo leerlo, o `w`, de *write* para poder escribir sobre el mismo documento:

```python

filename = 'quijote.txt' # Asignamos el nombre del documento a una variable.

file = open(filename, mode='r') # Abrimos el archivo

texto = file.read() # De esta forma almacenamos todo el texto
                    # contenido en el archivo, dentro de la variable texto
file.close()
```

Como se puede ver en el fragmento de código anterior, al final utilizamos un cierre, `file.close()`. El cierre finaliza la función `open`, por lo que podemos decir que cerramos el fichero que hemos abierto. De esta forma, no solo nos aseguramos de que todos los datos se guarden correctamente, sino que también ejercemos una buena práctica de programación en Python.

Pese a ello, si somos un poco perezosos y no queremos tener que acordarnos de cerrar todos los documentos que abramos, podemos hacerlo con una declaración `with`. está nos permite ejecutar comandos dentro de la declaración, con el documento abierto, y además sin necesidad de tener que acordarnos de cerrar el documento una vez estamos fuera de la declaración:

```python
with open('quijote.txt', 'r') as file:
        
    print(file.read()) # Mostramos el contenido de la lectura del fichero.
```

#### 1.2) **<ins>Ficheros planos</ins>**:

Lo primero de todo es entender que es un archivo plano, estos **son archivos de texto básicos que contienen registros, datos de tablas sin relaciones estructuradas**.

Si profundizamos en los **registros**(*record*), veremos que cada uno corresponde a una línea del archivo que contiene diferentes datos, estos datos suelen estar separados por un **delimitador**, como `,` o `;`.

En cambio, las **columnas**(*column*), representan los atributos o campos que describen cada dato dentro de los registros.

Un ejemplo simple para entenderlo sería:

```
usuario,producto,precio
KM37,Teclado,25
PR19,Ratón,18
YU88,Pantalla,132
```

Este fragmento, sería una representación de un documento **CSV**. Los documentos *CSV*, *Comma-Separated values*, representan la información separando los valores por comas. Su extensión es `*.csv`.

Aun así, hay múltiples tipos de formatos y delimitadores de campos. Dependiendo del tipo de documento y de los datos que contenga, podemos llegar a utilizar diferentes *paquetes* con módulos útiles para importar documentos y poder manipular los datos contenidos.

Algunos de los paquetes útiles para la importación y manipulación de datos:

- **Numpy**: Muy útil si el documento consta enteramente de números que queramos almacenar en una *matriz numpy*, como los documentos *MNIST*.

- **Pandas**: Tanto para datos numéricos como para cadenas de texto que queramos almacenar en *DataFrames*, como documentos tipo `*.csv`.

#### 1.3) **<ins>Importar archivos planos en NumPy</ins>**:

Como acabamos de comentar, NumPy es de los mejores paquetes que hay para manipular datos numéricos. Aprender a utilizar alguna de sus funciones puede ser esencial dependiendo de la tarea que queramos realizar. Utilizando el caso que comentábamos de los archivos *MNIST*, podemos utilizarlo de la siguiente forma:

```python

import numpy as np # Importamos el paquete y lo renombramos

filename = 'MNIST.txt'

datos = np.loadtxt(filename, delimiter=',') # Utilizamos está función para cargar los datos
                                            # también definimos el delimitador como ','
```

también nos podemos encontrar con casos en los que el documento tenga encabezados que debamos evitar en la carga de datos. Simplemente utilizamos el parámetro `skiprows`, indicandole el número de líneas a evitar:

```python

import numpy as np # Importamos el paquete y lo renombramos

filename = 'MNIST.txt'

datos = np.loadtxt(filename, delimiter=',', skiprows=1) # Evitamos solo la primera línea
```

Otro parámetro útil puede ser `usecols`, donde podemos recoger únicamente los datos de los registros contenidos en las columnas especificadas:

```python

import numpy as np # Importamos el paquete y lo renombramos

filename = 'MNIST.txt'

datos = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=[0,2]) # Especificamos que queremos 
                                                                       # la primera y la tercera columna
```

De igual forma, trabajar con otros tipos de datos en NumPy no es difícil. Podemos especificar el tipo de dato que queremos para que todas las entradas sean como indicamos:

```python

datos = np.loadtxt(filename, delimiter=',', dtype=str) # Todos los datos cargados serán strings
```

En resumen, NumPy es la herramienta ideal para poder manejar datos numéricos dadas las matrices tan eficientes que podemos generar.

#### 1.4) **<ins>Importar archivos planos en Pandas</ins>**:

Pandas también tiene su forma de importar archivos planos. Pero su principal atractivo es algo de lo que ya hemos hablado antes, y en lo que ahora profundizaremos, los **DataFrames**. 

esta estructura de datos organizada en filas y columnas similar a una tabla de base de datos. Y podemos organizar los datos importados de un documento en un **DataFrame**:

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

El argumento `header` debe contener el número de líneas que ocupa el encabezado del documento, siendo un argumento posicional. En el caso de no tener ninguno debemos de indicar **None**.

Hay múltiples argumentos que podemos indicar en la función de importación de documentos. Desde indicarle el separador de datos, con `sep='*'`, hasta el carácter que interpretamos como comentario, con `comment='*'`, pasando por especificar los strings que podemos considerar como *valores no disponibles(**Na**)*:

```python

file = 'titanic_corrupt.txt'

data = pd.read_csv(file, sep='\t', comment='#', na_values=['Nothing'])
```

En este caso **\t** representa una tabulación, como **\n** podría representar un salto de línea.

### Capítulo 2: **<ins>Importar datos de otros tipos de archivos</ins>**

#### 2.1) **<ins>Archivos Pickled</ins>**:
Como el nombre del capítulo indica, hay otros tipos de archivo a parte de los planos. Podemos empezar, con los **archivos Pickled**, archivos encurtidos. Es un tipo de archivos nativos de Python, nace con la necesidad de almacenar diferentes tipos de datos de los que no es tan obvio como almacenarlos, como diccionarios o listas. Algún ejemplo:

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

Dado que este tipo de archivos se organizan en hojas, lo primero sería identificar la hoja que queremos utilizar. Podemos acceder a ellas tanto por el nombre como por el índice que ocupan en la lista generada por la función **`data.sheet_names`**:

```python
df1 = data.parse('1960-1966') #Nombre de la hoja, como un string
df2 = data.parse(1) #Índice de la hoja
```

Dado que en ambos ejemplos hemos almacenado la información como DataFrame de la hoja que queremos utilizar, ahora tenemos contenido en las variables `df1` y `df2` únicamente la información que nos interesa. De hecho podemos jugar la función parse y generar DataFrames "personalizados", de forma que la información que contengan este organizada de la forma que deseemos:

```python

df3 = data.parse(2, usecols=[0], skiprows=[0], names=['Country'])
```

De esta forma hacemos lo siguiente:

- `usecols=[*]`: Utilizamos únicamente las columnas que indicamos, especificado en índice o nombre. 

- `skiprows=[*]`: Evitamos incluir los registros indicados, especificado como el índice que ocupa el registro que queremos evitar.

- `names=['Country']`: Atribuimos un nombre a la columna del DataFrame que queremos evitar.

De esta forma indicamos que únicamente utilizaremos la primera columna de la tercera hoja del libro de Excel contenido en `data`. Además, evitamos la primera fila, dado que contiene el encabezado de la columna, y lo renombramos como *Country*.

#### 2.3) **<ins>Archivos SAS/Stata</ins>**:
Los archivos **SAS**, *Statisctical Analysis System*, son habitualmente utilizados para el análisis avanzado, administración de datos e inteligencia de negocios, utilizar los datos para mejorar.

Los archivos SAS más comunes suelen tener una extensión **sas7bdat**, y los podemos importar de la siguiente forma:

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
Otro de los muchos tipos de archivos es **HDF5**, *Hierarchical Data Format version 5*. Lo que diferencia a HDF5 del resto, es el hecho de que es el formato más común para poder almacenar **grandes cantidades de datos numéricos**. Una pregunta lógica sería, `¿Qué tan grandes son estas cantidades?`, y el hecho es que estamos hablando de cientos de gigabytes, sino de terabytes.

Pero para poder entender la magnitud de la que hablamos necesitamos un ejemplo, pero lo primero sería aprender a importarlos:

```python

import h5py

file = 'LOSC_4_V1-815411200-4096.hdf5'

data = h5py.File(file,'r') #Solo lectura
```

Ahora que ya tenemos importado el archivo `LOSC_4_V1-815411200-4096.hdf5`, podemos empezar a jugar con el:

```python

for key in data.keys():

    print(key) #meta
               #quality
               #strain
```

Como podemos ver, la estructura jerárquica de este archivo se puede explorar con el método `*.keys()` de la misma forma que lo haríamos con un diccionario. 

Esto nos puede hacer entender que dado que es un fichero jerárquico y de gran tamaño, cada clave puede llegar a tener otras "subclaves":

```python
for skey in data['meta'].keys:
    
    print(skey) # Description
                # Description
                # Detector
                # GPSstart
                # Type
```

Dado que son datos numéricos, conocemos la estructura jerárquica y sabemos utilizar NumPy, es interesante utilizar este paquete para poder manipular los datos que contienen estos tipos de archivos:

```python
print(np.array(data['meta']['Detector']), np.array(data['meta']['GPSstart']))
```

De esta forma, los datos contenidos en la  jerarquia `meta/Detector` y `meta/GPSstart`, se verán transformados en una matriz de NumPy.

#### 2.5) **<ins>Archivos MATLAB</ins>**:
Matlab, la abreviación de *Matrix Laboratory*, es un tipo de documento ampliamente utilizado en entornos de ciencia e ingeniería. La extensión de este tipo de documentos es **\*.mat**. Pero en cuanto a este tipo de documentos, a diferencia del resto que hemos estado tratando, para poderlos importar necesitamos el módulo de funciones **SciPy**.

**SciPy** tiene dos funciones especialmente interesantes para poder importar archivos:

- **scipy.io.loadmat()**: Nos permite leer documentos en formato Matlab.

- **scipy.io.savemat()**: Nos permite escribir archivos en formato Matlab.

Ahora vamos a poner un ejemplo de como importaríamos un documento Matlab

```python
import scipy.io

filename = 'test.mat'

mat = scipy.io.loadmat(filename)
```

Ahora bien, en el entorno de trabajo de MATLAB podemos visualizar directamente todas las variables utilizadas en nuestro código. En Python, en cambio, esto no funciona de la misma forma: el contenido del archivo .mat se interpreta como un diccionario, donde las claves corresponden a los nombres de las variables creadas en MATLAB, y los valores son los objetos asociados a dichas variables.

Esto se entiende mejor si retomamos el ejemplo anterior y exploramos su estructura:

```python
import scipy.io

filename = 'test.mat'

mat = scipy.io.loadmat(filename)

print(type(mat))      # <class 'dict'>
print(type(mat['x'])) # <class 'numpy.ndarray'>

```

Como se puede observar, el primer objeto (mat) es un diccionario, ya que contiene los nombres de las variables del archivo. En cambio, al inspeccionar uno de sus elementos, por ejemplo mat['x'], accedemos al valor almacenado en esa variable, que en este caso corresponde a una matriz de NumPy.

---

### Capítulo 3: **<ins>Trabajar con bases de datos relacionales en Python</ins>**

#### 3.1) **<ins>Introducción a las Bases de Datos Relacionales</ins>**:
Para entender como funcionan las bases de datos relacionales en Python, hay que entender qué son las bases de datos relacionales. estás son bases de datos basadas en un modelo relacional de datos, lo que implica que la información está contenida en **tablas**, compuestás por **registros** y columnas, **atributos** de cada registro de datos.

esta estructura de bases de datos, es especialmente eficiente cuando las diferentes tablas están interconectadas entre sí. Para poder hacerlo es esencial que cada registro tenga un identificador único, conocido como clave primaria, esto es útil para poder acceder al registro en concreto. Por lo tanto, al contener también claves primarias de otras tablas podemos relacionarlas entre sí. 

Ahora bien, el lenguaje estándar de comunicación con bases de datos es **SQL**, *Structured Query Language* o Lenguaje de Consultas Estructurado. Si bien es diferente de Python, también tiene una sintáxis bastante fácil de comprender:

```sql
SELECT * FROM pedidos WHERE IDcliente = '666';
```

- `*`: Es un valor polivalente, seleccionamos todo lo que coincida.

- `pedidos`: Es el nombre de la tabla de la que seleccionamos la información.

- `IDcliente = '666'`: Podríamos considerarlo como la estructura condicional en la que solo recogemos el registro que coincide con el atributo `IDcliente` igual a `666`.

Todo lo comentado previamente son conceptos básicos, pero imprescindibles, para poder comprender lo que viene a continuación.

Cuando pretendemos trabajar con una base de datos desde Python, lo primero que necesitamos es importar un *Sistema de Gestión de Bases de Datos Relacionales*, o **Relational Database Management System(RDBMS)**. Un RDBMS es un software utilizado para crear, gestionar y mantener bases de datos relacionales, los más utilizados serían SQLite, MySQL o PostgreSQL.

Pero el RDBMS por si solo no nos permite hacer mucha cosa, por eso existen los **motores de bases de datos**. Estos son softwares que se encargan de crear, leer, actualizar y eliminar registros del RDBMS. Para poder crear un motor de bases de datos podemos hacerlo de la siguiente forma:

```python

from sqlalchemy import create_engine

engine = create_engine('sqlite:///Northwind.sqlite')
```

- `sqlalchemy`: Es el paquete **SQLAlchemy** del que podemos extraer la función que nos interesa, que sería `create_engine`.

- `create_engine('sqlite:///Northwind.sqlite')`: Indicamos que creamos un motor de bases de datos que conectará con la base de datos `sqlite:///Northwind.sqlite`. Es importante matizar que le estamos dando dos tipos de datos en está cadena:

    - `sqlite`: Le indicamos el **RDBMS** de la base de datos que pretendemos manipular.
    - `..:///Northwind.sqlite`: Le indicamos el nombre y la ruta de la base de datos a la que debe conectarse.

Importante recordar que si no sabemos el nombre de las tablas que contienen información podemos ejecutar el siguiente fragmento:

```python
table_names = engine.table_names()

print(table_names) # ['Categorias', 'Clientes', `Pedidos`, `Empleados`, ...]
```

#### 3.2) **<ins>Consultas en Bases de Datos Relacionales</ins>**:
Como hemos visto, el procedimiento para podernos conectar a una base de datos y hacer consultas, sería el siguiente:

1) Importar los paquetes, y funciones, necesarios.
2) Crear el motor de la base de datos.
3) Conectarnos al motor.
4) Consultar la base de datos.
5) Guardar los resultados en un DataFrame.
6) Cerrar la conexión.

Un ejemplo visual puede ser más ilustrativo:

```python

#1)
from sqlalchemy import create_engine
import pandas as pd

#2)
engine = create_engine('sqlite:///Logistica.sqlite')

#3)
con = engine.connect() #Método para conectarnos al motor

#4)
rs = con.execute("SELECT * FROM Pedidos") #Método para ejecutar la consulta

#5)
df = pd.DataFrame(rs.fetchall()) #Transferimos todos los datos al DataFrame

df.columns = rs.keys() #Esto nos permite asignar el mismo nombre de las columnas de BD en el DataFrame

#6)
con.close() #Cerramos
```

Teniendo en cuenta los diferentes métodos para poder conectarnos y ejecutar consultar, lo interesante en ese punto es cómo el motor se comunica con la librería de Pandas. 

* `rs.fetchall()`: Recuperamos todas las filas de la ejecución de la consulta. Combinando esto con la función `pd.DataFrame(...)` podemos transformar lo obtenido en un objeto DataFrame con la información consultada.

**Pequeño truco:** Si queremos despreocuparnos del hecho de tener que cerrar el motor de la base de datos, podemos utilizar el método `with`:

```python

with engine.connect() as con:
    ...
    rs = con.execute('SELECT * FROM Pedidos ORDER BY Fecha_pedido')
    df = pd.DataFrame(rs.fetchmany(size=5)) #Solo importamos 5 registros

```

#### 3.3) **<ins>Consultar bases de datos con Pandas</ins>**:
Despues de crear un motor de bases de datos, hemos obtenido los resultados de consultas utilizando múltiples líneas de código. Pandas, permite hacer exactamente lo mismo en una única línea:

```python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///Logistica.sqlite')

df = pd.read_sql_query('SELECT * FROM Pedidos ORDER BY Fecha_pedido', engine)
```

Para generar el mismo DataFrame que teniamos en los ejemplos anteriores, hemos tenido que introducir diferentes argumentos a la función `pd.read_sql_query(...)`:
    
* ``SELECT * FROM Pedidos ORDER BY Fecha_pedido``:  Sería la sentencia que queremos ejecutar.

* ``engine``: El motor sobre el que ejecutaremos la sentencia.

#### 3.4) **<ins>JOINing tablas</ins>**:

En inglés, **JOIN**, significa juntar. Entendiendo esto, y dado que la ventaja principal de las bases de datos relacionales es el hecho de la poder correlacionar diferentes tablas, podemos con una sentencia como la siguiente:

```python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///Logistica.sqlite')

df = pd.read_sql_query('SELECT NPedidos, IdCliente FROM Pedidos INNER JOIN Clientes on Pedidos.IdCliente = Clientes.IdCliente', engine)
```

Con **INNER JOIN** lo que hacemos es importar otra tabla para poder referenciarla dentro de la sentencia SQL que ejecutamos.