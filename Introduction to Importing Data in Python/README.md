# 📘 Introduction to Importing Data in Python

---

## 1. Descripción general

En este curso aprenderás las bases para importar datos a Python desde distintos formatos de archivo.
Conocerás cómo leer archivos planos, formatos estructurados como Excel o SAS, y también cómo conectarte a bases de datos relacionales mediante SQL.
Este conocimiento es esencial para cualquier perfil orientado al análisis de datos o ingeniería de datos.

--- 

## 2. Índice de capítulos

1. [Introducción y ficheros planos](#capítulo-1-introducción-y-ficheros-planos)
   - [Manipulación de documentos](#11-manipulación-de-documentos)
   - [Ficheros planos](#12-ficheros-planos)
2. [Importar datos de otros tipos de archivos](#capítulo-2-importar-datos-de-otros-tipos-de-archivos)
3. [Trabajar con bases de datos relacionales en Python](#capítulo-3-trabajar-con-bases-de-datos-relacionales-en-python)

---

## 3. Apuntes

### Capítulo 1: **<ins>Introducción y ficheros planos</ins>**

#### 1.1) **<ins>Manipulación de documentos</ins>**:
Para poder leer datos de ficheros planos, lo primero es aprender a manipular archivos en python. La forma de hacerlo es especialmente simple, simplemente los abrimos con la función ```open```. 

```open``` nos permite interactuar con el archivo del modo que le indiquemos como `r`, de *read* para solo leerlo, o `w`, de *write* para poder poder escribir sobre el mismo documento:

```python

filename = 'quijote.txt' # Asignamos el nombre del documento a una variable.

file = open(filename, mode='r') # Abrimos el archivo

texto = file.read() # De esta forma almacenamos todo el texto
                    # contenido en el archivo, dentro de la varible texto
file.close()
```

Como se puede ver en el fragmento de código anterior, al final utilizamos un cierre, `file.close()`. El cierre finaliza la función `open`, por lo que podemos decir que cerramos el fichero que hemos abierto. De esta forma, no solo nos aseguramos que todo los datos se guardan correctamente, sino que tambien ejercemos una buena práctica de programación en python.

Pese a ello, si somos un poco perezosos y no queremos tener que acordarnos de cerrar todos los documentos que abramos, podemos hacerlo con una declaración `with`. Esta nos permite ejecutar comandos dentro de la declaración, con el documento abierto, y además sin necesidad de tener que acordarnos de cerrar el documento una vez estamos fuera de la declaración:

```python
with open('quijote.txt', 'r') as file:
        
    print(file.read()) # Mostramos el contenido de la lectura del fichero.
```

#### 1.2) **<ins>Ficheros planos</ins>**:

Lo primero de todo es entender que es un archivo plano, estos **son archivos de texto basicos que contienen registros, datos de tablas sin relaciones estructuradas**.

Si profundizamos en los **registros**(*record*), veremos que cada uno corresponde a una línea del archivo que contiene diferentes datos, estos datos suelen estar separados por un **delimitador**, como `,` o `;`.

En cambio, las **columnas**(*column*), representan los atributos o campos que describen cada dato dentro de los registros.

Un ejemplo simple para entenderlo sería:

```
usuario,producto,precio
KM37,Teclado,25
PR19,Ratón,18
YU88,Pantalla,132
```



---

### Capítulo 2: **<ins>Importar datos de otros tipos de archivos</ins>**

---

### Capítulo 3: **<ins>Trabajar con bases de datos relacionales en Python</ins>**

---

