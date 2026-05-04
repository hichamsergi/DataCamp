# 📘 Nombre del capítulo

## 1. Descripción

## 2. Índice

1. [Título del apartado 1](#capítulo-1-título-del-apartado-1)

2. [Título del apartado 2](#capítulo-2-título-del-apartado-2)

3. [Título del apartado 3](#capítulo-3-título-del-apartado-3)

---

## 3. Apuntes

### Capítulo 1: **<ins>Dificultades habituales con los datos</ins>**

La parte del trabajo más importante de un Data Engineer, es generar datos de calidad. Proporcionar información de calidad en las condiciones correctas es esencial para que, por ejemplo, un Data Scientist pueda elaborar predicciones correctamente.

A la hora de entregar correctamente estos datos, los errores más básicos que podemos llegar a cometer estarían relacionados con el tipo de dato que contiene una columna. Digamos que, por algun motivo, los registros de la columna de *Revenue* en un DataFrame de ventas son de tipo string y queremos convertirlos a enteros:

```python
ventas["Revenue"] = ventas["Revenue"].astype('int')
```

Con la función `.astype(..)` podemos convertir un tipo de dato en otro, siempre y cuando este "sea convertible". Es decir, podemos convertir un '1' en entero, pero no podemos converir '1\$' a entero, ya que al contener el simbolo '\$' trataríamos una cadena string con un simbolo no convertible a entero.

El ejemplo anterior es especialmente útil. Imaginemos que como el valor de la columna 'Revenue' contiene valores numéricos seguidos del simbolo '$', queremos eliminar el simbolo para convertir los registros de la columna en enteros.

```python
ventas["Revenue"] = sales["Revenue"].str.strip('$')
```

Como podemos ver, para poder utilitzar la función `strip('...')` primero debemos de indicarle el tipo de dato, string, para poder eliminar el simbolo de todos los registros.

Para verificar que hemos cambiado el tipo de dato, podemos utilizar la función `assert`. Esta función nos permite realizar una comprobación de una operación booleana, retornando un `AssertionError` en caso de que esta devuelva *False*:

```python
assert ventas["Revenue"].dtype == 'int'
```

También es importante saber que debido a la amplia variedad de formatos que puede haber en las fechas, estas son un caso especialmente importante a tener en cuenta.

Pueden darse casos en los que las fechas se presenten como cadenas *string*. Debemos de tener cuidado en como lo convertimos a un *datatype* en formato fecha:

```python
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date']).dt.date
```

Lo primero que hemos hecho, ha sido utilizar la función `to_datetime` de Pandas para indicar que la columna `ride_date` corresponde a un *datetype* de fecha. Una vez lo tenemos, especificamos el tipo de dato, `dt`, y luego le indicamos que parte de esa fecha es la que nos vamos a quedar. En el ejemplo anterior indicamos `date`, que correspondería a la parte de la fecha que equivale a `YYYY-MM-DD`. Pese a todo, hay multiples formatos y podemos recoger diferente información en función de nuestras encesidades. 

Ahora podemos asumir que nuestro *dataset* contiene la información en el formato que nos interesa. El paso lógico, podría ser aprender a filtrarla y quedarnos únicamente con los registros que nos interesan:

```python
movies = movies[movies["avg_rating"] <= 5]
```

De esta forma, reasignamos el valor del *DataFrame* inicial al valor de el mismo con el promedio de rating(`avg_rating`) inferior o igual a `5`.

Otro métodos para poder realizar un cribaje de registros no necesarios puede ser con el método `.drop()`:

```python

movies.drop(movies[movies["avg_rating"] <= 5].index, inplace = True)
```
Vamos a descomponer la función anterior para entenderla mejor:

* `movies.drop(...)`: Indicamos el *DataFrame* del que vamos a eliminar los registros, seguido de la función `.drop()`.

* `movies[movies["avg_rating"] <= 5].index`: Recogemos únicamente los indices de los registros que cumplan con la condición indicada.

* `inplace = True`: Modificamos el *DataFrame* original. 

Entendiendo lo previo, podemos saber por lo tanto lo que pretende hacer la siguiente función:

```python
movies.loc[movies[movies["avg_rating"] <= 5], 'avg_rating'] = 5
```

Modificamos el *DataFrame* para que contenga únicamente el promedio de rating de los registros que tienen un promedio de rating inferior o igual a 5.

Ahora que ya sabemos filtrar para eliminar registros que no cumplen con los parametros que queramos, podemos aprender a como eliminar datos duplicados. Los datos duplicados son otro de los grandes problemas que podemos llegar a tener, ya que implica tener en cuenta la misma información 2 veces. Para esta tarea utilizaremos dos funciones que nos serán de gran ayuda:

* `df.duplicated(...)`: Funciona como un buscador de duplicados, no elimina directamente, sino que señala duplicados.

* `df.drop_duplicates(...)`: Es el ejecutor de la eliminación de duplicados, realmente se encarga de eliminar los registros que sean identicos a otros.

Poder saber si se trata de un registro completamente duplicado, o simplemente de uno con un dato duplicado, es algo que no podemos pasar por alto y es muy importante. En ambas funciones podemos utilizar los siguientes atributos que nos ayudarán a poder identificar si un duplicado es parcial o completo:

* `(subset=['...','...'], ...)`: Con `subset` podemos identificar que columnas queremos analizar para poder focalizar la busqueda de duplicados.

* `(..., keep=False)`: Podemos indicarle si queremos conservar alguno de los duplicados encontrados. Hay diferentes posibles argumentos, False, `first` y `last`. Con el primero eliminamos todos los duplicados, con los dos siguientes, dariamos por valido el primero o el último registro duplicado.


### Capítulo 2: **<ins>Problemas de texto y datos categóricos</ins>**
Como ya hemos trabajado con *DataFrames*, conocemos los diferentes tipos de datos. Ahora bien, en ciertas columnas los datos pueden estar determinado a un conjunto de posibles opciones, esos datos se llamarán **datos categóricos**(`category`). Este conjunto de posibles respuestas, es especialmente importante si pensamos en una encuesta de satisfacción, tipos de sangre o cualquier tipo de información que deba ceñirse a un conjunto limitado de opciones.

Entendiendo esto, debemos saber utilizar Python para poder localizar registros inconsistentes y limpiar nuestro *DataFrame*. Podemos definir 3 pasos simples a la hora de realizar la limpieza de datos categoricos y datos inconsistentes:

1) Localizar los valores inconsistentes. En este punto, necesitaremos alguna especie de registro o *DataFrame* que contenga los posibles datos, los correctos:

```python
categorias_incons = set(datos_estudio['tipo_sangre']).difference(categoria['tipos_sangre'])
```

2) Localizar los registros que contengan estos valores inconsistentes:

```python
registros_incons = datos_estudio['tipo_sangre'].isin(categorias_incons)
```

3) Poder diferenciar entre los valores inconsistentes y los valores consistentes:

