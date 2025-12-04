# 📘 Introduction to APIs in Python

## 1. Descripción

-------

## 2. Índice

1. 
2. 
3. 

-----

## 3. Apuntes

### Capítulo 1: **<ins>Hacer peticiones a la API con Python</ins>**
Com ya Hemos comentado alguna vez las **API**, o *Application Programming Interface*, son un conjunto de reglas, protocolos y rutinas, creadas para interactuar entre aplicaciones de software. En la realidad, funcionan como intermediarias entre dos aplicaciones, solicitante y proveedor de información.

Las que más nos interesarían, serían las **Web API**, un tipo de API que se comunica a través de Internet utilizando el protocolo **HTTP**. Esto implica que hay un *cliente*, que envia una petición de información a un *servidor*, utilizando Internet como medio. Este, le responde y contesta de vuelta. Hay de tres tipos:

- **SOAP**: Emplea un estilo formal, y es comunmente utilizada en entornos empresariales que requieren una robustez y protocolos estrictos.

- **REST**: Es el más popular y común, conocido por su simplicidad, escalabilidad y facilidad de integración.

- **GraphQL**: Tiene un enfoque más sofisticado, centrado en la precisión y recuperación flexible de datos y optimizando el rendimiento.

Para interactuar con cualquiera de ellas utilizaremos dos de las librerías que ya conocemos, **urllib** y **requests**. Vamos a refrescarlas brevemente:
| urllib | requests |
|-------|----------|
| Módulo potente nativo de Python | Más directa, no necesita tantos pasos como urllib |
|Sacrificamos simplicidad| Mucho más fácil de utilizar |

* **urlib**:
```python
from urllib.request import urlopen
api = "http://api.music-catalog.com/"

with urlopen(api) as response:

    data = response.read()
    string = data.decode()

    print(string)
```

* **requests**:

```python
import requests
api = "http://api.music-catalog.com/"

response = requests.get(api)

print(response.text)
```

Como se puede comprender a simple vista, al final el paquete requests es mucho más directo y utiliza menos líneas de código.

#### 1.1) **<ins>Anatomía básica de una petición API</ins>**:
Como es de suponer, de las cosas más importantes a la hora de trabajar con APIs, es la URL. Ya sabemos lo que significan, y entendemos que es una ruta a un recurso, pero hace falta desgranar las partes de la URL:

`http://` `350.5th-ave.com` `:80` `/unit/243` `?floor=77`

- `http://`: Protocolo utilizado para el acceso a los datos.

- `350.5th-ave.com`: Dominio donde se aloja la información, el servidor que la contiene.

- `:80`: Puerto de acceso.

- `/unit/243`: Ruta local dentro del dominio.

- `?floor=77`: Consulta que haremos al recurso.

Habiendo aprendido que compone a una API, podríamos decir que la parte más relevante sería la consulta final. Podemos implementar consultas utilizando la librería `requests`:

```python
import requests

response = requests.get('http://350.5th-ave.com/unit/243') #URL simple
```

Ahora bien, dentro de los métodos *HTTP*, como `GET`, podemos utilizar *requests* para proporcionar parámetros de consulta como argumentos adicionales. Esto mismo podemos hacerlo con `params=...`, un argumento al que le podemos proporcionar diccionarios, con pares clave-valor, que será interpretado como parámetros de consulta al recurso:

```python
#Establecemos los parámetros
query_params = {'floor':77, 'elevator':True}

#Añadimos parámetros a la URL:
response = requests.get('http://350.5th-ave.com/unit/243', params=query_params)
```

Pero, dependiendo del tipo de método *HTTP* podemos hacer diferentes cosas, por eso es importante conocerlos todos:

|Método|Acción|Descripción|
|------|------|-----------|
|*GET*|Leer|Lo mismo de siempre, comprobar el contenido de un buzón sin sacar las cartas|
|*POST*|Crear|Añadiríamos una nueva carta al buzón|
|*PUT*|Actualizar|Remplazamos una carta preexistente por otra|
|*DELETE*|Eliminar|Eliminamos una carta del buzón|

Pongamos un ejemplo práctico:
```python
#GET, utilizando identificadores únicos:
response = requests.get('http://350.5th-ave.com/unit/243/{3}') #En este caso accederemos al recurso ID=3 de la ruta indicada

#POST, tenemos que añadir datos adicionales a nuestra petición:
response = requests.post('http://350.5th-ave.com/unit/243', data={"clave":"valor"})

#PUT, tenemos que añadir datos adicionales a nuestra petición:
response = requests.put('http://350.5th-ave.com/unit/243', data={"clave":"valor"})

#DELETE, simplemente indicamos la ruta a eliminar:
response = requests.delete('http://350.5th-ave.com/unit/243')
```

Como se puede ver, para los métodos `POST` y `PUT`, es necesario indicar información adicional además de la URL simple. En este caso, `data` es la forma de hacerlo, y es muy similar a `params` donde se le transmite mediante diccionarios. 


#### 1.2) **<ins></ins>**:

#### 1.3) **<ins></ins>**:

### Capítulo 2: **<ins>Más conceptos de solicitud API</ins>**
