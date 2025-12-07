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
Como ya Hemos comentado alguna vez, las **API**, o *Application Programming Interface*, son un conjunto de reglas, protocolos y rutinas, creadas para interactuar entre aplicaciones de software. En la realidad, funcionan como intermediarias entre dos aplicaciones, solicitante y proveedor de información.

Las que más nos interesarían, serían las **Web API**, un tipo de API que se comunica a través de Internet utilizando el protocolo **HTTP**. Esto implica que hay un *cliente*, que envía una petición de información a un *servidor*, utilizando Internet como medio. Este le responde y contesta de vuelta. Hay de tres tipos:

- **SOAP**: Emplea un estilo formal, y es comúnmente utilizada en entornos empresariales que requieren una robustez y protocolos estrictos.

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
|*GET*|Leer|Lo mismo de siempre, comprobar el recurso de una URL|
|*POST*|Crear|Añadiríamos un nuevo recurso a la ruta|
|*PUT*|Actualizar|Reemplazamos un recurso preexistente por otro|
|*DELETE*|Eliminar|Eliminamos un recurso de la ruta|

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

#### 1.2) **<ins>Cabeceras y códigos de estado</ins>**:
Dependiendo del tipo de orden que queramos darle al servidor, puede que nos interese saber o interpretar la respuesta que este nos dé. Esta respuesta se indica en un formato de códigos de 3 dígitos:

|TIPO DE CÓDIGO|SIGNIFICADO|USO FRECUENTE|
|--------------|-----------|-------------|
|`1xx`|Respuesta informativa||
|`2xx`|Mensaje de éxito|`200`: La consulta tiene respuesta afirmativa|
|`3xx`|Mensaje de redirección||
|`4xx`|Error del lado del Cliente|`404`: No se encontró el recurso solicitado por el cliente|
|`5xx`|Error del lado del Servidor|`500`: Error interno del servidor|

Ahora bien, el contenido que se solicita, por parte del cliente, y se proporciona, por parte del servidor, se negocia en los encabezados. Este conjunto de información organizada en pares clave-valor, se separa por dos puntos. Vamos a analizar un conjunto de mensajes y sus encabezados:

- Petición del cliente:
```python
GET /users/73 HTTP/1.1

#Encabezado:
Host: datacamp.com
Accept: application/json
```

- Respuesta del servidor:
```python
HTTP/1.1 200 OK #Código de respuesta

#Encabezado:
Content-Type: application/json
Content-Language: en-US
Last-Modified: Wed, 21 Oct 2025 07:28:00 GMT

#Cuerdo del mensaje:
{
    "id": 73,
    "name": "Hicham Varo",
    "age": 25,
    "email": "hicham@datacamp.com"
}
```

En este caso, podemos ver que el cliente envia el encabezado `Accept` con valor `application/json` indicando que puede aceptar respuestas en formato **JSON**.

En respuesta, el servidor envía el encabezado `Content-Type` con valor `application/json`, para que el cliente sepa en que formato le están respondiendo.

Todo esto, podemos integrarlo en nuestros scripts mediante el ya conocido paquete `requests`:
```python
import requests

response = requests.get(
    'https://api.datacamp.com',
    headers={'accept':'application/json'}
)
```

Como podemos ver, cada método HTTP, acepta un parámetro llamado `headers` en el que podemos indicar, en formato diccionario, tantos pares clave-valor como solicitudes queramos enviar al servidor. 

También podemos ver los encabezados de la respuesta de la siguiente forma:
```python
response.headers['content-type'] #'application/json'

response.headers.get('content-type') #'application/json'
```

Utilizando la solicitud anterior, también podemos ver el código HTTP que hemos generado:
```python
response.status_code == 200 #Nos devuelve 'True' si todo ha ido OK

response.status_code == requests.codes.not_found #No necesitamos saber el código HTTP concreto

response.status_code == requests.codes.ok #No necesitamos saber el código HTTP concreto
```

### Capítulo 2: **<ins>Más conceptos de solicitud API</ins>**
Habitualmente, dado que las respuestas de las API contienen datos privados y sensibles, estas requieren algún método de autenticación. Vamos a catalogar algunos métodos de autenticación:

|Método|Facilidad en la implementación|Seguridad|
|------|------------------------------|---------|
|Autenticación básica, user-passwd| 5/5 | 1/5 |
|Token API| 4/5 | 2/5 |
|Autenticación JWT| 3/5 | 4/5 |
|OAuth 2.0| 2/5 | 5/5 |

#### 2.1) **<ins>Autenticación básica</ins>**:
En este caso añadimos una cabecera especifica al encabezado de la solicitud:
```python
GET /users/73 HTTP/1.1

#Encabezado:
Host: datacamp.com
Accept: application/json
Authorization: Basic XXXXXXXXXX
```

Esta cabecera contiene una combinación codificada en **Base64** de nuestro usuario y contraseña. Dado que **Base64** es una algoritmo de codificación bidireccional, cualquiera puede revertir la codificación de los datos, viento el contenido real del mensaje que hemos codificado.

Podemos hacer todo esto utilizando el paquete `requests`:
```python
requests.get('http://api.music-catalog.com', auth=('username', 'password'))
```

`Requests` se encargará de añadir el encabezado al mensaje y codificarlo en **Base64**.

#### 2.2) **<ins>Token API</ins>**:
Esta opación es más interesante que la autenticación básica. Suponiendo que tenemos un token de la API a la que queremos hacer la solicitud, podemos añadirlo de las siguientes formar:

- Añadimos el token de autenticación a la URL a la que queremos acceder, mediante `params`:
```
http://api.music-catalog.com/albums?access_token=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

```python
params={'access_token':'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}

requests.get('http://api.music-catalog.com/albums', params=params)
```

- Utilizamos la cabecera `Authorization` y el método `Bearer` para añadirlo, sería como el token al portador:
```python
headers = {'Authorization': 'Bearer XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}

requests.get('http://api.music-catalog.com/albums', headers=headers)
```

```python
GET /users/73 HTTP/1.1

#Encabezado:
Host: datacamp.com
Accept: application/json
Authorization: Bearer XXXXXXXXXXXXXXXXXXX #Ahora ya no indica 'Basic' sino 'Bearer'
```

