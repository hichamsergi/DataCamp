# 📘 Intermediate Importing Data in Python

---

## 1. Descripción

En este capítulo aprenderás

---

## 2. Índice

1. [Importación de datos desde Internet](#capítulo-1-importación-de-datos-desde-internet)
2. []()
3. []()
4. []()

---

## 3. Apuntes

### Capítulo 1: **<ins>Importación de datos desde Internet</ins>**
Si bien anteriormente hemos aprendido a importar datos desde documentos locales, como archivos *pickle*, *CSV* o *MATLAB*, puede haber veces donde necesitemos importar datos directamente desde internet.

Para poder extraer información desde las páginas web que nos interesen, como ya es habitual, lo podemos hacer a través de un paquete. El paquete que nos ayudará en este caso es `urllib`, que nos permitirá extraer información de internet a traves de *URLs*.

Una **URL**, *Uniform Resource Locator*, pueden contener información que podemos extraer utilizando el paquete mencionado anteriormente:

```python
from urllib.request import urlretrieve 

url = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-white.csv'

urlretrive(url,'winequality-white.csv') 
```
El contenido de la URL lo almacenamos localmente en el documento *winequality-white.csv*, accediendo al recurso a traves de internet.

Ahora bien, si ni siquiera queremos mantener la información de forma local podemos jugar con nuestro estimado paquete **Pandas**:

```python
import pandas as pd

url = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

df = pd.read_csv(url, sep=';') #Indicamos que el separador es un ';'
```

De esta forma, en vez de indicar la ruta del archivo local, le estamos especificando que debe de leer el archivo CSV a traves de la URL.

Tomando los ejemplos anteriores nada nos impide hacer los mismo, pero con archivos de tipo `xls`:

```python
import pandas as pd

url = 'https://assets.datacamp.com/course/importing_data_into_r/latitude.xls'

#Leemos todas las hojas del Excel:
xls = pd.read_excel(url, sheet_name=None)

#Mostramos los nombres de las hojas:
print(xls.keys())

#De la hoja '1700 mostramos algunos datos'
print(xls['1700'].head())
```

#### 1.1) **<ins>URLs y HTTP</ins>**:
Si bien ya hemos definido lo que es una URL, hace falta entender que realmente lo qué se indica en realidad cuando especificamos una es un recurso en web. Por lo tanto al indicar una URL, en vez de especificar una ruta local, lo que hacemos es indicar una ruta para poder acceder a traves de internet a un recurso.

Hemos utilizado referencias de rutas *web*, pero también podemos hacerlo para recursos almacenados en servidores *FTP*. Por lo tanto, podemos entender un poco mejor los ejemplos que dabamos antes donde habia una URL:

    https://assets.datacamp.com/course/importing_data_into_r/latitude.xls

- `https://`: Consisten en el identificador del protocolo que se va a utilizar para conectarse. Podemos llegar a indicar `ftp`, en el caso de que necesitemos conectarnos a traves de dicho protoloco al recurso en red.

- `assets.datacamp.com/course/importing_data_into_r/latitude.xls`: Ruta del recurso en red al que vamos a acceder.

Dado que el concepto de ruta es fácilmente comprensible, podemos concentrarnos en el del protocolo. **HTTP**, *HyperText Transfer Protocol*, es el protocolo que utiliza la web para poder transmitir información. Por lo tanto, cada vez que accedemos a una página web lo que hacemos es lanzar una **petición HTTP**, en concreto una petición **GET**. Así podemos entender, que en los ejemplos anteriores, cuando utilizamos la función `urlretrieve` lo que hacemos en realidad es lanzar una petición GET contra la URL especificada.

```python
import requests

url = 'https://www.wikipedia.org'

r = requests.get(url) #Envia la solcitud GET a la URL

text = r.text #Transforma el HTML de respuesta en una cadena
```

```python
from urllib.request import urlopen, Request

url = 'https://www.wikipedia.org'

request = Request(url)

response = urlopen(request) #Abrimos la URL como si fuera un archivo

html = response.read()

response.close() #Cerramos la URL
```

### Capítulo 2: **<ins></ins>**

### Capítulo 3: **<ins></ins>**
