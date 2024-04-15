import numpy as np
from scipy.sparse import lil_matrix

def generar_malla_tridimensional(sizex, sizey, sizez, ndivx, ndivy, ndivz, jumpx=0.0):
    """
    Genera una malla tridimensional para un dominio estructural.

    Args:
    sizex (float): Tamaño del dominio en el eje x.
    sizey (float): Tamaño del dominio en el eje y.
    sizez (float): Tamaño del dominio en el eje z.
    ndivx (int): Número de divisiones en el eje x.
    ndivy (int): Número de divisiones en el eje y.
    ndivz (int): Número de divisiones en el eje z.

    Returns:
    tuple: Tupla que contiene la lista de nodos y la lista de elementos de malla.
    """
    gapx = sizex / ndivx
    gapy = sizey / ndivy
    gapz = sizez / ndivz

    vec_nodes_0 = []
    for i in range(0, ndivx + 1, 1):
        for j in range(0, ndivy + 1, 1):
            for k in range(0, ndivz + 1, 1):
                vec_nodes_0.append([i * gapx + jumpx - sizex / 2, j * gapy, k * gapz])

    mesh = []
    for i in range(0, ndivx, 1):
        for j in range(0, ndivy, 1):
            for k in range(0, ndivz, 1):
                n1 = [i, j, k]
                n2 = [i + 1, j, k]
                n4 = [i, j + 1, k]
                n3 = [i + 1, j + 1, k]
                n5 = [i, j, k + 1]
                n6 = [i + 1, j, k + 1]
                n8 = [i, j + 1, k + 1]
                n7 = [i + 1, j + 1, k + 1]
                n_loc = [n1, n2, n3, n4, n5, n6, n7, n8]
                n_glob = []
                for l in range(0, len(n_loc), 1):
                    n_glob.append(n_loc[l][0] * (ndivz + 1) * (ndivy + 1) + n_loc[l][1] * (ndivz + 1) + n_loc[l][2])
                vec_aux = [[0, 1, 3, 4], [1, 2, 3, 6], [4, 7, 6, 3], [4, 6, 5, 1], [4, 6, 1, 3]]
                for l in range(0, len(vec_aux), 1):
                    mesh.append([n_glob[vec_aux[l][0]], n_glob[vec_aux[l][1]], n_glob[vec_aux[l][2]], n_glob[vec_aux[l][3]]])

    return vec_nodes_0, mesh


def calcular_funcion_de_forma(coordenadas_nodos, punto_evaluacion):
    #Calcula la función de forma para un punto de evaluación dado y nodos tetraédricos.
    # Implementar el cálculo de la función de forma (lineal) para los nodos y el punto de evaluación
    # Esto es un ejemplo simplificado
    funcion_forma = [...]
    return funcion_forma


def ensamblar_matrices_locales(matrices_locales, indices_globales):
    """
    Ensambla las matrices locales en la matriz global.

    Args:
    matrices_locales (list): Lista de matrices locales (numpy.ndarray).
    indices_globales (numpy.ndarray): Índices globales de los nodos en la matriz global.

    Returns:
    scipy.sparse.lil_matrix: Matriz global ensamblada.
    """
    nodos_totales = len(indices_globales)
    K_global = lil_matrix((nodos_totales, nodos_totales))
    
    for matriz_local in matrices_locales:
        for i, idx_global_i in enumerate(indices_globales):
            for j, idx_global_j in enumerate(indices_globales):
                K_global[idx_global_i, idx_global_j] += matriz_local[i, j]
                
    return K_global
