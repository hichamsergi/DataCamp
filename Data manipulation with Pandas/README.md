# 📘 Data manipulation with Pandas

## 1. Descripción

Pandas es la biblioteca de Python más popular del mundo, utilizada para todo, desde la manipulación hasta el análisis de datos. En este capítulo aprenderas a utilizar las diferentes herramientas que esta nos proporciona para poder manipular DataFrames.

---

## 2. Índice

1. [Transformación de DataFrames](#capítulo-1-transformación-de-dataframes)
2. [Agregar DataFrames](#capítulo-2-agregar-dataframes)
3. [Segmentar e indexar DataFrames](#capítulo-3-segmentar-e-indexar-dataframes)
4. [Crear y visualizar DataFrames](#capítulo-4-crear-y-visualizar-dataframes)

---

## 3. Apuntes

### Capítulo 1: **<ins>Transformación de DataFrames</ins>**
Como ya sabemos, la estructura de un *DataFrame* es rectangular, organizada en filas y columnas. Las filas, representan los registros de información individual. Las columnas, representan diferentes atributos o variables de los registros mencionados. Para poder hechar un primer vistazo a un *DataFrame*, podemos utilizar el método `head`, este nos mostrará los primeros 5 registros:
```python

my_dataframe.head()


Dia	Entrada	Salida	Duracion	Tipo
0	1	NaN	NaN	NaN	Ausencia
1	2	NaN	NaN	NaN	Ausencia
2	3	NaN	NaN	NaN	Ausencia
3	4	NaN	NaN	NaN	Ausencia
4	5	NaN	NaN	NaN	Ausencia

```

Como podemos ver, al igual que los indices de las listas, los *DataFrames* empiezan por indice 0.

Otro método importante para poder entender mejor nuestros *DataFrames*, es `info`. Este nos muestra los nombres de las columnas, el tipo de dato que contienen y si estas tienen algun valor nulo.
```python
my_dataframe.info()
```

También podemos acceder a los atributos del *DataFrame*, como `shape`. Estos se indican sin el parentesis final que ponemos en los métodos. En concreto, `shape`, nos da la información de la "forma" del *DataFrame*, indicandonos el número de filas, seguido del número de columnas. 

```python
my_dataframe.shape
```

Los atributos de los *DataFrames* también nos pueden proporcionar información importante. Por ejemplo, `my_dataframe.values`, nos generará una matriz *NumPy* bidimensional con la información de nuestro *DataFrame*.

`my_dataframe.columns` y `my_dataframe.index`, contienen los nombes de las columnas y números de fila, respectivamente.




### Capítulo 2: **<ins>Agregar DataFrames</ins>**

### Capítulo 3: **<ins>Segmentar e indexar DataFrames</ins>**

### Capítulo 4: **<ins>Crear y visualizar DataFrames</ins>**
