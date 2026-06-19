# 📘 Streamlined Data Ingestion with Pandas

## 1. Índice

1. [Importación de datos de archivos planos](#capítulo-1-importación-de-datos-de-archivos-planos)
2. [Importación de datos de archivos Excel](#capítulo-2-importación-de-datos-de-archivos-excel)
3. [Importación de datos de Bases de Datos](#capítulo-3-importación-de-datos-de-bases-de-datos)
4. [Importación de datos JSON y trabajo con APIs](#capítulo-4-importación-de-datos-json-y-trabajo-con-apis)

------

## 2. Apuntes

### Capítulo 1: **<ins>Importación de datos de archivos planos</ins>**

La función que más hemos utilizado para poder importar datos desde un documento, puede haber sido `.read_csv(...)`. Si bien, la forma más común de utilizarla es para importar documentos de tipo CSV, también se puede utilizar para importar cualquier tipo de archivo plano. Utilizando el argumento `sep="..."`, podemos definir el separador que utilice nuestro documento para poder leer el archivo:

```python
import pandas as pd

tax_data = pd.read_csv(`us_tax_data_2016.tsv`, sep="\t")
```

De todas formas, es comprensible que no necesitemos todo el contenido del *DataFrame*, por lo que debemos saber como limitar la importación de datos para ser más eficientes. Podemos hacerlo con `usecols` de la siguiente forma:

```python
columnas_utiles = ['STATE', 'N1', 'zipcode']

data = pd.read_csv('us_tax_data_2016.csv', usecols=columnas_utiles)
```

De esta forma, solo importamos los datos contenidos en las columnas con los nombres definidos en la lista. 

Pero podemos limitar aun más los datos recogidos, digamos que solo queremos los primeros 1000 registros. `nrows`, nos recogerá los 1000 primeros registros del fichero que le proporcionemos:

```python

data_w_column_names = pd.read_csv('us_tax_data_2016.csv', nrows=1000)
```

Pero `nrows` es especialmente útil cuando se utiliza con us homónimo `skiprows`:

```python

data = pd.read_csv('us_tax_data_2016.csv', 
    nrows=200, 
    skiprows=1000,
    header=None)
```

Así pues, de esta forma recogemos los primeros 200 registros a partir del 1000 registro. Teniendo en cuenta que asumimos que no hay encabezado en las columnas.

Tomemos como ejemplo el dataset anterior, en el que no tenemos nombres de columnas, y contiene 200 registros. Vamos a dar nombre a esas columnas recogiendo el nombre de las columnas del dataset previo:

```python

column_names = list(data_w_column_names) #Atajo para recoger los nombres de las columnas

data = pd.read_csv('us_tax_data_2016.csv', 
    nrows=200, 
    skiprows=1000,
    header=None,
    names=column_names)
```

Como estamos viendo, una de las formas más eficiente de tratar datos con Pandas, es cargarlos correctamente y de forma selectiva. Esto, muchas veces pasa por indicar el tipo de dato que se va a proporcionar en una determinada columna, de esta forma evitamos errores de tipología de dato:

```python

df = pd.read_csv("us_tax_data_2019.csv", dtype={"zipcode": str})
```

Así pues, cuando procesamos la columna **zipcode** indicamos que ese dato es un string. De esta forma forma datos como los ceros situados a la izquierda no se verán eliminados.

Pero rellenar la información que consideramos errónea por valores faltantes, *NaN*, puede ser útil cuando nos encontramos con datos como un *0* en columnas como el código postal:

```python
df = pd.read_csv("us_tax_data_2019.csv", na_values={"zipcode": 0})
```

Mediante el argumento `na_values`, indicamos que queremos rellenar los valores que sean como *NaN*. De esta manera evitamos que un dato erróneo sea considerado como correcto o valido.


Pero un *DataFrame* es muy grande y puede contener errores múltiples que pueden pasarse por alto. Por eso, indicar lo que queremos que haga Pandas al procesarlos es imprescindible para evitar que los scripts se vean interrumpidos:

```python
df = pd.read_csv("us_tax_data_2019.csv", 
        error_bad_lines=False,
        warn_bad_lines=True)
```

En estos casos, los siguientes argumentos indican cosas diferentes:

* `error_bad_lines`: Omitimos las líneas incorrectas, cargamos el resto. Básicamente nos pregunta si queremos añadir las líneas erróneas, y nosotros respondemos `False`, indicando NO, o `True`, indicando si y generando los errores esperados.

* `warn_bad_lines`: Mostramos un mensages cuando haya una línea incorrecta. Por lo que cada vez que encuentre una nos lo notificará. 

### Capítulo 2: **<ins>Importación de datos de archivos Excel</ins>**

Es muy común que en los archivos Excel haya más de una hoja, cada una con los datos pertinentes, pero `read_excel` únicamente importa la primera si no le indicamos lo contrario. Es por eso que Pandas ofrece la posibilidad de indicar la hoja de la que queremos recoger los datos.

Utilizando el argumento `sheet_name`, dentro de `read_excel()`, podemos indicar no solo el nombre de la hoja que queremos recoger, sino también el índice que esta ocupa, o una lista de ellos para poder importar varias hojas.

```python
data = pd.read_excel('fcc_data.xlsx',
                        sheet_name=1)

data = pd.read_excel('fcc_data.xlsx',
                        sheet_name='2026')      
```

Pero, *como podemos hacer para importar todas las hojas?*. Es apregunta, se responde facilmente y utilizando el mismo argumento que acabamos de aprender, `sheet_name=None`:

```python
data = pd.read_excel('fcc_data.xlsx',
                        sheet_name=None)  
```

El problema de utilizar este método es que realmente no importamos un *DataFrame* con toda la infromación. Lo que realmente recibimos es un diccionario ordenado con pares clave valor que corresponden a el nombre de la hoja, como clave, y un *DataFrame*, como valor.

Si queremos organizarlo todo en un mismo *DataFrame* deberemos realizar algun paso extra:

```python

todas_hojas = pd.DataFrame() #DataFrame vacio

for sheet_name, data_f in data.items():

    data_f["Year"] = sheet_name

    todas_hojas = pd.concat([todas_hojas, data_f])
```

Pero en el capítulo anterior hemos aprendido a como indicar que queremos importar un determinado tipo de datos, con `dtype`. Pero los datos booleanos requieren una mencion especial, no por el hecho de ser binarios, o **True** o **False**, sino por el hecho de que algunas veces podemos verlos representados de diferentes formas, como **Yes** o **No**.

Este tipo de casos, en los que no se indica explicitamente **True** o **False**, son en los que nos vamos a concentrar. Con el argumento `true_values`, podemos indicarle los valores que consideremos como **True**, proporcionandole una lista:

```python
data = pd.read_excel('fcc_data.xlsx',
                        true_values=['Yes'],
                        false_values=['No'])  
```
Pese a ello, la conversión debe valorarse y considerar las posibles implicaciones de la conversión, dado que las operaciones que se lleven a cabo sobre el dataset basadas en datos booleanos pueden tener un impacto no deseado.

Pero como ya sabemos, los datos booleanos no son los más difíciles de gestionar, sino que los son las fechas. Así pues, cuando queremos especificar que una columna contiene fechas, no lo hacemos con `dtype` sino con un argumento especial, `parse_dates`:

```python

date_cols = ["Columna_fecha1", "Columna_fecha2"]

data = pd.read_excel('fcc_data.xlsx',
                        parse_dates=date_cols)
```

De todas forma, este método solo funciona si Pandas reconoce el formato de la fecha. Si este formato no pertenece a un estándar, deberemos importar los datos utilizando `parse_dates` y posteriormente utilizar la función `.to_datetime()`. Esta función es muy útil, y funcional, ya que podemos indicar el formato específico de nuestra fecha no estandarizada:

```python

formato_fecha = "%m%d%Y %H:%M:%S"

date2_standarize = pd.to_datetime('fcc_data.xlsx',
                        format=formato_fecha)
```

* `%Y`: Indicando año, en formato de 4 dígitos.

* `%m`: Mes, en formato de 2 dígitos.

* `%d`: Día, en formato de 2 dígitos.

* `%H`: Hora, en formato de 24 horas.

* `%M`: Minutos, en formato de 2 dígitos.

* `%S`: Segundos, en formato de 2 dígitos.

### Capítulo 3: **<ins>Importación de datos de Bases de Datos</ins>**

Pero la ingesta de datos no solo se puede dar por los diferentes tipos de archivos que ya hemos comentado. Si tenemos una base de datos a la que podamos realizar consultas, podemos hacerlo tanto con Pandas como con una libreria ya conocida, `sqlalchemy`. Esta libreria nos permite generar el motor a través del cual lanzaremos nuestras consultas:

```python
# Importamos la función create_engine() de la libreria sqlalchemy
from sqlalchemy import create_engine

# Creamos el motor de la base de datos
engine = create_engine('sqlite:///data.db')
```

Ahora bien, este es solo el primer paso. `sqlalchemy` solo nos permite conectarnos a la base de datos, cuando ya hemos podido acceder, toca utilizar Pandas:

```python
# Load hpd311calls without any SQL
hpd_calls = pd.read_sql("SELECT * FROM hpd311calls", engine)
```

Como se puede ver, `.read_sql(...)` nos permite lanzar una consulta SQL, mediante Pandas. Lo que recibimos de esta función es un *DataFrame* con los datos solicitados. Pero podemos complicar más el proceso, haciendo más compleja nuestras sonsultas de SQL:

```python
# Obtener date, tmax, y tmin de weather
query = """
SELECT date, 
       tmax, 
       tmin
  FROM weather;
"""

# Obtenemos todo de hpd311calls cuando el tipo de queja corresponda a 'SAFETY'
query = """
SELECT *
FROM hpd311calls
WHERE 'SAFETY' == complaint_type;
"""

# Recoge los registros que tengan temps <= 32 o snow >= 1
query = """
SELECT *
  FROM weather
  WHERE tmax <= 32
  OR snow >= 1;
"""

# Obtenemos registros únicos de la combinación de borough y complaint_type
query = """
SELECT DISTINCT borough, 
       complaint_type
  FROM hpd311calls;
"""
```

Como podemos ver, hay muchas formas de complicarnos la vida y hacer extremadamente complejas nuestras consultas. Y como Python, SQL también tiene sus funciones integradas y nos permite agrupar registros de tal forma que podemos rizar el rizo aun más:

```python
# Obtener un recuento de todas las quejas agrupadas por su tipo
query = """
SELECT complaint_type, 
     COUNT(*)
  FROM hpd311calls
  GROUP BY complaint_type;
"""

# 
query = """
SELECT month, 
        MAX(tmax), 
        MIN(tmin),
        SUM(prcp)
  FROM weather 
 GROUP BY month;
"""
```

Pero lo más interesante puede ser la forma de mezclar tablas, que para SQL corresponderían a diferentes *DataFrames* si queremos entenderlo a través de Pandas. Para hacerlo, necesitamos importar la tablas externa de la que recogeremos o combinaremos datos. Para hacerlo, utilizaremos `JOIN` y especificamos mediante una sentencia lógica como mezclaremos los datos:

```python
# Query to join weather to call records by date columns
query = """
SELECT * 
  FROM hpd311calls
  JOIN weather 
  ON hpd311calls.created_date = weather.date;
"""

# Query to get hpd311calls and precipitation values
query = """
SELECT hpd311calls.*, weather.prcp
  FROM hpd311calls
  JOIN weather
  ON hpd311calls.created_date = weather.date;"""

# Modify query to join tmax and tmin from weather by date
query = """
SELECT hpd311calls.created_date, 
	   COUNT(*), 
       weather.tmax,
       weather.tmin
  FROM hpd311calls 
       JOIN weather
       ON hpd311calls.created_date = weather.date
 WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER' 
 GROUP BY hpd311calls.created_date;
 """
```

### Capítulo 4: **<ins>Importación de datos JSON y trabajo con APIs</ins>**

Y para finalizar, el último método de importación de datos, **JSON** y las **API**. De la misma forma que los ejemplos anteriores, vamos a utilizar Pandas para poder manipular y leer datos en dicho formato. 

Pero tenemos que aplicar un poco lo que ya conociamos, y es que Pandas en realidad no es tan listo o intuitivo como nos pensado. Para poder leer correctamente ciertos datos, debemos entender que dependiendo de la orientación de nuestros datos JSON, y es por eso que merece la pena explicar los dos tipos de orientación:

* `orient='index'`: Esta correspondería al clasico diccionario anidado, en el que tenemos una clave indice que corresponde al indice del registro y el diccionario anidado, al nombre de la columna y el valor que queremos cargar en esta.

* `orient='split'`: Esta correspondería a tres claves, `columns`, `index` y `data`, que contienen listas con la información a cargar en cada una de los apartados que describen.

```python

df = pd.read_json("dhs_report_reformatted.json",
                      orient='split')
```

Ahora bien, para poder recibir la infromación que nos hace falta de los archivos JSON, debemos realizar una solicitud mediante APIs. Estas solicitudes requieren de una vieja conocida, la libreria `requests`, y para poder solicitar utilizaremos la siguiente función:

```python

requested_data = requests.get(url_string,
                              params=...,
                              headers=...)
```

En este caso, asumimos que el primer argumento de la función es la URL de la que pretendemos recibir información. Pero el resto de argumentos nos sirven para lo siguiente:

* `params`: Toma un diccionario, con pares clave-valor que funcionarán como los parámetros de consulta para la API.

* `headers`: Toma un diccionario, con pares clave-valor que funcionarán como valores customizables de los encabezados HTTP que mandamos.

En definitiva, lo que recibimos de una consulta es un objeto `response`. Pero este objeto puede contener información que no nos es útil. Para recibir la información en formato JSON utilizaremos `response_data.json()`. Y como nuestro objetivo es convertir esa respuesta en un *DataFrame*, generaremos uno vacio con `pd.DataFrame()`, para que no dé un error al utilizar la función `pd.read_json(...)`:

```python

responsed_data = requested_data.json()

final_df = pd.DataFrame(responsed_data["businesses"])
```

Ahora que sabemos como recoger información de diferentes fuentes, debemos saber como combinar entre si la información que acabamos de recoger. Esto podemos hacerlo con la función `.concat([..., ...])` de Pandas, que conctatenará los diferentes elementos proporcionados en la lista que le indiquemos:

```python
df1 = pd.DataFrame({"Nombre": ["Ana"]}, index=[0])
df2 = pd.DataFrame({"Nombre": ["Eva"]}, index=[0])  # ¡Mismo índice!

#Ejemplo simple con error
concator = pd.concat([df1, df2]) 
```

Es importante comentar que no es tan fácil como concatenar *DataFrames*, tenemos que tenre cuidado con elementos como los números de índices que Pandas genera en las filas. También podemos hacerlo con el argumento `ignore_index=True`:

```python

# BIEN: Resetea el contador de filas de arriba a abajo
bien = pd.concat([df1, df2], ignore_index=True)
# Resultado: filas indexadas limpiamente como 0 y 1.
```

Otra forma de mezclar información de diferentes *DataFrames* es utilizando `.merge(..., ...)` que nos permite hacer operaciones o consultas en dos *DataFrames* simultaneamente. Funciona de froma parecida a los **JOIN** de *SQL*, pero con algunas variaciones:

```python
ventas = pd.DataFrame({
    "id_partido": [101, 102],
    "entradas_vendidas": [12000, 8500]
})

# Tabla 2: Datos de los partidos
partidos = pd.DataFrame({
    "id_partido": [101, 102],
    "rival": ["Barça", "Real Madrid"]
})

# Fusionamos usando 'id_partido' como puente
partidos_completos = ventas.merge(partidos, on="id_partido")
```

Y como en *SQL* hay una forma más compleja de utilizar *merge*:

```python

merged = call_counts.merge(weather,
                            left_on='created_date',
                            right_on='date')
```
