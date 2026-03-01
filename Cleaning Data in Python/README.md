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

Con la función `.astype(..)` podemos convertir un tipo de dato en otro, siempre y cuando este "sea convertible". Es decir, podemos convertir un '1' en entero, pero no podemos converir '1$' a entero, ya que al contener el simbolo '$' trataríamos una cadena string con un simbolo no convertible a entero.

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

### Capítulo 3: **<ins>Problemas avanzados de datos</ins>**

### Capítulo 4: **<ins>Vinculación de registros</ins>**