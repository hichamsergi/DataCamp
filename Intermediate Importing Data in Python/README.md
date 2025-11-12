# 📘 Intermediate Importing Data in Python

---

## 1. Descripción

En este capítulo aprenderás

---

## 2. Índice

1. [Importación de datos desde Internet](#capítulo-1-importación-de-datos-desde-internet)
    - [De remoto a local, o solo remoto?](#11-de-remoto-a-local-o-solo-remoto)
    - [URLs y HTTP](#12-urls-y-http)
    - [Rastreando la web](#13-rastreando-la-web)
2. [Interactuar con API para importar datos desde la web](#capítulo-2-interactuar-con-api-para-importar-datos-desde-la-web)
3. []()
4. []()

---

## 3. Apuntes

### Capítulo 1: **<ins>Importación de datos desde Internet</ins>**

#### 1.1) **<ins>De remoto a local, o solo remoto?</ins>**:
Si bien anteriormente hemos aprendido a importar datos desde documentos locales, como archivos *pickle*, *CSV* o *MATLAB*, puede haber veces donde necesitemos importar datos directamente desde internet.

Para poder extraer información desde las páginas web que nos interesen, como ya es habitual, lo podemos hacer a través de un paquete. El paquete que nos ayudará en este caso es `urllib.requests`, que nos permitirá extraer información de internet a traves de *URLs*.

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

#De la hoja '1700' mostramos algunos datos
print(xls['1700'].head())
```

#### 1.2) **<ins>URLs y HTTP</ins>**:
Si bien ya hemos definido lo que es una URL, hace falta entender que realmente es un recurso en web. Por lo tanto al indicar una URL, en vez de especificar una ruta local, lo que hacemos es indicar una ruta para poder acceder a traves de internet a dicho recurso.

Hemos utilizado referencias de rutas *web*, pero también podemos hacerlo para recursos almacenados en servidores *FTP*. Por lo tanto, podemos entender un poco mejor los ejemplos que dabamos antes donde habia una URL:

    https://assets.datacamp.com/course/importing_data_into_r/latitude.xls

- `https://`: Consisten en el identificador del protocolo que se va a utilizar para conectarse. Podemos llegar a indicar `ftp`, en el caso de que necesitemos conectarnos a traves de dicho protoloco al recurso en red.

- `assets.datacamp.com/course/importing_data_into_r/latitude.xls`: Ruta del recurso en red al que vamos a acceder.

Dado que el concepto de ruta es fácilmente comprensible, podemos concentrarnos en el del protocolo. **HTTP**, *HyperText Transfer Protocol*, es el protocolo que utiliza la web para poder transmitir información. Por lo tanto, cada vez que accedemos a una página web lo que hacemos es lanzar una **petición HTTP** al recurso, en concreto una petición **GET**.

Ahora podemos entender cuando en los ejemplos anteriores utilizabamos la función `urlretrieve`, del paquete `urllib.requests`, para lanzar lanzar una petición GET contra la URL y así poder descargar el recurso en red. Pero las peticiones **GET** las podemos utilizar para leer la web, en vez de descargar recursos:

```python
from urllib.request import urlopen, Request

url = 'https://www.wikipedia.org'


#Lanzamos la petición GET a la URL
request = Request(url)


#Abrimos la información retornada por la petición a la URL como si fuera un archivo
response = urlopen(request)

#Leemos dicha información, transformandola en una cadena de texto
html = response.read()

#Cerramos la URL como un archivo normal y corriente
response.close()
```

En el ejemplo anterior, lanzamos la petición GET contra la URL y esta nos contesta con el contenido de dicha pagina web, en **formato HTML**. Lo que nos retorna lo interpretamos como un archivo y es por eso que lo abrimos, leemos y cerramos.

Como siempre, hay formas mas simples y rápidas de hacer lo que acabamos de aprender, y se puede hacer con uno de los paquetes más utilizados y antiguos de Python, `Requests`. Este paquete nos permite simplificar y adaptar a Python todo lo relativo a las peticiones **HTTP**:

```python
import requests

url = 'https://www.wikipedia.org'

r = requests.get(url) #Envia la solcitud GET a la URL

text = r.text #Transforma el HTML de respuesta en una cadena
```

Entonces, en menos líneas, leemos la información que nos retorna la petición HTTP y la lamacenamos para poder manejarla.

#### 1.3) **<ins>Rastreando la web</ins>**:
Anteriormente hemos comentado qué, despues de una solicitud, recibimos información en formato HTML. **HTML**, *HyperText Markup Language*, es el código en el que las páginas web estructuran su contenido. Por lo tanto, después de una petición GET, recibiremos toda la información de la página web en dicho formato.

Si bien el contenido que podemos recibir es el total, este puede ser una mezcla de dos tipos diferentes de datos:

- **Estructurados**: Son datos predefinidos, organizados de una forma determinada.

- **No estructurados**: Son datos que ni estan predefinidos ni organizados. Pese a ello, contiene etiquetas que nos indican donde se localizan los encabezados o *hypervínculos*, por ejemplo.

En general, para poder manipular datos HTML estraídos de una web, necesitaremos analizar y extraer datos estructurados de ellos. Para poder realizar esto, utilizaremos el paquete **BeatifulSoup** de Python:

```python

from bs4 import BeautifulSoup
import requests

url = 'https://www.crummy.com/software/BeautifulSoup'

r = requests.get(url)

html_doc = r.text

soup = BeautifulSoup(html_doc)

print(soup.prettify()) # Esto nos mostrará de una forma bonita el HTML extraido
```

Este paquet tiene algunos métodos interesantes que podemos utilizar con el ejemplo anterior:

- `soup.title`: Recogemos el título principal del HTML.

- `soup.get_text()`:Recogemos todo el texto contenido en el HTML.

- `soup.find_all(...)`: Recogemos todos los datos contenidos en la etiqueta HTML que seleccionemos en su interior.

### Capítulo 2: **<ins>Interactuar con API para importar datos desde la web</ins>**
Para poder acceder a datos a traves de la web, hay multiples formas. Ya hemos aprendido como hacerlo mediante peticiones a traves del protocolo HTTP, ahora aprenderemos a como hacerlo a traves de API. **API**, o *Application Programming Interface*, es un conjunto de reglas, protocolos y rutinas, creadas para interactuar entre aplicaciones de software. En la realidad, funcionan como una especie de intermediario entre dos aplicaciones, el solicitante y el proveedor de información.

Como hemos comentado, tanto el que solicita información como el que la provee, se comunican entre ellos a traves de una API. Estas APIs, de forma habitual, suelen intercambiar dicha información en formato de archivo JSON. El formato **JSON**, *JavaScript Object Notation*, se compone de pares **clave-valor** separados por comas, al igual que un diccionario. Este par, a diferencia de los diccionarios, tiene alguna peculiaridad:

- `Clave`: En los archivos JSON, las claves siempre van entre comilladas, siendo entonces un string.

- `Valor`: Los valores, pueden ser cualquier tipo de datos, strings, enteros, matrices e incluso objetos.

En este formato, y bajo estas características, se estructura toda la información de un archivo JSON.

#### 2.1) **<ins>Cargar JSON en Python</ins>**:
En este sentido, pese a que pueda sonar repetitivo, la forma de interpretar los datos contenidos en un JSON es la misma, mediante el metodo `with`. La variante caracteristica de este tipo de formato de documento, es el paquete que necesitamos para poder cargar los datos contenidos, el paquete `json`. Vamos a aprender a utilizarlo:

```python

import json

with open('snakes.json', 'r') as json_file:

    json_data = json.load(json_file) #Cargamos los datos

type(json_data) #Este nos mostrará que es un diccionario: <dic>
```

Hay que fijarse en el hecho de que hemos abierto el archivo en modo lectura, `r`, a diferencia de otro tipo de formatos como el *pickle*, JSON es legible al ojo humano.

Ahora que entendemos mejor como se estructura este tipo de archivos y ya hemos aprendido a cargar uno, vamos a experimentar con el:

```python

for key,value in json_data.items():
    print(key + ': ', value) #Nos mostrará todas las claves + valor que haya
```

#### 2.2) **<ins>Las API y la interacción con la Web</ins>**:
Como ya sabemos lo que es una API, como interactuar con una web, que formato de datos nos exportan y como interpretarlos, ahora podemos ir directamente con ejemplos practicos de casos reales:

```python
import requests

url = 'http://www.omdbapi.com/?t=Hackers'

r = requests.get(url)

json_data = r.json()

print(json_data)
    #{'Response': 'False', 'Error': 'No API key provided.'}
```

En apartados anteriores comentabamos que el retorno de las peticiones GET, a traves del protocolo HTTP, nos retornaba el contenido real del documento. En este caso esperaríamos que fuera un HTML, pero hemos utilizado una función incorporada realmente útil, `r.json()`. Esta nos transformará el HTML que recibamos en un diccionario JSON. 

Ahora bien, si nos fijamos un poco, veremos que la URL es un poco rara. Tiene varias cosas a comentar:

- `../?t=..`: Este conjunto de carácteres le indica a la API que vamos a realizar una consulta.

- `..Hackers`: Es la consulta que realizamos a la API.

Por lo tanto, lo que hemos hecho es consultar a la API *omdbapi* sobre la película *Hackers* de 1995.



### Capítulo 3: **<ins></ins>**
