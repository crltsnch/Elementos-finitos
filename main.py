from dominio import *
from dos import *
from scipy.sparse import lil_matrix

def main():
    # Parte I: Fundamentos de Elementos Finitos
    
    # Introducción a Python
    dimensiones_dominio = (10, 10, 10)
    dominio = generar_dominio(*dimensiones_dominio)
    print("Dominio estructural simple:")
    print(dominio)

    # Introducción a Paraview
    presion = np.array([100, 150, 200])
    desplazamiento = np.array([0.1, 0.2, 0.3])
    exportar_para_paraview(presion, desplazamiento)

    # Funciones Auxiliares en Python
    desplazamientos_nodales = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    tensor = tensor_deformaciones(desplazamientos_nodales)
    print("Tensor de deformaciones:")
    print(tensor)

    # Pre-procesado de Datos
    sizex = 10
    sizey = 10
    sizez = 10
    ndivx = 5
    ndivy = 5
    ndivz = 5
    mesh, _ = generar_malla_tridimensional(sizex, sizey, sizez, ndivx, ndivy, ndivz)
    coordenadas_nodos = mesh.points

    # Ejemplo conceptual de ensamblaje de matrices locales en la matriz global
    nodos_totales = 100  # Definir el número total de nodos
    K_local = lil_matrix((nodos_totales, nodos_totales))
    indices_globales = np.array([0, 1, 2, ...])  # Definir los índices globales de los nodos
    K_global = ensamblar_matrices_locales(K_local, indices_globales)


if __name__ == "__main__":
    main()