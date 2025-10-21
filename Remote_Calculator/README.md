# 🧮 Proyecto: Calculadora de presencialidad en la oficina

A fecha de 21 de octubre de 2025, tengo un trabajo con un contrato de presencialidad basado en porcentajes.
El contrato exige una presencialidad anual total del 20% en la oficina de la empresa, por lo que puedo trabajar telemáticamente el 80% restante.
Dicho esto, este proyecto nace como solución a los siguientes problemas:

- El porcentaje total de teletrabajo es tan amplio que fácilmente puede llevar a un incumplimiento del contrato, por lo que exige tener cuidado de no sobrepasar ese 80% de trabajo telemático.

- El sistema de fichaje de la empresa no proporciona información relativa a los porcentajes de asistencia y teletrabajo.

- Para poder obtener la información del punto anterior, es necesario solicitarla directamente al encargado del departamento y esperar a que la suministre.

# ⚙️ Solución propuesta

Como solución, he creado el siguiente script en Python, que permite calcular de forma automática el porcentaje de días teletrabajados, presenciales y los días restantes para cumplir con la presencialidad exigida:

```python
import pandas as pd

csv_file = "./Remote_Calculator/data.csv"

# Función lambda que nos permite calcular el porcentaje:
porcentaje = lambda x, y: (x * 100) / y

# Transformamos los datos del CSV en un DataFrame:
df_csv = pd.read_csv(csv_file, header=0)

# Recogemos los datos del DataFrame que necesitamos
total_teletrabajo = (df_csv['Tipo'] == 'Teletrabajo').sum()
total_presencial = (df_csv['Tipo'] == 'Presencial').sum()
remaining = df_csv['Tipo'].isnull().sum()

# Calculamos el total de días trabajados:
total = total_teletrabajo + total_presencial

# Total de días trabajados:
print(f"\nDías totales trabajados: {total}")

# Porcentaje y total de días teletrabajados:
print(f"\n\tTeletrabajo {round(porcentaje(total_teletrabajo, total), 2)}%, {total_teletrabajo} días.")

# Porcentaje y total de días presenciales:
print(f"\n\tPresencial {round(porcentaje(total_presencial, total), 2)}%, {total_presencial} días.")

# Calculamos los días restantes del total del año:
total_oficina = round((total + remaining) * 0.2)

print(f"\nDÍAS RESTANTES DE OFICINA: {total_oficina - total_presencial}\n")
```

# 🧾 Estructura de los datos

Los datos son recogidos de un documento CSV que contiene la información relativa a la asistencia anual, registrada por días:

```csv
Día,Entrada,Salida,Duración,Tipo
1,,,,Ausencia
2,,,,Ausencia
3,,,,Ausencia
4,,,,Ausencia
5,,,,Ausencia
6,,,,Ausencia
7,8,15,6h 30m,Presencial
8,8,15,6h 30m,Presencial
9,8,15,6h 30m,Presencial
10,8,15,6h 30m,Presencial
11,,,,Ausencia
12,,,,Ausencia
13,8,15,6h 30m,Teletrabajo
14,8,15,6h 30m,Teletrabajo
15,8,15,6h 30m,Teletrabajo
16,8,15,6h 30m,Presencial
17,8,15,6h 30m,Presencial
...
```

Cualquier dato como vacaciones o fines de semana se interpreta como Ausencia.
Los registros ausentes de datos corresponden a fechas posteriores a la fecha de creación.

# 📊 Salida del script

A día de hoy, la ejecución del script genera el siguiente resultado:

```
Días totales trabajados: 182

        Teletrabajo 84.07%, 153 días.

        Presencial 15.93%, 29 días.

DÍAS RESTANTES DE OFICINA: 16
```