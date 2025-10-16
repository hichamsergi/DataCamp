import pandas as pd
import tabula as tb # paquete que nos permitirá transformar el tipo de formato PDF a CSV
import os 

wd_pdf = "./TEST/PDF/"
wd_csv = "./TEST/CSV/"

total_presencial = 0
total_teletrabajo = 0

# Convertimos los PDF existentes en CSV para el manejo:
for documento in os.listdir(wd_pdf):
    
    pdf_file = wd_pdf + '/' + documento 

    csv_file_gen = tb.convert_into(pdf_file, wd_csv + documento[:6] + '.csv', output_format='csv', pages='all', lattice=False)


#Tansformamos los datos de CSV en un DataFrame:
for documento in os.listdir(wd_csv):

    df_csv = pd.read_csv(wd_csv+documento, header=None, na_values='nan')

#Iteramos sobre el DataFrame para poder localizar los días de Presencial/Teletrabajo
    for day in df_csv[0]:

        print(day)

#        if type(day) == str:
#
#            if 'Teletrabajo' in day:
#                total_teletrabajo += 1 
#            
#            elif 'Presencial' in day:
#               total_presencial += 1