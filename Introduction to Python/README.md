# 📘 Introduction to Python

---

## 1. Descripción

Breve introducción a Python desde 0, sin requerimientos de conocimientos previos en este lenguaje de programación.

---

## 2. Índice:

1. [Que es Python?](#capítulo-1-que-es-python)
2. [Trabajar con diferéntes *data types*.](#capítulo-2-trabajar-con-diferéntes-data-types)
3. [Estructuras condicionales y bucles.](#capítulo-3-estructuras-condicionales-y-bucles)

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

- **Listas:** Las listas representan un tipo de dato que puede almacenar múltiples valores en una única variable, conteniendo múltiples tipos de datos como *strings*, *integers*, *floats* o *booleans*. Todo el contenido de una lista debe de delimitarse entre **corchetes**,```[]```, separando los diferentes datos por comas:
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
- **Diccionarios:** Los diccionarios son una estructura de datos formada por dos componentes, la **clave** y el **valor**. Mientras las *listas* se componian de diferentes elementos *individuales*, los diccionarios al igual que su versión física se componen de una palabra, lo que sería la *clave*, y una definición, el *valor*. Esta estructura de datos se encapsula entre dos llaves, ```{}```:
```
# Diccionario asociando un producto con su precio:

prod_prec = {"P1":10, "P2":20,
             "P3":30, "P4":40,
             "P5":50, "P6":60}
```
Este tipo de dato no utiliza una indexación numérica, como las listas. Para poder acceder a los valores que el mísmo diccionario contiene, accedemos refiriendonos a la clave asociada al valor:
```
# Ver el precio del producto "P4":

prod_prec["P4"] # 40
```
Ahora bien, en algunos casos podemos querer ver el listado completo de productos, siguiendo el ejemplo, o por le contrario, el listado de precios de los productos. Para poder obtener toda esa información, podemos hacero así:
```
prod_prec.key() # dict_keys(['P1', 'P2', 'P3', 'P4', 'P5', 'P6'])

prod_prec.value() # dict_values([10, 20, 30, 40, 50, 60])

print(prod_prec)
```

Otro **pequeño truco** que podemos aplicar con los diccionarios es el hecho de generar una lista compuesta por todas las asociaciones clave-valor que tiene el diccionario:
```
prod_prec.items() # dict_items([('P1', 10), ('P2', 20), ('P3', 30), ('P4', 40), ('P5', 50), ('P6', 60)])
```
Comentar qué, esta lísta esta compuesta por diferentes paréntesis que encapsulan los conjuntos clave-valor. Eso implica que la lista esta compuesta por diferentes *tumplas*, que es un tipo de dato que veremos más adelante.

Pero los diccionarios pueden, y a veces deben, de ser modificables. De tal forma que podemos llegar a necesitar modificar un valor o añadir uno nuevo. Podemos hacerlo así:
```
# Añadimos un nuevo producto con su precio:

prod_prec["P7"] = 70

# Actualizamos el precio de un producto:

prod_prec["P6"] = 50
```

**¡¡¡IMPORTANTE!!!**: LOS DICCIONARIOS NO ACEPTAN CLAVES DUPLICADAS, estas deben de ser únicas.

- **Set:** Es un tipo de dato en python que **almacena valores únicos**. Los valores contenidos en el *set* no puede cambiar, por lo que una vez se han generado son inalterable. Pese a ello, podemos eliminar o añadir nuevos valores. Este tipo de dato es especialmente útil para eliminar valores duplicados de un conjunto de datos. Los datos en los *sets* se almacenan de forma desordenada, haciendolos bastante rapidos a la hora de buscar valores en su interior, pero inindexables.Esta estructura de datos se encapsula entre dos llaves, ```{}```:
```
# Invitados a un evento:

invitados = {"Isaac", "Natxo",
             "Marc", "Alberto",
             "Marcia", "Hicham"}

print(invitados)
```

Dadas las propiedades que tienen los sets, podemos necesitar en algun momento convertir otros tipo de datos a *set*, a esto lo llamamos **casting**:
```
lista_invitados = ["Isaac", "Natxo",
            "Marc", "Alberto",
            "Marcia", "Hicham", "Isaac"]

# Convertimos la lista en un set:

invitados_VIP = set(lista_invitados)

# Comprobamos que tipo de dato es "invitados_VIP":
type(invitados_VIP) # <class 'set'>
```
Pese al hecho de que **los valores contenidos en los sets no pueden tener índices**, hay funcines bastante útiles a la hora de tratar con ellos:
```
# Ordenar un set:

sorted(invitados_VIP) # ['Alberto', 'Hicham', 'Isaac', 'Marc', 'Marcia', 'Natxo']
```

- **Tuplas:** Este es otro tipo de dato que tiene una peculiaridad significativa, es **inmutable**. A diferencia del *set*, donde los valores son los inmutables, las tuplas no pueden ser modificadas de ninguna de las formas. No se puede añadir valores, eliminarlos o modificar ningún tipo de datos o elemento contenido por una tupla, una vez creada es inalterable. También podemos diferenciarlo de los *set* en el hecho de que están ordenados, de forma que son indexables. Este dato es especialmente útil cuando pretendemos almacenar datos que de ninguna de las formas debe o puede ser alterable, como contraseñas. Los datos de las tuplas son almacenados de enre dos paréntesis, ```()```:
```
# Almacenamos las localizaciones de oficinas:

ofi_localizacion = ("Barcelona", "Madrid", "Bilbao", "Malaga")

ofi_localizacion[2] # Bilbao 

# Convertir una lista en una tupla:

2_tupla = tuple(my_lista)
```

##### RESUMEN:

| Estructura de datos | Sintaxis     | Inmutable | Permite valores duplicados | Ordenada | Indexación con  [..] |
|----------------------|-------------|-----------|----------------------------|----------|--------------------|
| Lista (List)        | [1, 2, 3]   | No        | Sí                         | Sí       | Sí - por índice    |
| Diccionario (Dict)  | {clave:valor} | No      | Sí                         | Sí       | Sí - por clave     |
| Conjunto (Set)      | {1, 2, 3}   | No        | No                         | No       | No                 |
| Tupla (Tuple)       | (1, 2, 3)   | Sí        | Sí                         | Sí       | Sí - por índice    |

---

### Capítulo 3: **Estructuras condicionales y bucles**

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