```python
datos_estudio[~registros_incons] #Datos inconsistentes
datos_estudio[registros_incons] #Datos consistentes
```

Ahora bien, los datos categóricos siguen siendo datos de texto. Por lo que lo que más debería de preocuparnos es el hecho de saber como limpiarlos antes de tomarlos como categóricos. Vamos a aprender:

```python
df['columna1'].str.lower()
df['columna1'].str.strip()
```
De igual forma que utilizamos `lower()` o `strip()` para normalizar el texto de un registro cualquiera lo utilizamos para normalizar datos de tipo *string* en un registro. Solo debemos de añadir `.str.lower()` o `.str.strip()` a las funciones de normalización. 

```python
phones['phone_number'] = phones['phone_number'].str.replace(r'\D+', '')
```

En el caso del ejemplo anterior lo que hemos hecho ha sido utilizar una expresión regular, `\D`, para poder remplazar los carácteres que no sean números por nada, eliminarlos.

Una vez hemos conseguido poder normalizar las categorías, y los registros contienen solo los datos categóricos que nos interesan, podemos empezar a jugar con los datos. 


Ahora vamos a aprender a como crear categorias en funcón de los datos:

```python

import pandas as pd

group_names=['0-200k', '200k-500k', '500k+']

demographics['income_group'] = pd.qcut(demographics['household_income'], q=3, labels=group_names)

demographics[['income_group','household_income']]
```

