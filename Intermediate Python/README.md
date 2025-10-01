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

**1) Funciones integradas**: Son funciones integradas en el mísmo lenguaje, disponibles por defecto, sin necesidad de importar módulos externos. Algunas de las más interesante para lo que nos ocupa, serían las funciones númericas. Estas son funciones nos facilitan la vida bastante, algunos ejemplos:

```python

ventas = [10,2,67,3,6.57999]

max(ventas) # 67

min(ventas) # 2

sum(ventas) # 88.57999

len(ventas) # 5

sorted(ventas) # [2,3,6.57999,10,67]

# Con esta herraminentas podemso jugar y extraer un promedio:
sum(ventas) / len(ventas)

# Ahora podríamos querer redondear el total de ventas a dos decimales:
total_ventas = sum(ventas)

round(total_ventas,2) # Esto nos redondeara a dos decimales, 88.58

# Para hacerlo mas rapido:
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

**2) Módulos**:
**3) Paquetes**:

### Capítulo 2: **<ins>Alias con funciones</ins>**



### Capítulo 3: **<ins>Funciones lambda y gestión de errores</ins>**



---