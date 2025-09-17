# 📘 Introduction to Python

---

## 1. Descripción

Breve introducción a Python desde 0, sin requerimientos de conocimientos previos en este lenguaje de programación.

---

## 2. Índice:

1. [Que es Python?](#capítulo-1-que-es-python)
2. [Trabajar con diferéntes *data types*.](#capítulo-2-trabajar-con-diferéntes-data-types)
3. [Control de flujo y bucles.](#capítulo-3-control-de-flujo-y-bucles)

---

## 3. Apuntes:

### Capítulo 1: **Que es Python?**

- *Python* es un lenguaje de *alto nivel*, su sintaxis es muy parecida al *inglés*.

- Al tener una sintaxis clara y legible es muy *fácil de aprender*, haciendolo ideal para principiantes.

- Tiene un *grán ecosistema de librerías* lo que lo convierte en un lenguaje ampliamente utilizado en campos como el desarrollo de software, análisis de datos, inteligencia artificial y más.

---

### Capítulo 2: **Trabajar con diferéntes *data types***

El objetivo de este capítulo es descubrir los tiferentes tipos de datos en Python, y saber cuándo y cómo utilizarlos. Los tipos de datos son los siguientes:

- **Strings:** Podríamos entenderlo como un tipo de dato que representa **texto**. Los *strings*, al igual que otros tipos de datos, tienen **métodos**. Los métodos son funciones específicas para un tipo de datos en concreto:
```
mi_texto = "Hola Jorge, mi nombre es Sergi"

# Reemplazar el nombre de Sergi por Hicham:
mi_texto = mi_texto.replace("Sergi","Hicham")

# Eliminar todas las mayusculas:
mi_texto = mi_texto.lower()

# Eliminar todas las minúsculas:
mi_texto = mi_texto.upper()

# Mostramos el contenido de la variable mi_texto
print(mi_texto)
```
Normalmente enmarcamos los *strings* entre dos comillas dobles, de tal forma que, así podemos evitar falsas delimitaciones al usar otros carácteres especiales como las comillas simples. Ahora bien, al tener un string muy largo, enmarcamos el string entre tres comillas dobles para poder hacer saltos de línea de forma que el texto sea más legible:
```
mi_texto_largo = """Buenos días Jorge,
Mí nombre es Hicham, y estoy encantado de haberte conocido.
Te escribo para comentarte que estoy aprendiendo Python y,
de momento, he aprendido a manejar strings.
"""
```

- **Listas:** Las listas representan un tipo de dato que puede almacenar múltiples valores en una única variable, conteniendo múltiples tipos de datos como *strings*, *integers*, *floats* o *booleans*. Todo el contenido de una lista debe de delimitarse entre **corchetes**, separando los diferentes datos por comas:
```
# Lista de precios:
precios = [10, 20, 30, 40]

# Mostrar los precios:
print(precios)
```
Otro atributo de las listas es que son elementos ordenados, lo que implica que podemos acceder a los diferentes elementos que conforman una lista mediante el **indice** que ocupa dicho elemento. Hay que aclarar que el indice de elementos siempre empieza por **cero**:
```
# Mostrar el valor del primer y del tercer indice:

precios[0] # 10

precios[2] # 30
```
Un **pequeño truco** que nos proporciona python es el hecho de no necesitar contar cuantos elementos hay en una lista, ya que podemos acceder a lo elementos de manera inversa indicando el indice en negativo:
```
# Mostrar el último valor de la lista:

precios[-1] # 40
```

En el caso de necesitar mostrar multiples elementos, podemos hacerlo indicando dos puntos entre los diferentes indices que queremos:
```
# Mostrar los 3 primeros precios:

precios[0:2] # 10, 20, 30

# Mostrar todos los precios a partir del segundo:

precios[1:] # 20, 30, 40
```

La forma de acceder a diferentes elementos se indica por *rangos*, como se puede ver previamente. Pero también podemos jugar un poco con estos rangos, de forma que si añadimos otros dos puntos al y final e indicamos un **2**, por ejemplo, solo se mostrarán los datos cada 2 posiciones:
```
# Mostrar solo los valores cada 2 precios:

precios[::2] # 10 y 30

precios[1::2] # 20 y 40
```
---

### Capítulo 3: **Control de flujo y bucles**

---

## 4. Ejercicios / Prácticas

- Descripción breve de cada ejercicio trabajado  
- Enlaces a notebooks o scripts  
- Acerca de lo que he aprendido haciendo los ejercicios  

---

---

## 5. Recursos adicionales

- Enlace al curso oficial en DataCamp  
- Materiales complementarios, documentación, lecturas recomendadas  
