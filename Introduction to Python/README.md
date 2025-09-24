# 📘 Introduction to Python

---

## 1. Descripción

Breve introducción a Python desde 0, sin requerimientos de conocimientos previos en este lenguaje de programación.

---

## 2. Índice:

1. [Qué es Python?](#capítulo-1-que-es-python)
2. [Trabajar con diferentes *data types*](#capítulo-2-trabajar-con-diferentes-data-types)
3. [Estructuras condicionales y bucles](#capítulo-3-estructuras-condicionales-y-bucles)
4. [Flujos de trabajo](#capítulo-4-flujos-de-trabajo)
---

## 3. Apuntes:

### Capítulo 1: **Qué es Python?**

- *Python* es un lenguaje de *alto nivel*, su sintaxis es muy parecida al *inglés*.

- Al tener una sintaxis clara y legible, es muy *fácil de aprender*, haciéndolo ideal para principiantes.

- Tiene un *gran ecosistema de librerías,* lo que lo convierte en un lenguaje ampliamente utilizado en campos como el desarrollo de software, análisis de datos, inteligencia artificial y más.

---

### Capítulo 2: **Trabajar con diferentes *data types***

El objetivo de este capítulo es descubrir los diferentes tipos de datos en Python, y saber cuándo y cómo utilizarlos. Los tipos de datos son los siguientes:

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
Normalmente, enmarcamos los *strings* entre dos comillas dobles, de tal forma que así, podemos evitar falsas delimitaciones al usar otros caracteres especiales como las comillas simples. Ahora bien, al tener un string muy largo, enmarcamos el string entre tres comillas dobles para poder hacer saltos de línea, de forma que el texto sea más legible:
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
Otro atributo de las listas es que son elementos ordenados, lo que implica que podemos acceder a los diferentes elementos que conforman una lista mediante el índice** que ocupa dicho elemento. Hay que aclarar que el índice de elementos siempre empieza por **cero**:
```
# Mostrar el valor del primer y del tercer indice:

precios[0] # 10

precios[2] # 30
```
**Pequeño truco:** No necesitamos contar cuantos elementos hay en una lista, podemos acceder a los elementos de manera inversa indicando el índice en negativo:
```
# Mostrar el último valor de la lista:

precios[-1] # 40
```

En el caso de necesitar mostrar múltiples elementos, podemos hacerlo indicando dos puntos entre los diferentes índices que queremos:
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
- **Diccionarios:** Los diccionarios son una estructura de datos formada por dos componentes, la **clave** y el **valor**. Mientras las *listas* se compongan de diferentes elementos *individuales*, los diccionarios, al igual que su versión física, se componen de una palabra, lo que sería la *clave*, y una definición, el *valor*. Esta estructura de datos se encapsula entre dos llaves, ```{}```:
```
# Diccionario asociando un producto con su precio:

prod_prec = {"P1":10, "P2":20,
             "P3":30, "P4":40,
             "P5":50, "P6":60}
```
Este tipo de dato no utiliza una indexación numérica, como las listas. Para poder acceder a los valores que el mismo diccionario contiene, accedemos refiriéndonos a la clave asociada al valor:
```
# Ver el precio del producto "P4":

prod_prec["P4"] # 40
```
Ahora bien, en algunos casos podemos querer ver el listado completo de productos, siguiendo el ejemplo, o por el contrario, el listado de precios de los productos. Para poder obtener toda esa información, podemos hacerlo así:
```
prod_prec.key() # dict_keys(['P1', 'P2', 'P3', 'P4', 'P5', 'P6'])

prod_prec.value() # dict_values([10, 20, 30, 40, 50, 60])

print(prod_prec)
```

**Pequeño truco:** Podemos aplicar con los diccionarios es el hecho de generar una lista compuesta por todas las asociaciones clave-valor que tiene el diccionario:
```
prod_prec.items() # dict_items([('P1', 10), ('P2', 20), ('P3', 30), ('P4', 40), ('P5', 50), ('P6', 60)])
```
Comentar que, esta lista está compuesta por diferentes paréntesis que encapsulan los conjuntos clave-valor. Eso implica que la lista está compuesta por diferentes *tuplas*, que es un tipo de dato que veremos más adelante.

Pero los diccionarios pueden, y a veces deben, de ser modificables. De tal forma, podemos llegar a necesitar modificar un valor o añadir uno nuevo. Podemos hacerlo así:
```
# Añadimos un nuevo producto con su precio:

prod_prec["P7"] = 70

# Actualizamos el precio de un producto:

prod_prec["P6"] = 50
```

**¡¡¡IMPORTANTE!!!**: LOS DICCIONARIOS NO ACEPTAN CLAVES DUPLICADAS, estas deben de ser únicas.

- **Set:** Es un tipo de dato en python que **almacena valores únicos**. Los valores contenidos en el *set* no pueden cambiar, por lo que una vez se han generado son inalterables. Pese a ello, podemos eliminar o añadir nuevos valores. 
Este tipo de dato es especialmente útil para eliminar valores duplicados de un conjunto de datos. Los datos en los *sets* se almacenan de forma desordenada, haciéndolos bastante rápidos a la hora de buscar valores en su interior, pero no son indexables. Esta estructura de datos se encapsula entre dos llaves, ```{}```:
```
# Invitados a un evento:

invitados = {"Isaac", "Natxo",
             "Marc", "Alberto",
             "Marcia", "Hicham"}

print(invitados)
```

Dadas las propiedades que tienen los sets, podemos necesitar en algún momento convertir otros tipos de datos a *set*. Esto lo llamamos **casting**:
```
lista_invitados = ["Isaac", "Natxo",
            "Marc", "Alberto",
            "Marcia", "Hicham", "Isaac"]

# Convertimos la lista en un set:

invitados_VIP = set(lista_invitados)

# Comprobamos que tipo de dato es "invitados_VIP":
type(invitados_VIP) # <class 'set'>
```
Pese al hecho de que **los valores contenidos en los sets no pueden tener índices**, hay funciones bastante útiles a la hora de tratar con ellos:
```
# Ordenar un set:

sorted(invitados_VIP) # ['Alberto', 'Hicham', 'Isaac', 'Marc', 'Marcia', 'Natxo']
```

- **Tuplas:** Este es otro tipo de dato que tiene una peculiaridad significativa, es **inmutable**. A diferencia del *set*, donde los valores son los inmutables, las tuplas no pueden ser modificadas de ninguna de las formas. No se puede añadir valores, eliminarlos o modificar ningún tipo de datos o elemento contenido por una tupla, que una vez creada es inalterable. 
También podemos diferenciarlo de los *sets* en el hecho de que están ordenados, de forma que no son indexables. Este dato es especialmente útil cuando pretendemos almacenar datos que de ninguna de las formas deben o pueden ser alterables, como contraseñas. Los datos de las tuplas son almacenados entre dos paréntesis, ```()```:
```
# Almacenamos las localizaciones de oficinas:

ofi_localizacion = ("Barcelona", "Madrid", "Bilbao", "Malaga")

ofi_localizacion[2] # Bilbao 

# Convertir una lista en una tupla:

2_tupla = tuple(my_lista)
```

##### **RESUMEN:**

| Estructura de datos | Sintaxis     | Inmutable | Permite valores duplicados | Ordenada | Indexación con  [..] |
|----------------------|-------------|-----------|----------------------------|----------|--------------------|
| Lista (List)        | [1, 2, 3]   | No        | Sí                         | Sí       | Sí - por índice    |
| Diccionario (Dict)  | {clave:valor} | No      | Sí                         | Sí       | Sí - por clave     |
| Conjunto (Set)      | {1, 2, 3}   | No        | No                         | No       | No                 |
| Tupla (Tuple)       | (1, 2, 3)   | Sí        | Sí                         | Sí       | Sí - por índice    |

---

### Capítulo 3: **Estructuras condicionales y bucles**

- **Estructuras condicionales:** Son fragmentos de código que nos permiten generar un flujo de trabajo en función de una operación *booleana*, ```True/False```:
```
# Unidades vendidas y objectivos de ventas:
u_vend = 1600
obje_vend = 1500

    #Operacion booleana principal
if u_vend > obje_vend:
    print("Objectivo alcanzado")

    #Operacion booleana alternativa
elif u_vend >= 1000:
    print("Objetivo casi alcanzado")

    #En caso negativo ejecutara este fragmento
else:
    print("No has alcanzado el objetivo")
```

- **Bucles:** Son fragmentos de código que nos permiten iterar sobre si mismos en funcion de ciertas condiciones. Los bucles también nos permiten introducir otros fragmentos de código en su interior. Cuando hablamos de bucles, hay de dos típos:

    - **Bucles *for*:** Iteramos sobre una cantidad de valores finita y conocida. Es especialmente útil para listas con un número de valores determinado:
    ```
    precios = [1,4,6,2,3]

    for precio in precio:
        print("El precio es ", precio)
    ```
    En el ejemplo anterior podemos entender que por cada iteración mostramos el valor de *precio* en ese momento.

    **Pequeño truco:** En el caso de querer iterar sobre *diccionarios*, hay una forma especialmente útil de hacerlo mediante el método ```*.items()```:
    ```
    dict = {1:"Hicham", 2:"Ana", 3:"Manolo", 4:"Vicky"}

    for key,value in dict.items(): 
        print(key,value)

        # Son aplicables el resto de métodos de diccionarios.
    ```
    Si además queremos modificar el contenido de una estructura de datos como podría ser una lista, podemos hacerlo con ```range()```, una función integrada de python:

    ```
    # Mostrar los números entre el 1 y el 5
    
    for num in range(1,6): # El primer digito es el inicio
                           # El segundo digito es el último del rango, este no se cuenta (n-1)
        
        print(num) # 1,2,3,4,5
    
    ```

    - **Bucles *while*:** En este caso iteramos siempre y cuando se cumpla una determinada condición, podríamos decir que es un bucle *booleano*. Se utiliza cuando no sabemos cuantas veces debemos de iterar:

    ```
    valor_max = 10

    num_compras = 0

    # Queremos seguir comprando acciónes hasta que llegue a "x" precio:

    while num_compras < valor_max:

        # Aumentamos nuestras posciónes:
        num_compras += 1
    ```

    **¡¡¡IMPORTANTE!!!**: Si no llega a cumplirse nunca la condición del bucle **while**, el bucle iterará **HASTA EL INFINITO**.

    Para evitar entrar en un bucle perpetuo, hay un metodo que podemos utilizar para finalizar el bucle antes de tiempo y salir:
    ```
    while num_compras < valor_max:

        # Queremos dejar de comprar cuando llegue a 7:
        if num _compras == 7:

            break #Esto termina el bucle repentinamente
    
        num_compras += 1
    ```
    
---


### Capítulo 4: **Flujos de trabajo**

Una vez ya hemos aprendido los diferentes tipos de datos, lo que implican las estructuras condicionales y como iterar, hay formas mas avanzadas y rapidas de hacer todo lo que hemos aprendido previamente. Algunas de estas formas:

- ```in```: Comprueba si el valor se encuentra en una variable o estructura de datos:
```
prod_prec = {
    "aa":10,"bb":20,
    "cc":30,"dd":40,
    "ee":50,"ff":60
}

if "dd" in prod_prec: # 
    print("dd","price is",prod_prec["dd"])
```

- ```not```: Comprueba que un valor no se encuentra en una variable o estructura de datos:
```
prod_prec = {
    "aa":10,"bb":20,
    "cc":30,"dd":40,
    "ee":50,"ff":60
}

if "hh" not in prod_prec: # 
    print("hh","price not expected")
```

- ```and``` y ```or```: Estas dos palabras comprueban que la condición booleana se cumple **si y solo si** se dan ambas condiciones, en el caso del ```and```, o **si se cumple una de las dos**, en el caso del ```or```.

- ```append(...)```: Esto es una función especifica para **listas**, y nos permite añadir valores a una lista preexistente:
```
prod = []

# Imaginamos que tenemosun diccionario preexistente:
for key,val in dicc_prod:
    
    # Queremos los productos de un determinado precio:
    if val == 20:
        prod.append(key)

print(prod) # Mostrará solo los productos con un precio de 20
```
## 4. Ejercicios / Prácticas

- Descripción breve de cada ejercicio trabajado.  
- Enlaces a notebooks o scripts.  
- Acerca de lo que he aprendido haciendo los ejercicios.  

---

---

## 5. Recursos adicionales

- Enlace al curso oficial en DataCamp  
- Materiales complementarios, documentación, lecturas recomendadas.  
