# 📘 Git

## 1. Índice

1. [Conocimientos básicos](#capítulo-1-conocimientos-básicos)
2. [Trabajar con ramas](#capítulo-2-trabajar-con-ramas)
3. [Colaborar con Git](#capítulo-3-colaborar-con-git)

------

## 2. Apuntes

### Capítulo 1: **<ins>Conocimientos básicos</ins>**

Git es una de las herramientas colaborativas más poderosas a la hora de trabajar en equipos de desarrollo. Permite que varios desarrolladores trabajen con la misma información de un proyecto y para ello divide en diferentes periodos las fases de integración.

Para entenderse mejor como sucede esto, vamos a suponer que hay un repositorio Git general en el que se almacena todo el código de un proyecto en el que varios desarrolladores están interviniendo simultaneamente. Cada desarrollador tiene en su dispositivo personal una copia de el proyecto, en la que lo altera para poder añadir nuevas funcionalidades. Estas modificaciones sobre los documentos comunes que todos ellos comparten, pasan por 3 fases:

1. **Modificación (Modified)**: Modificación local de los archivos que realiza cada desarrollador en su propio equipo.

2. **Preparado (Staged)**: Fase en la que se decide que archivos modificados localmente van a ser compartidos.

3. **Confirmado (Commited)**: Almacenamos localmente los archivos modificados que hemos decidido que vamos a compartir.

Ahora que se comprenden las fases locales del archivo, vamos a entender como sería el flujo de trabajo normal en un repositorio. Empezemos por lo basico, **confirmar el estado del repositorio**, para ver que archivos se han modificado localmente respecto al último **commit**:

```shell
git status
```

El camando es bastante descriptivo, pedimos que nos de el estatus del proyecto. Este nos indica que archivos han sido modificados y cuales no, y cuáles estan en fase de **staging**.

Si por el motivo que sea queremos ver que modificaiones locales hemos aplicado a los archivos respecto a los que tenemos en **staging**:

```shell
git diff
```

Ahora imaginemos que hemos modificado un archivo localmente y lo quereos añadir a la fase de **staging**:

```shell
git add README.md #Si indicamos "." en vez de el nombre del archivo, subiremos todas las modificaciones hechas
```

Y de nuevo, podemos ver que modificaciones estan en **staging** que no hemos aplicado a la fase **commit**:

```shell
git diff --staged
```

En caso de equivocarnos con algún cambio realizado que no queramos "**commitear**" podemos ejecutar lo siguiente:

```shell

git restore archivo.md
```

Cuando ya tenemos claro las modificaciones **staged** que añadiremos a la fase **commit**, podemos ejecutar los siguientes comandos:

```shell

git commit -m "Mensaje"

git commit --amend -m "Nuevo mensaje" #De esta forma corregimos el menaje commit recien creado sin generar un commit nuevo
```

Y una vez lo tenemos todo, podemos ver el histórico de commits que hemos hecho linea por linea:

```shell

git log --oneline

git log -3 #Mostramos solo los 3 últimos commits
```

### Capítulo 2: **<ins>Trabajar con ramas</ins>**

Ahora que ya tenemos claro el funcionamiento de la gestión local de un repositorio, podemos empezar entender que son, y como funcionan las ramas.

Las **ramas** son versiones individuales y diferentes de nuestros archivos o proyectos que nos permiten llevar un control sistemático de los cambios que aplicamos. En cada rama, podemos tener diferentes versiones de nuestros archivos, las mismas o archivos completamente diferentes que no existan en otras ramas. 

Las ramas son especialmente útiles cuando pretendemos aplicar nuevas funcionalidades sin que estas puedan llegar a afectar a nuestro entorno de producción. Este entorno, por defecto, se llamará `main`. Pero, si queremos saber cuantas ramas existen, debemos ejecutar el siguiente comando:

```shell

git branch

# main
# * ai_assistant
#
#
```

La rama que aparece con un asterisco, nos indica que es la rama actual en la que nos encontramos. Si queremos cambiar y resituarnos en alguna en concreto:

```shell

git switch main
```

De esta forma, convertimos a `main` en la rama en la que nos encontramos, pero podemos localizarnos en cualquier otra.

Si, por el contrario, queremos crear una nueva, podemos hacerlo con el comando `branch` añadiendo el nombre de la nueva rama:

```shell

git branch speed-test
```

Pero podemos hacerlo desde `switch` con el argumento `-c`, en la que cambiaremos de rama creando la nueva que hayamos indicado:

```shell
git switch -c llm-upgrade
```

Hay que entender que cuando creeamos una rama nueva esta se ramificará desde la rama en la que nos situemos, por lo que es muy importante tener presente la rama en la que se trabaja.

Pero si estamos llevando a cabo un desarrollo muy extenso y queremos ver que cambios harian falta en main para que fuera como `chatbot` podemos ejecutar el comando `diff`:

```shell

git diff main chatbot
```

Aquí comparamos las diferencias entre `main` y `chatbot`. Podemos habernos equivocado en el nombre de nuestra rama, podemos corregirlo:

```shell

git branch -m chatbot mega-chatbot
```

Ahora bien, si las modificaciones ya han sido implementadas en `main` y queremos eliminar la rama, debemos saber si esta ha sido fusionada o no para ser conscientes de que comando debemos utilizar:

```shell

git branch -d fusiones_branch 
git branch -D unfusiones_branch #Borrado de fuerza bruta no preguntará antes de eliminar.
```

Cuando ya tenemos claro que todo esta bien, tiene el nombre que queremos y los cambios son compatibles, nos debemos situar en la rama principal. Posteriormente podemos fusionarla utilizando el siguiente comando:

```shell

git merge ai-assistant
```

### Capítulo 3: **<ins>Colaborar con Git</ins>**

Cuando varias personas intervienen en un proyecto es normal y común que pueda llegar a haber conflictos a la hora de modificar documentos. Conflictos como modificar el mismo documento desde varias ramas, es una de las situaciones que nos puede generar un error a la hora de intentarlas fusionar con `main`:

```shell
$ git merge documentation
Auto-merging task_list.txt
CONFLICT (content): Merge conflict in task_list.txt
Automatic merge failed; fix conflicts and then commit the result.
```

Git ya nos avisa que hay un conclicto de intereses a la hora de intentar fusionar diferentes ramas y nos pide que lo resolvamos antes de llevar a cabo la fusión. Para ello, podemos abrir el documenot y veremos lo siguiente:

```shell
TODO: Add documentation
<<<<<<< HEAD
TODO: Add unit tests
=======
TODO: Add examples
>>>>>>> documentation
TODO: Increase font size on courses pages
```

Podemos identificar diferentes bloques de información respecto al documento que pretendemos fusionar:

* **Contenido compartido sin conflicto:** `TODO: Add documentation` y `TODO: Increase font size on courses pages`.

* **Contenido de la rama actual(main):** `TODO: Add unit tests`.

* **Cambio entrante conflictivo(documentation):** `TODO: Add examples`.

Así pues, para poder solucionar los conflictos que nos impiden fusionar ramas, debemos decidir que cambio queremos aplicar. Para hacerlo, modificamos el documento que genera el conflicto con la decisión que hayamos tomado.

Ahora que ya sabemos como trabajar con ramas, documentos locales y corregir diferencias de contenido en un documento de una rama y de otra, vamos a ver como podemos implementar estos cambios en repositorios remotos. 

Lo primero sería enlazar nuestro repositorio local al repositorio remoto:

```shell
$ git remote add origin {URL}
```

De esta forma nombramos hacemos que `origin`, el repo remoto, se vincule con el repositorio en el que nos encontremos. 

Cuando ya hemos vinculado repositorios, verificamos que no haya ninguna disparidad, descargando el listado de commits, ramas y cambios que se hayan dado:

```shell
$ git fetch origin main
```

`fetch` funciona como una vista previa de los cambios que no existen en local. Descarga los cambios que tengamos en remoto, en una rama provisional llamada `origin/main`. Si vemos que hay cambios importantes o que debamos implementar, podemos implementarlos ejecutando `git merge origin/main`.

Cuando ya este todo listo para funsionar los entornos locales y remotos, ejecutamos un `push` al repositorio remoto:

```shell

$ git push origin local_branch
```

De esta forma, todo los cambios en documentos y ramas que hayamos decidido implementar en local, se subiran al repositorio remoto.