En el ejemplo que acabamos de ver, hemos hecho lo siguiente:

1. Definir los límites de 3 categorias diferentes.
2. Dividir la columna `household_income` en 3 grupos que contengan los mismos número de registros. Mientras creamos una nueva columna, `income_group`, en función del valor y en que rango de límites se encuentra, lo asignamos a uno de los 3 grupos.
3. Mostramos los resultados de `income_group` y `household_income`.

El ejemplo es muy útil cuando sabemos los rangos exactos que debemos definir. En caso de no saberlos, podemos utilizar el siguiente ejemplo:

```python

label_ranges = [0, 60, 180, np.inf]
label_names = ['short', 'medium', 'long']

# Create wait_type column
airlines['wait_type'] = pd.cut(airlines['wait_min'], bins = label_ranges, labels = label_names)
```

El ejemplo es parecido al que ya hemos aprendido, con varias diferencias:

1. En vez de rangos, definimos los valores límite.
2. Indicamos los nombres de las etiquetas.
3. Inicamos que en vez de dividir los registros en 3 grupos diferentes, lo haga en base a los límites de los rangos definidos previamente.

### Capítulo 3: **<ins>Problemas avanzados de datos</ins>**
Como hemos comentado en algún punto, las fechas son datos especialmente sensibles. Ya sea por la gran cantida de formatos, por la mezcla de números y texto e inclusión de carácteres sepadores, son datos que pueden dar más de un dolor de cabeza si intentamos regularizar información. 

También hemos hablado de que la función `to_datetime`, que traduce del formato nativo de la fuente de datos a un formato genérico del que podemos extraer información sobre fechas:

```python
birthdays['Birthday'] = pd.to_datetime(birthdays['Birthday'],
                                    errors = 'coerce')
```
El argumento `.., errors= 'coerce'` nos permite auto-rellenar los valores que den error en la conversión con un `NaN`.

Pero lo realmente interesante, es como podemos manejar las fechas cuando ya las hemos regularizado:

```python
birthdays['Birthday'] = birthdays['Birthday'].dt.strftime("%d-%m-%Y")
```
El punto que nos interesaría sería el siguiente,`.dt.strftime("%d-%m-%Y")`. Básicamente estamos indicando al registro que analizamos que recoja un dato tipo `dt`, datetime. Al indicarle que es de ese formato, podemos especificarle que pese a que lo que analiza es una cadena *string*, el dato corresponde a una fecha, por lo que podemos utilizar expresiones regulares para extrar `%d`, el día `%m`, el mes, y `%Y`, el año. Estas expresiones nos pueden ayudar a extraer estos datos de forma individual, o conjunta, como en el ejemplo.

Otros errores importantes pueden ser los relacionados con la validación cruzada de campos, es decir, datos que para ser consistentes deben de corresponder con información contenida en otros campos. Por ejemplo:
```python

inv_equ = banking[fund_columns].sum(axis=1) <= banking['inv_amount']
```
En la expresión booleana que hay encima podemos ver que utilizamos la suma de las columnas que corresponden a fondos dutilizados por el cliente, para verificar si los fondos disponibles de dicho cliente se han visto sobrepasados o no. De esta forma podemos ver si el cliente ha utilizado más fondos de los que debería, por lo que, utilizamos una validación cruzada de datos. 

Y por encima de esos errores, podemos toparnos con los que podemos considerar los más importantes, los valores ausentes. La ausencia puede deberese a múltiples causas, pero debemos decidir qué hacer con ellos. Hay dos opciones, eliminamos el registro que tenga el valor ausente o rellenamos el valor ausente para que deje de serlo:V

