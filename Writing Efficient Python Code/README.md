




```python
#Que entendemos por oficiente?

#1. La rapidez, aquel código que tiene una diferencia de tiempo baja entre la ejecución y la devolución de un resultado.

#2. Consumo mínimo de recursos. La eficiencia tambien depende del consumo de memoria que tenga la ejecución de nuestro código.

#La legibilidad es un concepto importante a tener en cuenta a la hora de escribir código eficiente. Cuando nuestro código es eficiente y legible, decimos que es código pitónico. Ejemplo:

#NO-pitónico:
numeros_doblados = []

for i in range(len(nums)):
    numeros_doblados.append(nums[i] * 2)

#Pitónico:
numeros_doblados = [x * 2 for x in nums]

```