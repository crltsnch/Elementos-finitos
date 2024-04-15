# Elementos-finitos
El link a mi repositorio es: [Github](https://github.com/crltsnch/Elementos-finitos)

En este ejercicio hemos resuelto un desafío que combina la inteligencia artificial con el Método de Elementos Finitos (MEF) en 3D.

Parte I: Fundamentos de Elementos Finitos
Introducción a Python: Escribir un script en Python que genere y mostrar un arreglo tridimensional representando un dominio estructural simple.

Introducción a Paraview: Desarrolle un script en Python que exporte los resultados de un análisis estructural (presiones y desplazamientos) a un formato compatible con Paraview. Explique cómo visualizar estos resultados en Paraview.

Funciones Auxiliares en Python: Implementar una función en Python que calcule el tensor de deformaciones para un elemento finito tetraédrico dada su matriz de desplazamientos nodales.

Parte II: Pre-procesamiento y Análisis
Pre-procesado de Datos: Escribir un script para generar un mallado de tetraedros a partir de una geometría básica proporcionada.

Implementación de Función de Forma: Implementar la función de forma de un elemento tetraédrico en Python. Verificar su implementación calculando la función de forma en puntos seleccionados del dominio.

Ensamblaje de Matrices: Programar el ensamblaje de la matriz de rigidez global para una estructura mallada con tetraedros. Asegurarse de implementar condiciones de contorno apropiadas y de verificar la simetría de la matriz resultante.

Parte III: Solución y Post-procesamiento
Solución de Sistema de Ecuaciones: Desarrollar un solver para el sistema de ecuaciones resultante del método de elementos finitos. Discutir la selección del método numérico y su impacto en la eficiencia y precisión de la solución.

Post-procesamiento: Generar un script para calcular y visualizar las tensiones y deformaciones en la estructura analizada. Integrar su código con Paraview para la visualización de los resultados.

Caso de Estudio: Aplique todo el flujo de trabajo en un caso de estudio estructural proporcionado. Disutir los resultados y cómo las decisiones tomadas en cada etapa afectaron el resultado final.

## Resolución
Para este ejercicio hemos ejecutado el archivo 0_main_mesh_nodes.py de la carpeta mesh para generar los archivos nodes.txt, mesh.txt. EStos archivos son usados por nuestro programa para generar una serie de archivos vtu que serán los que le ingresaremos a Preview para visualizar nuestro problema (MEF_beam_bulk_1.vtu, MEF_beam_bulk_2.vtu, así hasta 10). Esta carpeta de archivos se la hemos ingresado a Preview y nos ha devuelto esto:

 
<img width="1440" alt="Captura de pantalla 2024-04-15 a las 22 19 46" src="https://github.com/crltsnch/Elementos-finitos/assets/91721777/f769972e-db69-4550-9137-b9ecbe59287b">


