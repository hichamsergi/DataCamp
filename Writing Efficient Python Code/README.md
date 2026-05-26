# 📘 Writing efficient Python code

## 1. Índice

1. [Fundamentos de eficiencia](#capítulo-1-fundamentos-de-eficiencia)
2. [Temporización y perfilamiento de código](#capítulo-2-temporización-y-perfilamiento-de-código)
3. [Ganando eficiéncia](#capítulo-3-ganando-eficiéncia)
4. []

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

### Capítulo 2: **<ins>Temporización y perfilamiento de código</ins>**

Como hemos comentado anteriormente, uno de los pilares de Python consiste en la rapidez de ejecución de nuestro código. Si queremos identificar que código se ejecuta con mayor rapidez, podemos hacerlo con el comando mágico de Python `%timeit`:

```python

%timeit num_aleatorios = np.random.rand(1000) #8.61us +- 69.1ns per loop (mean +- std. dev. of 7 runs, 100000 loops each)
```

Como se puede ver en el output, este comando nos proporciona información estadística, como la media(8.61) y la desviación estándar(69.1). También podemos ver la cantidad de ejecuciones y bucles que han sido necesarios para llevar a cabo la información estadísitica que acabamos de comentar.

El número de ejecuciones representa la cantidad de iteraciones necesarias para estimar el tiempo de ejecución, y podemos forzar a que haya una cantidad determinada. Esto se hace de la siguiente forma:

```python

%timeit -r2 -n10 num_aleatorios = np.random.rand(1000) #16.9us +- 5.14ns per loop (mean +- std. dev. of 2 runs, 10 loops each)
```

Pero podemos jugar con el comando `%timeit`, pidiendole que se ejecute sobre un bloque de código, indicando `%%timeit`. O podemos guardar toda la información de los diferetes tiempos de ejecución que ha habido en todas las ejecuciones, utilizando la opción `-o`:

```python

times = %timeit -o -r2 -n10 num_aleatorios = np.random.rand(1000) #Variable con todos los tiempos de ejecución en una variable de tipo lista.
```

Esto es especialmente útil para poder analizar los diferentes tiempos de ejecución:

```python

times.best
times.worst
```

Pero ahora imaginemos que queremos medir una gran cantidad de código o un bloque, pero línea a línea. Para esto, utilizaremos una técnica llamada Perfilado de Código. Consiste en el analisis del tiempo de ejecución de nuestro código línea a línea. De esta forma se entiende mejor si nuestro código esta siendo eficiente, y en que puntos podemos aplicar una modificación para mejorarlo.

El paquete `line_profiler` nos ayudara a poder hacerlo:

```python
%pip3 install line_profiler

%load_ext line_profiler

%lprun -f <función_a_analizar_sin_parentesis> <llamada_d_función_con_argumentos>
```

Como podemos ver el comádo mágico `lprun` reliza el perfilado por líneas de nuestro código, indicando también el porcentage de tiempo que gasta en cada una de ellas.

Más allá del tiempo, hemos deficinido la eficiencia como el impacto que tiene nuestro código en los recursos del dispositivo en los que se ejecuta. Para poder medir la eficiencia en costo de memória, podemos hacerlo mediante el módulo `sys`:

```python
import sys

num_list = [*range(1000)]

sys.getsizeof(num_list) #9112

num_list_np = np.array(range(1000))

sys.getsizeof(num_list_np) #8096
```

Como hemos visto anteriormente, el módulo `sys` es muy parecido a `%timeit`, perfile y da información de bloques individuales de código. A nosotros nos interesa poder analizar bloques del mismo, por eso queremos utilizar erramientas más potentes, como `memory_profiler`.

El paquete `memory_profiler`, funciona exactamente igual que `line_profiler`, analizamos bloques de código para poder valorar el impacto que tiene en memoria, en vez de en el tiempo de ejecución. Para poder utilizarlo seguimos los mismos pasos:

```python
%pip3 install memory_profiler

%load_ext memory_profiler

%mprun -f convert_units convert_units(heroes, hts, wts)
```

El único inconveniente en perfilar código con `%mprun`, es que para poder hacerlo debemos registrar nuestra función en un archivo externo e importarla:

```python
#Tenemos la función 'convert_units' en el archivo 'hero_funcs.py'

from hero_funcs import convert_units

%load_ext memory_profiler

%mprun -f convert_units convert_units(heroes, hts, wts)
```

### Capítulo 3: **<ins>Ganando eficiéncia</ins>**

Uno de los cuellos de botella que hemos podido llegar a identificar es el iterar sobre valores de una lista. Por ejemplo, tenemos una lista de nombres y les queremos asignar valores numéricos de otra lista, de forma individual. Una forma poco *pitónica* de afrontar el problema sería entrar en un bucle e iterar. La forma *pitónica* de hacerlo sería utilizar la función incorporada **zip**:

```python

names = ['Bulbasaur', 'Charmander', 'Squirtel']
hps = [45, 39, 44]

combined = [*zip(names, hps)] #[('Bulbasaur', 45), ('Charmander', 39), ('Squirtel', 44)]
```

Otro módulo integrado de Python es `collections`. Este, tiene incorporada una función llamada `Counter`, que nos puede servir para poder generar un diccionario con el recuento total por valor proporcionado. Por ejemplo:

```python
poke_type = ['Grass', 'Dark', 'Fire', 'Fire'...]

from collections import Counter

type_counts = Counter(poke_type) #Counter({'Water: 105,
                                 # 'Normal': 92, 'Bug': 65...})
```

Si queremos poder iterar de forma eficiente, podemos utilizar otro módulo, `itertools`. Con esta erramienta, e importanto la función `combinations`, podemos generar todas las posibles combinaciones de elementos de una lista, con el tamaño que indiquemos. Por ejemplo:

```python
# Import combinations from itertools
from itertools import combinations

# Create a combination object with pairs of Pokémon
combos_obj = combinations(pokemon, 2)

#[('Geodude', 'Cubone'), ('Geodude', 'Lickitung'), ('Geodude', 'Persian'), ('Geodude', 'Diglett'), ('Cubone', 'Lickitung'), ('Cubone', 'Persian'), ('Cubone', 'Diglett'), ('Lickitung', 'Persian'), ('Lickitung', 'Diglett'), ('Persian', 'Diglett')] 
```