# Limpiar datos para una campaña de marketing bancario

El proyecto pretende realizar una recolecta de datos de un documento para poder extraer información útil para una campaña de marketing. Podemos encontrar el proyecto y toda su descripción en [`notebook.ipynb`](notebook.ipynb). La información útil se ha dividido en 3 documentos diferentes:

- ## `client.csv`:

    | columna | tipo de dato | descripción | requisitos de limpieza |
    |---------|--------------|-------------|----------------------- |
    | `client_id` | `entero` | ID del cliente | N/A |
    | `age` | `entero` | Edad del cliente en años | N/A |
    | `job` | `objeto` | Tipo de trabajo del cliente | Cambiar `"."` por `"_"` |
    | `marital` | `objeto` | Estado civil del cliente | N/A |
    | `education` | `objeto` | Nivel de educación del cliente | Cambiar `"."` por `"_"` y `"unknown"` por `np.NaN` |
    | `credit_default` | `bool` | Si el crédito del cliente está en default | Convertir a tipo de dato `booleano`:<br> `1` si `"yes"`, de lo contrario `0` |
    | `mortgage` | `bool` | Si el cliente tiene una hipoteca existente (préstamo hipotecario) | Convertir a tipo de dato booleano:<br> `1` si `"yes"`, de lo contrario `0` |

    En el notebook se describe la construcción el siguiente *DataFrame*:

    |	client_id | age	| job | marital | education | credit_default | mortgage |
    |-----------|-----|-----|---------|-----------|----------------|----------|
    |   0 |	56 | housemaid | married | NaN | 1 | 0 |
    |	1 | 57 | services | married	| high_school | 0 |	0 |
    |	2 | 37 | services | married	| high_school |	0 |	1 |
    |	3 | 40 | admin_ | married | basic_6y |0 | 0 |
    |	4 | 56 | services | married | high_school | 0 | 0 |
    |...|...|...|...|...|...|...|


- ## `campaign.csv`:

    | columna | tipo de dato | descripción | requisitos de limpieza |
    |---------|--------------|-------------|------------------------|
    | `client_id` | `entero` | ID del cliente | N/A |
    | `number_contacts` | `entero` | Número de intentos de contacto al cliente en la campaña actual | N/A |
    | `contact_duration` | `entero` | Duración del último contacto en segundos | N/A |
    | `previous_campaign_contacts` | `entero` | Número de intentos de contacto al cliente en la campaña anterior | N/A |
    | `previous_outcome` | `bool` | Resultado de la campaña anterior | Convertir a tipo de dato `booleano`:<br> `1` si `"success"`, de lo contrario `0`.                                |
    | `campaign_outcome` | `bool` | Resultado de la campaña actual | Convertir a tipo de dato `booleano`:<br> `1` si `"yes"`, de lo contrario `0`. |
    | `last_contact_date` | `datetime` | Última fecha en la que se contactó al cliente | Crear combinando `day`, `month` y una nueva columna `year` (con valor `2022`); <br> **Formato =** `"YYYY-MM-DD"` |

    En el notebook se describe la construcción el siguiente *DataFrame*:

    | client_id	| number_contacts | contact_duration | previous_campaign_contacts | previous_outcome | campaign_outcome | last_contact_date |
    |-----------|-----------------|------------------|----------------------------|------------|-----------------|------------------|
    | 0	| 1	| 261 |	0 |	1 |	0 |	2022-May-13 |
    | 1	| 1	| 149 |	0 |	0 |	0 |	2022-May-19 |
    | 2	| 1	| 226 | 0 |	0 |	0 |	2022-May-23 |
    | 3	| 1	| 151 | 0 |	0 |	0 |	2022-May-27 |
    | 4 | 1	| 307 | 0 |	0 |	0 |	2022-May-3 |
    |...|...|...|...|...|...|...|


- ## `economics.csv`:

    | columna | tipo de dato | descripción | requisitos de limpieza |
    |---------|--------------|-------------|------------------------|
    | `client_id` | `entero` | ID del cliente | N/A |
    | `cons_price_idx` | `float` | Índice de precios al consumidor (indicador mensual) | N/A |
    | `euribor_three_months` | `float` | Tasa Euribor a tres meses (indicador diario) | N/A |

    En el notebook se describe la construcción el siguiente *DataFrame*:

    | client_id | cons_price_idx | euribor_three_months |
    |-----------|----------------|----------------------|
    | 0	| 93.994 | 4.857 |
    | 1	| 93.994 | 4.857 |
    | 2	| 93.994 | 4.857 |
    | 3	| 93.994 | 4.857 |
    | 4 | 93.994 | 4.857 |
    |...|...|...|


## Anotaciones del proyecto:

* #### *Diferencias entre la celda y su contenido*:

    - **`df.replace()`**: Reemplaza el **valor completo** de la celda. Funciona en cualquier tipo de dato (números, texto, $\text{NaN}$).
    <br>

    - **`df.str.replace()`**: Reemplaza una **porción de texto dentro del valor** de la celda. Solo funciona en columnas de texto.

* #### *Aplicar funciones especificas a los valores de las celdas*:

    - **`df.apply(lambda_f)`**: Indicando la columna del *DataFrame*, como `df`, aplicamos una función lambda a todos los registros de la columna.

* #### *Rellenar, eliminar y renombrar celdas y columnas*:

    - **`df.fillna("cualquir_cosa")`**: Rellenamos las celdas vacias por el valor contenido en el paréntesis.
    <br>

    - **`df.drop(columns=["nombre"])`**: Elimina las columnas con el/los nombres contenidos en la lista.
    <br>

    - **`df.rename(columns={"antiguo":"nuevo"})`**: Renombra la/las columnas con el nombre del valor indicado como `antiguo`, por el valor indicado como `nuevo`.

* #### *Cambiar el tipo de dato en la celda*:

    - **`df.adtype(str)`**: Transforma el tipo de valor contenido en las celdas del *DataFrame* por el indicado entre paréntesis.