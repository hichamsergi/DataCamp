# 📘 Intermediate Python for Developers

---

## 1. Descripción



---

## 2. Índice:

1. [El ecosistema Python](#capítulo-1-el-ecosistema-python)
2. [Alias con funciones](#capítulo-2-alias-con-funciones)
3. [Funciones lambda y gestión de errores](#capítulo-3-funciones-lambda-y-gestión-de-errores)

---

## 3. Apuntes:

### Capítulo 1: **<ins>El ecosistema Python</ins>**

El atractivo de Python para el desarrollo de software, la inteligencia artificial o el análisis de datos no radica únicamente en su legibilidad, sino principalmente en el conjunto de herramientas, librerías y utilidades que lo convierten en una herramienta tan poderosa. 

Estas herramientas, las podríamos diferenciar en tres grandes grupos:

**<ins>1) Funciones integradas</ins>**: Son funciones integradas en el mísmo lenguaje, disponibles por defecto, sin necesidad de importar módulos externos. Algunas de las más interesante, para lo que nos ocupa, serían las funciones numéricas. Estas son funciones nos facilitan la vida bastante, algunos ejemplos:

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

**<ins>2) Módulos</ins>**: Son *scripts* integrados en Python que contienen **atributos**, **funciones** e incluso **otros módulos**. Esto nos ayuda especialmente a evitar escribir código que ya existe.

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

**<ins>3) Paquetes</ins>**: Es una colección de módulos organizados dentro de una carpeta. Esto permite estructurar y reutilizar el código de las funciónes contenidas en los diferentes módulos de la carpeta.

Para poder importar los módulos contenidos en un paquete, debemos instalar el mismo paquete, en este caso ```pandas```:
```bash
hicham@localhost:~$ python3 -m pip install pandas
```
Una vez hemos instalado el paquete con todos los módulos, podemos hacer uso de esos módulos importándolos.

Una buena práctica en python, consiste en renombrar los paquetes dentro de nuestro código de forma que no tengamos que llamar todo el rato al mismo módulo:
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

ventas.head() # Esto nos mostraá las primeras 5 filas del DataFrame generado
```

### Capítulo 2: **<ins>Alias con funciones</ins>**

Habitualmente, podemos encontrarnos con ciertas limitaciones, puede haber ocasiones donde las funciones integradas de python o paquetes de funciones no sean suficiente y necesitemos crear las nuestras propias. Para poder hacerlo debemos de hacernos las siquientes preguntas:

  **1) ¿Cuantas líneas ocupará nuestro código si no creamos la función?**
  **2) ¿Cual es la complejidad de nuestra función?**
  **3) ¿Cual será la frecuencia de uso de nuestra función?**

Esto nos ayudará a cuestionarnos si realmente es necesario crear nuestra función propia. Pese a ello podemos seguir la regla mas simple de todas, *Don't Repeat Yourself* (**DRY**).

Para poder crear nuestra porpia función podemos hacerlo de la siguiente forma:
```python

def average(values):

  # Calcular el promedio
  average_value = sum(values) / len(values)

  rounded_average = round(average_value, 2)

  # Devolvemos el valor deseado fuera de la función
  return rounded_average
```

Ahora, entendemos el funcionamiento basico de las funciones. Pese a ello, podemos profundizar aun más en como trabajan y porqué hacen lo que hacen. Empezando por descomponer las funciones:

```python
def function_name(argument):
  ...
```

La descripción de los dos primeros terminos es simple, utilizamos ```def``` para definir una función propia, y lo siguiente es el mísmo nombre que le asignaremos a la función, en este caso ```function_name(...)```.

En cuanto al ```argument```, serían los argumentos que les transmitimos a la función para poder funcionar. Podemos transmitirle de dos tipos diferentes:

* **Posicional**: Los argumentos posicionales corresponden a su utilidad dependiendo de la posición en la que se recogen. Tomando como ejemplo una función que ya conocemos, la función round:
  
  ```python
  round(3.1415926535, 2)
  ```
  Estaríamos indicando que el primer número es el que queremos redondear, y el segundo, el decimal sobre el que redondearemos, en este caso el segundo:

  ```python
  >>> round(3.1415926535, 2)
  3.14
  ```

* **Palabras clave**: Por el contrario, los argumentos basados en palabras clave, requieren que definamos el valor de cada argumento utilizando su palabra clave. Esto es especialmente útil cuando tenemos una función con muchos argumentos, dado que podemos asignar una palabra clave a cada argumento para poderlos utilizar. Volvemos a utilizar la función round para ejemplificar:
```python

round(number=3.1415926535, ndigits=2)
```

### Capítulo 3: **<ins>Funciones lambda y gestión de errores</ins>**



---