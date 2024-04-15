from dominio import *

def main():
    dimensiones_dominio = (10, 10, 10)
    dominio = generar_dominio(dimensiones_dominio)
    print("Dominio estructural simple:")
    print(dominio)

    #Paraview
    presion = np.array([100, 150, 200])
    desplazamiento = np.array([0.1, 0.2, 0.3])
    exportar_para_paraview(presion, desplazamiento)

    desplazamientos_nodales = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    tensor = tensor_deformaciones(desplazamientos_nodales)
    print("Tensor de deformaciones:")
    print(tensor)

if __name__ == "__main__":
    main()