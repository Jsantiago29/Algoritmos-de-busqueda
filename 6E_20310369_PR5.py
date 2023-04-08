#Jaime Santiago GarcÃ­a
#20310369

import math

def kruskal(graph, max_path=False):
    if max_path:
        aristas_ordenadas = sorted((-peso, inicio, fin) for inicio in graph for fin, peso in graph[inicio].items() if peso != math.inf)
    else:
        aristas_ordenadas = sorted((peso, inicio, fin) for inicio in graph for fin, peso in graph[inicio].items() if peso != math.inf)
    arbol_min = {i: i for i in graph}
    arbol_cant = len(arbol_min)
    aristas_min = []
    costo_minimo = 0

    for peso, inicio, fin in aristas_ordenadas:
        if arbol_min[inicio] != arbol_min[fin]:
            aristas_min.append((inicio, fin, peso))
            costo_minimo += peso
            arbol_min_actual, arbol_min_nuevo = arbol_min[inicio], arbol_min[fin]
            for i in range(arbol_cant):
                if arbol_min[i] == arbol_min_actual:
                    arbol_min[i] = arbol_min_nuevo
            arbol_cant -= 1
            if arbol_cant == 1:
                break

    return aristas_min, costo_minimo

# Ejemplo de uso
n = int(input("Ingrese la cantidad de nodos: "))
graph = {}
for i in range(n):
    graph[i] = {}
for i in range(n):
    for j in range(i + 1, n):
        respuesta = input(f"Hay conexión entre el nodo {i} y el nodo {j}? (si/no): ")
        if respuesta.lower() == "si":
            costo = int(input(f"Ingrese el costo entre el nodo {i} y el nodo {j}: "))
            graph[i][j] = costo
            graph[j][i] = costo
        elif respuesta.lower() == "no":
            graph[i][j] = math.inf
            graph[j][i] = math.inf
        else:
            print("\n   Por favor ingrese una respuesta válida (Debe de ser si/no).\n")
        

aristas_min, costo_minimo = kruskal(graph)
print(f"El costo minimo del árbol es: {costo_minimo}")

aristas_max, costo_max = kruskal(graph, max_path=True)
if costo_max != -math.inf:
    print(f"El costo maximo de la trayectoria es: {abs(costo_max)}")
else:
    print("No hay una trayectoria de máximo costo en el grafo.")
