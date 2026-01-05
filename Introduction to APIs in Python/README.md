# 📘 Introduction to APIs in Python

## 1. Descripción

-------

## 2. Índice

1. [Hacer peticiones a la API con Python](#capítulo-1-hacer-peticiones-a-la-api-con-python)
    - [Anatomía básica de una petición API](#11-anatomía-básica-de-una-petición-api)
    - [Cabeceras y códigos de estado](#12-cabeceras-y-códigos-de-estado)
2. [Más conceptos de solicitud API](#capítulo-2-más-conceptos-de-solicitud-api)
    - [Autenticación básica](#21-autenticación-básica)
    - [Token API](#22-token-api)
3. [Trabajar con datos estructurados](#capítulo-3-trabajar-con-datos-estructurados)
    - [Recibir información JSON](#31-recibir-información-json)
    - [Enviar datos JSON](#32-enviar-datos-json)
4. [Manejo de errores](#capítulo-4-manejo-de-errores)

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

En este caso, podemos ver que el cliente envía el encabezado `Accept` con valor `application/json` indicando que puede aceptar respuestas en formato **JSON**.

En respuesta, el servidor envía el encabezado `Content-Type` con valor `application/json`, para que el cliente sepa en qué formato le están respondiendo.

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
En este caso añadimos una cabecera específica al encabezado de la solicitud:
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
Esta opción es más interesante que la autenticación básica. Suponiendo que tenemos un token de la API a la que queremos hacer la solicitud, podemos añadirlo de las siguientes formar:

- Añadimos el token de autenticación a la URL a la que queremos acceder, mediante `params`, como parámetro de consulta:
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


### Capítulo 3: **<ins>Trabajar con datos estructurados</ins>**
Una vez hecha la solicitud, se transmite la información que el cliente ha solicitado. Dicha información, comúnmente, se hace llegar en formato **JSON**, un viejo conocido. Llamaremos **codificación** a la estructuración de datos en formato JSON para su transmisión, y **decodificación** al proceso inverso.


#### 3.1) **<ins>Recibir información JSON</ins>**:
En Python, el paquete integrado `json` nos permite trabajar libremente en la codificación y decodificación de datos en este formato:
```python
import json

album = {'id': 42, 'title':'Back in Black'} #Diccionario con información

album_2_encode = json.dumps(album) #Codificamos el diccionario anterior en formato JSON

album_2_decode = json.loads(album_2_encode) #Decodificamos el objecto JSON generado
                                            # de esta forma generamos un diccionario de nuevo
```

Pero lo más interesante es cuando mezclamos esto con lo que hemos aprendido sobre las solicitudes API. Vamos a utilizarlo con lo que hacemos con el paquete `requests`:
```python

#Realizamos una petición a la API, solicitando la info en formato JSON:
response = requests.get('http://api.music-catalog.com/lyrics', headers={'accept': 'application/json'})

#Decodificamos la información de forato JSON a un diccionario:
data = response.json()
```

#### 3.2) **<ins>Enviar datos JSON</ins>**:
Si entendemos como funciona lo que implica la codificación y decodificación de información, enviar datos mediante consultas a las APIs utilizando JSON es bastante simple:

```python
import requests

playlist = {'name':'Road Trip', 'genre':'rock', 'private':'true'}

#Añadimos la playlist utilizando JSON:
response = requests.post('http://api.music-catalog.com/playlists', json=playlist)
```

### Capítulo 4: **<ins>Manejo de errores</ins>**
Las API determinan si ha habido algún error en el manejo de las peticiones utilizando los códigos de error `4xx`, para los errores en el cliente, y `5xx`, para los errores en el servidor.

Los errores de tipo `4xx`, habitualmente, implican una solicitud mal hecha, fallo en la autenticación o incluso un encabezado incorrecto. Para solucionarlos, el cliente puede corregir la solicitud y volver a enviar la petición. Errores comunes:

- `401 Unauthorized`: La solicitud se hace a recursos o información protegida. Las credenciales utilizadas son incorrectas.

- `404 Not Found`: Los recursos que se han solicitado no existen, o no se han podido encontrar.

- `429 Too Many Requests`: Se han emitido demasiadas solicitudes en un corto periodo de tiempo.

Los errores de tipo `5xx`, habitualmente, implican un error por el lado del servidor, por lo que se escapa al control del cliente. Normalmente, son causados por una sobrecarga del mismo servidor, una mala configuración del mismo o errores internos. La forma correcta de manejarlos es contactar con el administrador de la API para que este pueda corregirlos. Errores frecuentes:

- `500 Internal Server Error`: El servidor ha tenido algún problema que le imposibilita el hecho de enviarnos la respuesta.

- `502 Bad Gateway`: El servidor API no ha podido alcanzar otro servidor necesario para poder realizar la respuesta.

- `504 Gateway Timeout`: El servidor API no ha recibido respuesta en un tiempo determinado.

Estos errores podemos detectarlos de las siguientes formas en nuestros scripts:
```python
import requests

url = 'http://api.music-catalog.com/album'

r = requests.get(url)

if r.status_code >= 400:
    #Algo ha ido mal

else:
    #Todo ha ido como se espera
```

Teniendo en cuenta que la misma librería `requests` nos genera un error de conexión cuando algo va mal, podemos jugar con los bloques `try-except` para poder manejar los errores:
```python
import requests

from requests.exceptions import ConnectionError

url = 'http://api.music-catalog.com/album'

try:
    r = requests.get(url)
    print(r.status_code)

except ConnectionError as conn_err:
    print(f'Connection Error! {conn_err}')
    print(error)
```

Y aún más, podemos manejar los errores dependiendo del código que nos devuelvan:
```python
import requests

from requests.exceptions import ConnectionError, HTTPError


try:
    r = requests.get('http://api.music-catalog.com/album')

    #Habilitamos la detección de los errores por tipo de código:
    r.raise_for_status()

    print(r.status_code)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
```

Con la opción `r.raise_for_status` cuando ocurra un error, si lo hace, el script generará una excepción por tipo de código HTTP. 

Esto en realidad implica que independientemente del error que ocurra, el error de la petición almacenado en `r.status_code` será filtrado por el bloque `except HTTPError`, devolviéndonos el código de error exacto que haya generado la petición, haciendo más fácil la depuración de nuestro script para poder corregir el error en la petición. 