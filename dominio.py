import numpy as np 
import pandas as pd

def generar_dominio(dimensiones):
    #Generar un dominio de elementos finitos.
    dominio = np.zeros(dimensiones)
    return dominio

def exportar_para_paraview(presion, desplazamiento, nombre_archivo='resultados_paraview.csv'):
    #Exportar los resultados de la simulación a un archivo csv para su visualización en Paraview.
    df = pd.DataFrame({'Presion': presion, 'Desplazamiento': desplazamiento})
    df.to_csv(nombre_archivo, index=False)
    print(f"Datos exportados a '{nombre_archivo}' para Paraview.")

def tensor_deformaciones(desplazamientos_nodales):
    #Calcular el tensor de deformaciones para un elemento finito tetraédrico dado su matriz de desplazamientos nodales.
    gradientes = np.gradient(desplazamientos_nodales)
    return gradientes
