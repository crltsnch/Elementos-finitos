import numpy as np 
import pandas as pd

def generar_dominio(dimensiones):
    dominio = np.zeros(dimensiones)
    return dominio

def exportar_para_paraview(presion, desplazamiento, nombre_archivo='resultados_paraview.csv'):
    df = pd.DataFrame({'Presion': presion, 'Desplazamiento': desplazamiento})
    df.to_csv(nombre_archivo, index=False)
    print(f"Datos exportados a '{nombre_archivo}' para Paraview.")
