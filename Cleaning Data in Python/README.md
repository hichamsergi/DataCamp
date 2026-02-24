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



```python
movies = movies[movies["avg_rating"] <= 5]

movies.drop(movies[movies["avg_rating"] <= 5].index, inplace = True)

movies.loc[movies[movies["avg_rating"] <= 5], 'avg_rating'] = 5
```



### Capítulo 2: **<ins>Problemas de texto y datos categóricos</ins>**

### Capítulo 3: **<ins>Problemas avanzados de datos</ins>**

### Capítulo 4: **<ins>Vinculación de registros</ins>**