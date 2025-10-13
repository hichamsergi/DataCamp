# 📘 Intermediate Python for Developers

---

## 1. Descripción

En este capítulo profundizarás en conceptos avanzados de Python pensados para desarrolladores: cómo manejar funciones más flexibles, crear código eficiente, gestionar errores correctamente y escribir programas más robustos.

El objetivo es que pases de escribir scripts simples a construir componentes reutilizables y sostenibles, con buenas prácticas que se usan profesionalmente.

---

## 2. Índice:

1. [El ecosistema Python](#capítulo-1-el-ecosistema-python)
   - [Funciones integradas](#11-funciones-integradas)
   - [Módulos](#12-módulos)
   - [Paquetes](#13-paquetes)
2. [Alias con funciones](#capítulo-2-alias-con-funciones)
3. [Funciones lambda y gestión de errores](#capítulo-3-funciones-lambda-y-gestión-de-errores)
4. [Gestión de errores](#capítulo-4-gestión-de-errores)
---

## 3. Apuntes:

### Capítulo 1: **<ins>El ecosistema Python</ins>**

El atractivo de Python para el desarrollo de software, la inteligencia artificial o el análisis de datos no radica únicamente en su legibilidad, sino principalmente en el conjunto de herramientas, librerías y utilidades que lo convierten en una herramienta tan poderosa. 

Estas herramientas, las podríamos diferenciar en tres grandes grupos:

#### 1.1) **<ins>Funciones integradas</ins>**: 
Son funciones integradas en el mísmo lenguaje, disponibles por defecto, sin necesidad de importar módulos externos. Algunas de las más interesante, para lo que nos ocupa, serían las funciones numéricas. Estas son funciones nos facilitan la vida bastante, algunos ejemplos:

```python

ventas = [10,2,67,3,6.57999]

max(ventas) # 67

min(ventas) # 2

sum(ventas) # 88.57999

len(ventas) # 5

sorted(ventas) # [2,3,6.57999,10,67]

# Con esta herramienta podemos jugar y extraer un promedio:
sum(ventas) / len(ventas)

# Ahora podríamos querer redondear el total de ventas a dos decimales:
total_ventas = sum(ventas)

round(total_ventas,2) # Esto nos redondeará a dos decimales, 88.58

# Para hacerlo más rápido:
total_ventas = round(sum(total_ventas),2)

```

Estas funciones integradas no solo tienen aplicaciones numéricas, también podemos aplicarlas a los strings:

```python

# String:

len("Introduccion a Python para desarrolladores") # 42

sorted("Hicham") # ['H','a','c','h','i','m']
```

En caso de tener dudas de como podemos utilizar una función, podemos llamar a la misma función ```help(...)```, y esta nos dará toda la documentación de la función que pretendemos utilizar:

```python

help(sorted)

# sorted(iterable, /, *, key=None, reverse=False)
#     Return a new list containing all items from the iterable  in ascending order.
```

#### 1.2) **<ins>Módulos</ins>**: 
Son *scripts* integrados en Python que contienen **atributos**, **funciones** e incluso **otros módulos**. Esto nos ayuda especialmente a evitar escribir código que ya existe.

Algunos de los módulos más populares:

 - ```os```: Módulo que nos permite interactuar e interpretar el sistema operativo del equipo donde se ejecuta Python.

 - ```collections```: Módulo que ofrece una amplia variedad de estructuras de datos avanzadas.

 - ```string```: Módulo que nos permite realizar operaciones avanzadas con strings.

 - ```logging```: Módulo que permite registrar información cuando se realizan pruebas de software.

 - ```subprocess```: Módulo que permite ejecutar comandos de terminal.

 Toda esta información es muy útil, pero necesitamos saber como integrar estos módulos dentro de nuestro código. Para poder hacerlo, debemos de importarlos:
 
 ```python
 
    import os

    os.getcwd() # Nos mostrará el directorio activo actual
    os.chdir("/home/hichamsergi")  # Cambiará de directorio raíz del usuario hichamsergi

    help(os) # Nos mostrará toda la documentación referente al módulo OS
 ```

 Pese a todo, el hecho importar un módulo entero para utilizar únicamente unas pocas funciones es algo muy poco eficiente. Podemos importar unicamente las funciones que sean necesarias de la siguiente forma:
 ```python

   from os import getcwd, chdir # Así solo importamos las funciones necesarias.
 ```

#### 1.3) **<ins>Paquetes</ins>**: 
Consiste en una colección de módulos organizados dentro de una carpeta. Esto permite estructurar y reutilizar el código de las funciones contenidas en los diferentes módulos de la carpeta.

Para poder importar los módulos contenidos en un paquete, debemos instalar el mismo paquete, en este caso ```pandas```:
```bash
hicham@localhost:~$ python3 -m pip install pandas
```
Una vez hemos instalado el paquete con todos los módulos, podemos hacer uso de esos módulos importándolos.

Una buena práctica en python, consiste en renombrar los paquetes dentro de nuestro código, de forma que no tengamos que llamar todo el rato al mismo módulo:
```python
import pandas as pd
...
```

Siguiendo el  ejemplo, ```pandas``` es un paquete especialmente interesante, ya que nos permite hacer cosas útiles como transformar un simple diccionario en un **DataFrame**. Los *Dataframe*, son una forma de organizar información parecida a la de las matrices o tablas de *Excel*, en las que hay columnas con datos organizados en filas:
```python
import pandas as pd

#Simple diccionario:
ventas = {
  "user_id":["KM37","PR19","YU88"],
  "order_value":[10,200,132]
}

#Convertimos el diccionario en un DataFrame:
ventas_df = pd.DataFrame(ventas)

ventas_df

#  user_id  order_value
#0    KM37           10
#1    PR19          200
#2    YU88          132
```

También podemos leer diferentes tipos de archivos con pandas, como CSV:
```python

ventas = pd.read_csv("ventas.csv") # Esto convertirá el contenido del CSV en un DataFrame

ventas.head() # Esto nos mostrará las primeras 5 filas del DataFrame generado
```

### Capítulo 2: **<ins>Alias con funciones</ins>**

Habitualmente, podemos encontrarnos con ciertas limitaciones, puede haber ocasiones donde las funciones integradas de python o paquetes de funciones no sean suficiente y necesitemos crear las nuestras propias. Para poder hacerlo debemos de hacernos las siguientes preguntas:

  **1) ¿Cuántas líneas ocupará nuestro código si no creamos la función?**  
  **2) ¿Cuál es la complejidad de nuestra función?**  
  **3) ¿Cuál será la frecuencia de uso de nuestra función?**  

Esto nos ayudará a cuestionarnos si realmente es necesario crear nuestra función propia. Pese a ello, podemos seguir la regla más simple de todas, *Don't Repeat Yourself* (**DRY**).

Para poder crear nuestra propia función podemos hacerlo de la siguiente forma:
```python

def average(values):

  # Calcular el promedio
  average_value = sum(values) / len(values)

  rounded_average = round(average_value, 2)

  # Devolvemos el valor deseado fuera de la función
  return rounded_average
```

Ahora, entendemos el funcionamiento básico de las funciones. Pese a ello, podemos profundizar aún más en como trabajan y porque hacen lo que hacen. Empezando por descomponer las funciones:

```python
def function_name(argument):
  ...
```

La descripción de los dos primeros términos es simple, utilizamos ```def``` para definir una función propia, y lo siguiente es el mísmo nombre que le asignaremos a la función, en este caso ```function_name(...)```.

En cuanto al ```argument```, serían los argumentos que les transmitimos a la función para poder funcionar. Podemos transmitirle de dos tipos diferentes:

* <ins>**Posicional**</ins>: Los argumentos posicionales corresponden a su utilidad dependiendo de la posición en la que se recogen. Tomando como ejemplo una función que ya conocemos, la función round:
  
  ```python
  round(3.1415926535, 2)
  ```
  Estaríamos indicando que el primer número es el que queremos redondear, y el segundo, el decimal sobre el que redondearemos, en este caso el segundo:

  ```python
  >>> round(3.1415926535, 2)
  3.14
  ```

* <ins>**Palabras clave**</ins>: Por el contrario, los argumentos basados en palabras clave, requieren que definamos el valor de cada argumento utilizando su palabra clave. Esto es especialmente útil cuando tenemos una función con muchos argumentos, dado que podemos asignar una palabra clave a cada argumento para poderlos utilizar. Volvemos a utilizar la función round para ejemplificar:

  ```python
  round(number=3.1415926535, ndigits=2)
  ```
  Entendiendo esto, podemos asignar valores por defecto a los mismos argumentos que transmitimos a una función. Tomamos por ejemplo la función del promedio redondeado a 2 dígitos:
  ```python

  def average(values,rounded=False): #Podemos definir también None, indicando que el argumento está vacío

    # Calcular el promedio si reunded es True
    if rounded == True:
      average_value = sum(values) / len(values)
      rounded_average = round(average_value, 2)
      return rounded_average

    # Sino, no redondeamos:
    else:
      average_value = sum(values) / len(values)
      return average_value
  ```

Esta función es especial, y únicamente redondeará los valores que nosotros decidamos. Dado qué como segundo valor definimos por defecto de tipo *booleano* tal que ```False```, solo se redondearán los números que forcemos que tengan un segundo argumento de tipo ```True```:

  ```python
  ventas = [125.97,84.32,99.78,154.21,78.50,83.67,111.13]

  average(ventas, False) # No redondeará

  average(ventas) # No redondeará, utilizando el valor por defecto FALSE

  average(values=ventas, rounded=True) # Redondeará
  ```

Puede haber casos en los que no sabemos cuántos valores se van a pasar a una función. Python nos permite manejar esta situación utilizando **argumentos arbitrarios**, que hacen nuestras funciones más flexibles.

Siguiendo con el ejemplo anterior, podemos modificar nuestra función **`average()`** para que acepte un número **indefinido** de valores en lugar de una lista.
Para ello, utilizamos `*args`, que agrupa todos los valores recibidos en una tupla:

```python
def average(*values, rounded=False):
  """
  Calcula el promedio de un número variable de valores numéricos.
  Permite redondear el resultado si se indica.
  
  Args:
      *values (float): Conjunto de valores numéricos.
      rounded (bool): Determina si el resultado debe redondearse.
  
  Returns:
      float: Promedio redondeado o sin redondear según 'rounded'.
  """

  average_value = sum(values) / len(values)

  if rounded:
    return round(average_value, 2)
  else:
    return average_value


print(average(5, 10, 15))           # 10.0
print(average(5, 10, 15, rounded=True))  # 10.0
```

También podemos añadir **`**kwargs`** para aceptar pares **clave-valor** y mostrar, por ejemplo, información adicional sobre el cálculo:

```python

# Define a function called concat
def concat(**kwarg):
  
  # Crea una cadena vacía
  result = ""
  
  # Iteramos sobre los valores asignados a las claves
  for arg in kwarg.values():
    result += " " + arg
  
  return result

# Ejemplo:
print(concat(start="Python", middle="is", end="great!")) # Python is great!
```

Y antes de terminar, algo que nos ayuda y podríamos considerar como la mejor de las practicas cuando generamos funciones personalizafas, el **DOCSTRING** de una función. Los *docstrings* de las funciones, corresponden a una breve descripción de la utilidad de la función. Pese a no ser obligatorio el hecho de definirlo, esto nos puede ayudar a entender las funciones en un futuro, no solo a nosotros sino también a cualquiera que lea nuestro código y quiera hacer uso de nuestras funciones:

  ```python

  def average(values,rounded=False): 
    """
    Esta función se utiliza para poder redondear a 2 decimales los promedios de los 
    conjuntos de valores que deseemos.
    
    Args:
        values (list): Conjunto de valores numéricos.
        rounded (boolean): Valor booleano, utilizado para decidir cuando redondeamos.
    
    Returns:
        rounded_average: Promédio redondeado, cuando rounded == True.
        average_value: Promédio sin redondear, cuando rounded == False.
    """
  
    if rounded == True:
      average_value = sum(values) / len(values)
      rounded_average = round(average_value, 2)
      return rounded_average

  
    else:
      average_value = sum(values) / len(values)
      return average_value
  ```

### Capítulo 3: **<ins>Funciones lambda</ins>**

Llegados a este punto, hemos aprendido a utilizar las funciones incorporadas de python y a generar nuestras propias funciones. Pese a ello, escribir una función personalizada de python desde cero puede ser algo tedioso y requerir mucho código. Para solucionar esto, python nos permite hacer uso de las **funciones lambda**.

Las **funciones lambda**, son funciones anónimas que no requieren de nombres ni necesitan guardarse como veriables, pese a que podemos almacenarlas. La forma de declararlas es la siguiente:

```python
lambda argument(x): expresion
```

  - Se utiliza **```x```** para un argumento simple.
  - **```expresion```** corresponderia al cuerpo de la función.
  - No requiere de declara **```return```** para devolver valores.

    
Ahora vamos a comparar una función personalizada y una lambda:

  - **Función Personalizada**:

```python
def promedio(valores):

  valor_promedio = sum(values) / len(values)

  return valor_promedio

print(promedio[3,6,9]) # 6.0
```

  - **Función Lambda**:

```python

lambda x: sum(x) / len(x)

#Recoger el promedio utilizando función lambda:
(lambda x: sum(x) / len(x))([3,6,9]) # 6.0
```

Como se puede ver, la función lambda nos permite ejecutar en una única línea de código exactamente lo mísmo que la función personalizada.

Como comentaba, pese a que las funciones lambda no necesítan ser asignadas a una variable, podemos hacerlo sin problema:

```python

# Asignación:
promedio = lambda x: sum(x) / len(x)

#Llamamos a la función lambda:
promedio([3,6,9]) # 6.0
```

Y de igual forma, podemos extender las funciones lambda y complicarnos mas la vida:
```python
(lambda x, y: x**y)(2,3) # 8
```

Un caso importante a comentar sería el uso de funciones lambda sobre iterables, como elementos de una lista. Dado que cuando utilizamos una función lambda, podríamos llegar a necesitar que se ejecutase sobre cada elemento de la lista:

```python

numeros = [1, 2, 3, 4]
resultado = map(lambda x: x ** 2, numeros)

print(list(resultado))  # [1, 4, 9, 16]
```

En estos casos, utilizamos la función integrada de python ```map``` para aplicar la función lambda a cada elemento de la lista. Esta función genera un **objeto map**, que posteriormente deberemos transformar en una lista utilizando de nuevo la función integrada de python ```list```. ```Map``` puede aplicar nuestra función lambda a todos los iterables grácias a su sintaxis:

```python

map(funcion,iterable)
```

En cualquier caso, es importante tener siempre claro cuando y como se deben de utilizar las funciones dadas las utilidades que nos presenta cada una.

|Escenários|Tipo de función|
|----------|---------------|
|Tareas complejas| Personalizada|
|Misma tarea repetidamente| Personalizada|
|Tarea simple| Lambda|
|Tarea una única vez| Lambda|

---

### Capítulo 4: **<ins>Gestión de errores</ins>**

Finalmente, algo demasiado importante como para pasar por alto, la **gestión de errores**. Entendemos por gestionar errores, como preparamos a nuestro codigo para manejar situaciones para las que no está preparado.

Si nos paramos a pensar, pese a que puede sonar paradogico, lo que estamos haciendo es decirle al programa qué en caso de no reaccionar de la forma deseada genere un error determinado. Conociendo algún error podemos entender la idea:

  - **<ins>TypeError</ins>**: Errore que se genera cuando el dato que estamos manejando es incompatible para la tarea que lo está utilizando. Ejemplo:
  
  ```python

  >>> "Hello" + 5

  TypeError: can only concatenate str (not "int") to str
  ```

  - **<ins>ValueError</ins>**: Error que se genera cuando el valor introducido no esta dentro de un rango aceptable. Ejemplo:
  
  ```python

  >>> float("Hello")

  ValueError: could not convert string to float: 'Hello'
  ```

  - **<ins>IndexError</ins>**: Error generado al acceder a un índice fuera de rango. Ejemplo:
  
  ```python

  >>> valores = [1, 2, 3]

  >>> valores[4]

  IndexError: list index out of rang
  ```

Pero más allá de poder diferenciar entre tipos de errores, lo que nos interesa es saber como podemos integrar este  conocimiento en nuestro código. Para poder integrarlo, utilizamos las sentencias ```try``` y ```except```. Utilizamos el ejemplo de nuestra querida función de promedios:

```python
def promedio(values):
  
  try:

    #Código que podría causar un error:
    valor_promedio = sum(values)/len(values)
    return valor_promedio

  except TypeError:
    #Código a utilizar si aparece un error:
    print("promedio() solo acepta listas o sets. Dato introducido incorrecto.")
  
```

También podemos hacerlo utilizando el metodo ```rise```:

```python
def promedio(values):
  
  if type(values) not in ["list","set"]:
    #Código que podría causar un error:
    valor_promedio = sum(values)/len(values)
    return valor_promedio
  
  else:
    #Código a utilizar si aparece un error:
    raise TypeError("promedio() solo acepta listas o sets. Dato introducido incorrecto.")
```

Ambas opciones tienen sus ventajas y desventajas, como siempre, lo importante es escoger bien la ocasión:

| Método             | Descripción                                                                                                                                        | Cuándo usarlo                                                                                                            |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | 
| **`try - except`** | Se utiliza para **capturar y manejar errores** que ocurren durante la ejecución del código. Permite evitar que el programa se detenga bruscamente. | Cuando queremos **prevenir fallos** y ofrecer una **alternativa controlada** al usuario o al flujo del programa.         |
| **`raise`**        | Se utiliza para **lanzar manualmente un error** cuando se detecta una condición no deseada.                                                        | Cuando queremos **forzar un error personalizado** o **detener la ejecución** si algo no cumple una condición específica. |
