# 📘 Streamlined Data Ingestion with Pandas

## 1. Índice

1. [Importación de datos de archivos planos](#capítulo-1-importación-de-datos-de-archivos-planos)
2. [Importación de datos de archivos Excel](#capítulo-2-importación-de-datos-de-archivos-excel)
3. [Importación de datos de Bases de Datos](#capítulo-3-importación-de-datos-de-bases-de-datos)
4. [Importación de datos JSON y trabajo con APIs](#capítulo-4-importación-de-datos-json-y-trabajo-con-apis)

------

## 2. Apuntes

### Capítulo 1: **<ins>Importación de datos de archivos planos</ins>**

La función que más hemos utilizado para poder importar datos desde un documento, puede haber sido `.read_csv(...)`. Si bien, la forma más común de utilizarla es para importar documentos de tipo CSV, también se puede utilizar para importar cualquier tipo de archivo plano. Utilizando el argumento `sep="..."`, podemos definir el separador que utilice nuestro documento para poder leer el archivo:

```python
import pandas as pd

tax_data = pd.read_csv(`us_tax_data_2016.tsv`, sep="\t")
```

De todas formas, es comprensible que no necesitemos todo el contenido del *DataFrame*, por lo que debemos saber como limitar la importación de datos para ser más eficientes. Podemos hacerlo con `usecols` de la siguiente forma:

```python
columnas_utiles = ['STATE', 'N1', 'zipcode']

data = pd.read_csv('us_tax_data_2016.csv', usecols=columnas_utiles)
```

De esta forma, solo importamos los datos contenidos en las columnas con los nombres definidos en la lista. 

Pero podemos limitar aun más los datos recogidos, digamos que solo queremos los primeros 1000 registros. `nrows`, nos recogerá los 1000 primeros registros del fichero que le proporcionemos:

```python

data_w_column_names = pd.read_csv('us_tax_data_2016.csv', nrows=1000)
```

Pero `nrows` es especialmente útil cuando se utiliza con us homónimo `skiprows`:

```python

data = pd.read_csv('us_tax_data_2016.csv', 
    nrows=200, 
    skiprows=1000,
    header=None)
```

Así pues, de esta forma recogemos los primeros 200 registros a partir del 1000 registro. Teniendo en cuenta que asumimos que no hay encabezado en las columnas.

Tomemos como ejemplo el dataset anterior, en el que no tenemos nombres de columnas, y contiene 200 registros. Vamos a dar nombre a esas columnas recogiendo el nombre de las columnas del dataset previo:

```python

column_names = list(data_w_column_names) #Atajo para recoger los nombres de las columnas

data = pd.read_csv('us_tax_data_2016.csv', 
    nrows=200, 
    skiprows=1000,
    header=None,
    names=column_names)
```

Como estamos viendo, una de las formas más eficiente de tratar datos con Pandas, es cargarlos correctamente y de forma selectiva. Esto, muchas veces pasa por indicar el tipo de dato que se va a proporcionar en una determinada columna, de esta forma evitamos errores de tipología de dato:

```python

df = pd.read_csv("us_tax_data_2019.csv", dtype={"zipcode": str})
```

Así pues, cuando procesamos la columna **zipcode** indicamos que ese dato es un string. De esta forma forma datos como los ceros situados a la izquierda no se verán eliminados.

Pero rellenar la información que consideramos errónea por valores faltantes, *NaN*, puede ser útil cuando nos encontramos con datos como un *0* en columnas como el código postal:

```python
df = pd.read_csv("us_tax_data_2019.csv", na_values={"zipcode": 0})
```

Mediante el argumento `na_values`, indicamos que queremos rellenar los valores que sean como *NaN*. De esta manera evitamos que un dato erróneo sea considerado como correcto o valido.


Pero un *DataFrame* es muy grande y puede contener errores múltiples que pueden pasarse por alto. Por eso, indicar lo que queremos que haga Pandas al procesarlos es imprescindible para evitar que los scripts se vean interrumpidos:

```python
df = pd.read_csv("us_tax_data_2019.csv", 
        error_bad_lines=False,
        warn_bad_lines=True)
```

En estos casos, los siguientes argumentos indican cosas diferentes:

* `error_bad_lines`: Omitimos las líneas incorrectas, cargamos el resto. Básicamente nos pregunta si queremos añadir las líneas erróneas, y nosotros respondemos `False`, indicando NO, o `True`, indicando si y generando los errores esperados.

* `warn_bad_lines`: Mostramos un mensages cuando haya una línea incorrecta. Por lo que cada vez que encuentre una nos lo notificará. 

### Capítulo 2: **<ins>Importación de datos de archivos Excel</ins>**

Es muy común que en los archivos Excel haya más de una hoja, cada una con los datos pertinentes, pero `read_excel` únicamente importa la primera si no le indicamos lo contrario. Es por eso que Pandas ofrece la posibilidad de indicar la hoja de la que queremos recoger los datos.

Utilizando el argumento `sheet_name`, dentro de `read_excel()`, podemos indicar no solo el nombre de la hoja que queremos recoger, sino también el índice que esta ocupa, o una lista de ellos para poder importar varias hojas.

```python
data = pd.read_excel('fcc_data.xlsx',
                        sheet_name=1)

data = pd.read_excel('fcc_data.xlsx',
                        sheet_name='2026')      
```

Pero, *como podemos hacer para importar todas las hojas?*. Es apregunta, se responde facilmente y utilizando el mismo argumento que acabamos de aprender, `sheet_name=None`:

```python
data = pd.read_excel('fcc_data.xlsx',
                        sheet_name=None)  
```

El problema de utilizar este método es que realmente no importamos un *DataFrame* con toda la infromación. Lo que realmente recibimos es un diccionario ordenado con pares clave valor que corresponden a el nombre de la hoja, como clave, y un *DataFrame*, como valor.

Si queremos organizarlo todo en un mismo *DataFrame* deberemos realizar algun paso extra:

```python

todas_hojas = pd.DataFrame() #DataFrame vacio

for sheet_name, data_f in data.items():

    data_f["Year"] = sheet_name

    todas_hojas = pd.concat([todas_hojas, data_f])
```

Pero en el capítulo anterior hemos aprendido a como indicar que queremos importar un determinado tipo de datos, con `dtype`. Pero los datos booleanos requieren una mencion especial, no por el hecho de ser binarios, o **True** o **False**, sino por el hecho de que algunas veces podemos verlos representados de diferentes formas, como **Yes** o **No**.

Este tipo de casos, en los que no se indica explicitamente **True** o **False**, son en los que nos vamos a concentrar. Con el argumento `true_values`, podemos indicarle los valores que consideremos como **True**, proporcionandole una lista:

```python
data = pd.read_excel('fcc_data.xlsx',
                        true_values=['Yes'],
                        false_values=['No'])  
```
Pese a ello, la conversión debe valorarse y considerar las posibles implicaciones de la conversión, dado que las operaciones que se lleven a cabo sobre el dataset basadas en datos booleanos pueden tener un impacto no deseado.

### Capítulo 3: **<ins>Importación de datos de Bases de Datos</ins>**

### Capítulo 4: **<ins>Importación de datos JSON y trabajo con APIs</ins>**
