# 📘 Writing efficient Python code

## 1. Índice

1. [Fundamentos de eficiencia](#capítulo-1-fundamentos-de-eficiencia)
2. []
3. []

------

## 2. Apuntes

### Capítulo 1: **<ins>Fundamentos de eficiencia</ins>**

La efinciencia en python es uno de sus pilares. Así de simple. El hecho de que cualquier fragmento de código se pueda ejecutar sin problema y sea funcional no lo convierte en buen código. Es por eso que cuando Guido van Rossum diseñó Python, lo hizo teniendo en mente la eficiencia como uno de sus pilares fundamentales.

Pero lo primero es definir lo que entendemos como código eficiente. Y para ello nos vasaremos en dos conceptos igual de simples:

1. **LA RAPIDEZ:** Aquel código que tiene una diferencia de tiempo baja entre su ejecución y la devolución de un resultado.

2. **CONSUMO MÍNIMO DE RECURSOS:** El consumo de memoria que tenga la ejecución de nuestro código, afecta directa y significativamente a la eficiencia del mismo.

3. **LEGIBILIDAD:** No solo debe ser rápido cuando se ejecuta, sino también cuando se lee y revisa. 

Cuando estos 3 principios se cumplen, diremos que nuestro código es **pitónico**. Vamos a ver un ejemplo:

```python
#NO-pitónico:
numeros_doblados = []

for i in range(len(nums)):
    numeros_doblados.append(nums[i] * 2)

#Pitónico:
numeros_doblados = [x * 2 for x in nums]
```

Las mismas bibliotecas integradas de Python, tienen componentes que nos ayudan a elaborar este código eficiente sin problema, y suponen una de sus mayores fortalezas. Algunas de las funciones que ayudan podrían ser:

* `range()`: Es una función útil, cuando queremos crear rangos de números. Por ejemplo:

```python
#NO-pitónico:
nums = [1,2,3,4,5]

#Pitónico:
nums = range(1,6)

lista_nums = list(nums)
```

Es importante indicar qué, la función `range` devuelve una objeto de rango. Si queremos una lista, deberemos convertirlo al tipo de dato deseado, **o podemos utilizar el carácter estrella para descomprimirlo `*`**.

La función se compone de los siguientes campos: `range(<start_value>, <stop_value>, <step_value>)`. El valor `stop`, es excluyente, por lo que realmente, finalizará en el valor previo al que se le ha indicado. 

* `enumerate()`: Proporciona elementos de índice para cada elemento en el objeto proporcionado. Por ejemplo:

```python

letras = ['a', 'b', 'c', 'd']

letras_indexadas = enumerate(letras)

lista_indexada = list(letras_indexadas) #[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
dicci_indexado = dict(letras_indexadas) #{0: 'a', 1: 'b', 2: 'c', 3: 'd'}
```

Podemos alterar el primer valor de indexación, utilizando el argumento `start` dentro de enumerate:

```python
letras = ['a', 'b', 'c', 'd']

letras_indexadas = enumerate(letras, start=5)

lista_indexada = list(letras_indexadas) #[(5, 'a'), (6, 'b'), (7, 'c'), (8, 'd')]
```

* `map()`: Aplica una función a cada elemento del objeto. Por lo tanto, toma dos valores de inicio, primero, la función a aplicar, y segundo, el objeto al que le aplicaremos dicha función. Por ejemplo:

```python
nums = [1.5, 2.3, 3.4, 4.6, 5.0]

num_redondeados = map(round, nums)

list(num_redondeados) #[2, 2, 3, 5, 5]
```

Si creamos una **función lambda**, también podemos utilizarla dentro de `map`:
```python
num = [1, 2, 3, 4, 5]

cuadrados = map(lambda x: x**2, num)

list(cuadrados) #[1, 4, 9, 16, 25]
```

De esta forma podemos ahorrarnos la necesidad de crear un bucle.

**NumPy**, la librería de Python especialmente útil para la ciéncia de datos, también nos provee de herramientas útiles para escribir código eficinete en Python. 

El principal benefício de esta librería serían las matrices NumPy. Es un tipo de dato homogénio, por lo que debe contener el mísmo tipo de valor, flotantes o numérico, o cualquier otro, pero únicamente de un tipo. Estas matríces son mucho más eficientes con la memória que las listas básicas de Python:

```python

num_lista = [*range(5)] #[0, 1, 2, 3, 4]

#
import numpy as np

numpy_array = np.array(range(5)) #array([0, 1, 2, 3 , 4])
```

Si generamos un array con diferentes típos, NumPy estandarizará los valores:

```python

numpy_array = np.array([1, 2.5, 3]) #array([1. , 2.5, 3. ]) 
```

Esto hace que las matrices, sean mucho más eficientes que las simples listas de Python dado que tenemos el mismo tipo de dato en todos los valores que analizamos. 

Pero de todas formas, estas matrices nos permiten hacer cosas que las listas de Python harían de una forma mucho menos eficiente, como aplicar una función a todos los conjuntos de una lista. Imaginemos que queremos elevar al cuadrado todos los valores que contiene una lista. Con una lista, podríamos hacerlo aplicando un bucle que itere y aplique el cuadrado o con una comprensión de listas. Pero si queremos hacerlo más eficiente aun, podemos hacerlo a través de una matriz:

```python

num_np = np.array([-2, -1, 0, 1, 2])

num_np ** 2 #array([4, 1, 0, 1, 4])
```

Con una simple operación, hemos podido hacer lo que pretendiamos ahorrando memoria y tiempo.

Pero si escalamos la dificultad, las ventajas de estas matrices se hacen aun más evidentes. Intentemos acceder a diferentes valores de una lista bidimensional, y de una matriz bidimiensional. A nivel estructural, serían lo mismo, pero al acceder a una u otra, vemos claramente las diferencias:

```python

#2-D lista:
num_2D = [
    [1, 2, 3],
    [4, 5, 6]
]
##Indexar el segundo valor de la primera lista:
num_2D[0][1] #2
##Devolver el primer valor de ambas listas:
[row[0] for row in num_2D] #1, 4

#2-D array:
num_array = np.array(nums_2)
##Indexar el segundo valor de la primera fila:
num_array[0, 1] #2
##Devolver el primer valor de ambas filas:
num_array[:,0] #1, 4
```

También existe una forma especial de indexar con estas matrices, la **indexación booleana**. Funciona de la siguiente forma:
```python

num_np = np.array([-2, -1, 0, 1, 2])

num_np > 0 #array([False, False, False, True, True])

num_np[num_np > 0] #array([1, 2])
```

Esto, sigue siendo extremadamente más eficiente que hacer una comprensión de lista para poder filtrar valores. 