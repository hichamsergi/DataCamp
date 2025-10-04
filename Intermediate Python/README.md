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

**1) Funciones integradas**: Son funciones integradas en el mísmo lenguaje, disponibles por defecto, sin necesidad de importar módulos externos. Algunas de las más interesante, para lo que nos ocupa, serían las funciones numéricas. Estas son funciones nos facilitan la vida bastante, algunos ejemplos:

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

**2) Módulos**: Son *scripts* integrados en Python que contienen **atributos**, **funciones** e incluso **otros módulos**. Esto nos ayuda especialmente a evitar escribir código que ya existe.

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

**3) Paquetes**:

### Capítulo 2: **<ins>Alias con funciones</ins>**



### Capítulo 3: **<ins>Funciones lambda y gestión de errores</ins>**



---