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

#### 1.1) **<ins>Clasificacicion y subconjuntos</ins>**:
Las necesidades de estructura de los *DataFrame* dependen de cada situación, por ese motivo, la clasificación de la información es importante. Podemos ordenar nuestro *DataFrame* de diferentes formas:

* `my_dataframe.sort_values("column_name")`: Este método nos permite organizar los registros de un *DataFrame* en función de los valores contenidos en una columna. Añadiendo el argumento `ascending=False`, podemos organizarlo de forma inversa, de mayor a menor. Proporcionando una lista, como argumento para la ordenación, podemos ordenar por tantas columnas como valores contenga esa lista.

* `my_dataframe["columna1"]`: De esta forma, accederemos únicamente a la columna indicada entre corchetes. Si queremos acceder a varias columnas únicas, debemos de convertir el valor contenido en una lista con los nombres deseados. 

Subconjuntar registros también es posible si utilizamos operadores lógicos conocidos:

* `my_dataframe[my_dataframe["column1"] > 50]`: En esta operación, obtendremos los registros de nuestro *Dataframe*, que contengan un valor superior a 50 en la columna `column1`.

* `my_dataframe["color"].isin(["Red","Blue"])`: Mostramos los registros que únicamente tienen el valor "*Red*" o "*Blue*" en la columna "*color*".

* `dogs[(dogs["height_cm"] > 60) & (dogs["color"] == "tan")]`: Esta es la sintaxis para generar una salida en la que únicamente se cumplan ambas condiciones.

* Tambien podemos almacenar una condición dentro de una variable que posteriormente podemos aplicar para generar subconjuntos:

```python
colors = ["brown", "black", "tan"]
condition = dogs["color"].isin(colors)
dogs[condition]
```

#### 1.2) **<ins>Nuevas columnas</ins>**:
Muchas veces el contenido de un *DataFrame* no es suficiente y necesitamos añadir nuevas columnas con contenido de columans derivadas de columnas existentes. Por ejemplo, transformar la unidad de medida:

```python
my_dataframe["peso_Kg"] = my_dataframe["peso_G"] / 1000
```

La fuerza de *Pandas* está en el hecho de mezclar las herramientas para subconjuntar y la generación de nuevas columnas.


### Capítulo 2: **<ins>Agregar DataFrames</ins>**
Como ya sabemos extraer columnas, dividirlas e incluso añadirlas, vamos a concentrarnos en los mismos datos que las componen. Podemos extraer información generica de todo un *DataFrame*, con la función `my_df.describe()`:

```python
         individuals  family_members     state_pop
count      51.000000       51.000000  5.100000e+01
mean     7225.784314     3504.882353  6.405637e+06
std     15991.025083     7805.411811  7.327258e+06
min       434.000000       75.000000  5.776010e+05
25%      1446.500000      592.000000  1.777414e+06
50%      3082.000000     1482.000000  4.461153e+06
75%      6781.500000     3196.000000  7.340946e+06
max    109008.000000    52070.000000  3.946159e+07
```

Como podemos ver, nos proporciona información general, y dicha información puede ser excesiva. De cualquier forma, podemos acceder pormenorizadamente a todos esos componentes que nos muestra `describe`:

```python
my_df["column1"].mean() #Media

my_df["column1"].median() #Mediana


my_df["birth_date"].min()
```

Y como con las funciones própias, podemos personalizar nuestras mismas funciones. Esto lo hacemos con el método `.agg`, de la siguiente forma:

```python
def pct30(column) #Definimos el método .agg
    return column.quantile(0.3)

my_df["columna3"].agg(pct30) #Este método calculará el percentil 30 de la columna 3

my_df[["columna3","columna7"]].agg(pct30) #Aplicamos el método a las dos columnas
```

De la misma forma que hemos visto en el último ejemplo, no solo podemos trasladas varias columnas a un método, sino también varios métodos a una única columna: 

```python
my_df["peso_kg"].agg([pct30, pct40])
```

Dado que la estadística puede contener valores necesariamente acumulativos, como sumas totales de diferentes líneas de registros referentes a pesos, por ejemplo. Hay diversas funciones ya conocidas que podemos aplicar este añadido acumulativo:

```python
my_df["col1"].cumsum()
my_df["col1"].cummax()
my_df["col1"].cummin()
my_df["col1"].cumprod()
```


### Capítulo 3: **<ins>Segmentar e indexar DataFrames</ins>**

### Capítulo 4: **<ins>Crear y visualizar DataFrames</ins>**
