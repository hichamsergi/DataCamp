# Proyecto: Proceso ETL completo

Este proyecto pretende simular un proceso completo de ETL(*Extract Transform and Load*). La distribución del directorio es la siguiente:

- `../dirty_data/`: Este directorio contiene los datos en bruto de 4 fuentes diferentes:

    - `../dataset_ventas.csv`: Dataset que contiene *10000* registros de ventas en formato **CSV**.
    - `../dataset_ventas.json`: Dataset que contiene *10000* registros de ventas en formato **JSON**.
    - `../dataset_ventas.txt`: Dataset que contiene *10000* registros de ventas en formato **plano**, con *" |"* de separador.
    - `../dataset_ventas.xlsx`: Dataset que contiene *10000* registros de ventas en formato **Excel**, *xls*.

- `../processed_data/`: En este directorio se  alojaran los datasets, renombrados con el mismo nombre añadiendo el prefijo `processed_`.

- `../clean_BK/`: En este directorio se alojará un documento **CSV** con la recopilación de todos los datasets, limpios, haciendo la función de back up.

- `../base_datos/`: En este directorio se creará la base de datos con el contenido de los datasets, se llamará `sales_data.db`. Esta, se administrará con el *sistema de gestión de bases de datos relacionales* **SQLite**. 

- [ETL.ipynb](ETL.ipynb): Este archivo contendrá el script que creará la pipeline de datos y archivos. También tiene el paso a paso de todo el proceso para poder entender el desarrollo.

- [LOGGINGprocess_ETL.log](LOGGINGprocess_ETL.log): Archivo de logs donde se registra cada proceso que se ha llevado a cabo.
