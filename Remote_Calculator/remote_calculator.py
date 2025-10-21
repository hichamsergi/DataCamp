import pandas as pd

csv_file = "./Remote_Calculator/data.csv"

#Función lambda que nos permite calcular el porcentaje:
porcentaje = lambda x, y: (x*100) / y

#Tansformamos los datos de CSV en un DataFrame:
df_csv = pd.read_csv(csv_file, header=0)

#Recogemos los datos del DataFrame que necesitamos
total_teletrabajo = (df_csv['Tipo'] == 'Teletrabajo').sum()
total_presencial = (df_csv['Tipo'] == 'Presencial').sum()

remaining = (df_csv['Tipo']).isnull().sum()

#Calculamos el total de días trabajados:
total = total_teletrabajo + total_presencial
    

#Total de días trabajados:
print(f"\nDías totales trabajados: {total}")

#Porcentaje y total de días teletrabajados:
print(f"\n\tTeletrabajo {round(porcentaje(total_teletrabajo, total),2)}%, {total_teletrabajo} días.")

#Porcentaje y total de días presenciales:
print(f"\n\tPresencial {round(porcentaje(total_presencial, total),2)}%, {total_presencial} días.")

#Calculamos los días restantes del total del año:
total_oficina = round((total + remaining) * 0.2)

print(f"\nDÍAS RESTANTES DE OFICINA: {total_oficina - total_presencial}\n")