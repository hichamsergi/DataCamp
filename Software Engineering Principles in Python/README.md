# 📘 Git

## 1. Índice

1. [Ingeniería de software y ciencia de datos](#capítulo-1-ingeniería-de-software-y-ciencia-de-datos)
2. [Escribir un módulo Python](#capítulo-2-escribir-un-módulo-python)
3. [Utilización de clases](#capítulo-3-utilización-de-clases)
4. [Mantenibilidad](#capítulo-4-mantenibilidad)

------

## 2. Apuntes

### Capítulo 1: **<ins>Ingeniería de software y ciencia de datos</ins>**

La ingeniería de software, es la rama de la ingeniería encargada del desarrollo, operación y mantenimiento de los programas informáticos. Para poder hacer estas tareas de forma correcta, se fundamenta en 3 pilares esenciales:

* **Modularidad**: El código modular es un código que se divide en unidades funcionales, cortas y fáciles de leer e interpretar.

* **Documentación**: La documentación es la parte de nuestro código que, sin ejecutarse, nos ayuda a entender que proposito tiene y como este debe interpretarse.

* **Pruebas automatizadas**: Nos ayuda a encontrar y corregir errores de forma rápida. Ahorra mucho tiempo frente a cualquier prueba manual y puede ejecutarse en cualquier momento.

Por lo tanto, en base a estos principios se construye el resto. Pero esto es pura teorica de los conceptos básicos. Lo interesante es como esto nos afecta como usuarios de software.

Para entender como los principios descritos anteriormente afectan al software que utilizamos, podemos hacer una pequeña prueba con un paquete que ya conocemos, **Numpy**:

```shell
pip install numpy #Descargamos el paquete y sus dependencias
```

Cuando el paquete ya se instala, podemos ejecutar el siguiente comando:

```python
import numpy as np

help(np.busday_count)
```

El comando anterior nos mostrarà toda la documentación relativa a la función `busday_count`. Es en el texto de salida donde podremos ver información como la descripción de la misma función, los parámetros de entrada que espera recibir, lo que la función nos retorna y algún ejemplo de ejecución.

Los paquetes no siempre tienen documentación, pero como podemos ver, es de agradecer y hace muy simple la interpretación del mismo.

De todas formas, adicionalmente a los principios que hemos descrito, hay una guía de estilo oficial de Pyhton donde se describe como debemos articular nuestro código para que sea limpio, coherente y fácil de leer, **PEP 8**.

**PEP 8**, es muy extensa con múltiples principios e indicaciones. Para que nos sea más fácil aplicarlos tenemos una libreria que nos señalará todos los puntos en los que se incumple un principio PEP 8, `pycodestyle`:

```python

pip install pycodestyle

pycodestyle my_script.py #Señala todas las infracciones de PEP 8
```

Al ejecutar el comando anterior, tendremos una salida similar a esta:

```shell
my_script.py:2:15: E261 at least two spaces before inline comment
my_script.py:5:16: E262 inline comment should start with '# '
my_script.py:11:1: E265 block comment should start with '# '
my_script.py:13:2: E114 indentation is not a multiple of four (comment)
my_script.py:13:2: E116 unexpected indentation (comment)
```

Como se puede ver en el ejemplo, nos señala los puntos en concreto donde estamos incumpliendo los principios PEP 8.

### Capítulo 2: **<ins>Escribir un módulo Python</ins>**

Ya hemos aprendido qué son los principios PEP 8. También hemos visto que ciertas funciones requieren de la instalación de paquete. Pero, qué es un paquete?

A niveles básicos, es una carpeta donde podemos encontrar un archivo de Python. El nombre de la carpeta corresponde al nombre del paquete, y las funciones, son las que podemos encontrar dentro de los archivos del directorio.

Ahora bien, para poder utilizar correctamente las funciones de nuestros archivos Python, debemos nombrarlo a un archivo de una forma determinada, `__init__.py`. Nombrandolo así, indicamos a Python que el directorio corresponde a un paquete y este puede ser importado igual que Numpy o Pandas.

De todas formas, si queremos hacer que nuestro paquete se pueda utilizar por cualquier otra persona hacen falta otros dos archivos, `setup.py` y `requisitos.txt`. Estos dos archivos se deben situar al mismo nivel que el directorio del paquete. 

* `requisitos.txt`: Mostrará como crear el entorno necesário para usar correctamente nuestro paquete. Dependencias de otros paquetes o versiones determinadas de Python, son algunos de los ejemplos de contenido que podemos añadir a este archivo. Ejemplo:

```
matplotlib
numpy==1.15.4
pycodestyle>=2.4.0
```

Ahora, podemos ejecutar la instalación de los requerimientos de nuestro paquete de la siguiente forma:

```shell
pip install -r requirements.txt
```

* `setup.py`: Es lo que le indica a pip como instalar nuestro paquete. Un ejemplo puede ser el siguiente:

```python
from setuptools import setup

setup(name='my_package',
      version='0.0.1',
      description='Un paquete de ejemplo para DataCamp.',
      author='Hicham Varo',
      author_email='examplehicham@gmail.com',
      packages=['my_package'],
      install_requires=['matplotlib',
                        'numpy==1.15.4',
                        'pycodestyle>=2.4.0'])
```

### Capítulo 3: **<ins>Utilización de clases</ins>**

Ahora ya sabemos como crear un módulo própio de Python, vamos a ver qué son las clases y como estas nos pueden ser útiles para la construcción de módulos.

Una clase es un mólde que define los atributos esenciales que debe tener un objeto para poder ser creado y cumplir su función dentro de nuestro código. Por ejemplo:

```python

class EquipoFut:

    def __init__(self, nombre, historial_goles, formacion_habitual):
        # Cada equipo que guardes en esta "caja" tendrá de forma obligatoria esto:
        self.nombre = nombre
        self.goles = historial_goles
        self.formacion = formacion_habitual
```

Así pues, hemos definido una clase que nos permitirá crear un equipo de fútbol, el objecto, pero para que este se pueda crear deberá tener `nombre`, `historial de goles` y `formación habitual`. Podemos crear un equipo de la siguiente forma:

```python

barca = EquipoFut('FC Barcelona', [2, 3, 4, 5], "4-3-3")

barca.nombre
barca.historial_goles
barca.formacion_habitual
```

De la forma descrita anteriormente podemos crear al equipo `FC Barcelona`, con los atributos descritos, y también acceder a cualquiera de los atributos descritos en la clase. 


### Capítulo 4: **<ins>Mantenibilidad</ins>**