```python
airquality_dropped = airquality.dropna(subset = ['CO2'])
```
En el ejemplo anterior lo que hacemos es eliminar el registro con la función `.dropna(...)`, siendo `Nan` la representación de un valor ausente en un dato de un registro. Pero lo que estamos indicando con el argumento `subset = ['CO2']` es que elimine los registros que tengan valores ausentes en la columna *CO2*.

En cambio, si decidimos rellenar esos valores, podemos hacerlo con la función `fillna`:
```python
co2_mean = airquality['CO2'].mean()

airquality_fillna = airquality.fillna({'CO2': co2_mean})
```
En el ejemplo, generamos un diccionario que substituirá todos los valores ausentes en la columna *CO2* por el promedio de dicha columna.

### Capítulo 4: **<ins>Vinculación de registros</ins>**

Como ya hemos aprendido, la limpieza de datos es de los mayores retos que podemos encontrarnos. Ya sea por datos ausentes o formatos de fechas, hasta ahora hemos aprendido a como gesitonar una gran mayoria de problemas.

Aun así, poder asociar valores erróneos a los correctos es de los mayores retos que podemos encontrarnos, más aun si pretendemos hacerlo de forma automática. Esto se debe a que debemos asumir qué, por similitud, los valores deben de ser substituido por los correctos. Y esto es posible gracias a que podemos medir la distancia de Levenshtein.

**La distancia de Levenshtein**, es un algoritmo que mide la diferencia entre dos textos. Asignando una puntuación de *0*, el más diferente, a *100*, un texto idéntico, este algoritmo mide la cantidad de cambios a realizar en un string para transformarlo en otro. Esto lo hace midiendo 3 tipos posibles de cambios a realizar:

- **Inserción:** Añadir una letra (ej: "Luz" ==> "Luz**a**").

- **Eliminación:** Quitar una letra (ej: "**P**lato" ==> "Lato").

- **Sustitución:** Cambiar una letra (ej: "**C**asa" ==> "**M**asa")

Un ejemplo de todo esto sería calcular la tranformación de "**MAR**" en "**SOL**":

1. Sustituir 'M' por 'S'.

2. Sustituir 'A' por 'O'.

3. Sustituir 'R' por 'L'.

Dando una puntuación de *0*.

En cambio la transformación de "**SAL**" a "**SOL**":

1. Nada
2. Sustituir 'A' por 'O'.
3. Nada

Dando una puntuación de *67*.

De todas formas, es importante conocer el concepto, pero tampoco es esencial saber como se realiza dicho cálculo. Como tenemos la libreria *thefuzz*, podemos calcular la distancia de Levenshtein llamando a sus funciones:
```python
#Importamos la libreria:
from thefuzz import fuzz#, process 

#Comparamos 'Reeding' vs 'Reading'
fuzz.WRatio('Reeding','Reading')
```
Con la función`WRatio` del módulo `fuzz`, conseguimos la puntuación basada en los cambios necesarios para poder transformar un string en otro.

Si bien de esta forma podemos obtener una la puntuación que buscamos, `WRatio` únicamente puede comparar dos palabras a la vez. Esto es muy util, pero algo limitado, solo estamos comparando dos strings a la vez.

La solución al hecho de tener que comparar muchas cadenas de texto a una sola, podemos solucionarla con el módulo `process`. 

```python

from thefuzz import process

#Recorremos una lista de valores considerados correctos para poder contrastar:
for state in categories['state']:

    #Por cada valor correcto, medimos la distancia de Levenshtein con los datos a analizar en `survey`. Lo hacemos fila a fila, indicando shape[0]:
    matches = process.extract(state, survey['state'], limit = survey.shape[0])

    #Recorremos la tupla que nos ha devuelto (String analizado, Puntuación del string, Índice del string)
    for potential_match in matches:

        #Recogemos únicamente el dato de la túpla que nos interesa, la Puntuación de Levenshtein. Si la puntuación es 80 o superior susbtituímos todos los registros de 'survey' por el registro que estamos analizando:
        if potential_match[1] >= 80:
            survey.loc[survey['state'] == potential_match[0], 'state'] = state

```