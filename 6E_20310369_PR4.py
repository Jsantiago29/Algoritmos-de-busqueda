#Jaime Santiago García
#20310369

import heapq
import math

def prim(grafica, inicio):
    # Inicializamos el conjunto de nodos visitados con el nodo de inicio
    visitados = set([inicio])
    # Inicializamos la lista de aristas con todas las aristas que parten del nodo de inicio
    aristas = [
        (costo, inicio, destino)
        for destino, costo in grafica[inicio].items()
    ]
    # Convertimos la lista de aristas en un heap (un árbol binario que cumple una propiedad de orden)
    heapq.heapify(aristas)
    # Inicializamos la variable que almacenará el costo del árbol parcial mínimo
    costo_apm = 0
    # Inicializamos la lista de aristas del árbol parcial mínimo
    aristas_apm = []
    while aristas:
        # Obtenemos la arista de menor costo del heap
        costo, origen, destino = heapq.heappop(aristas)
        if destino not in visitados:
            # Si el nodo de destino de la arista no ha sido visitado, lo visitamos
            visitados.add(destino)
            # Agregamos la arista al árbol parcial mínimo
            costo_apm += costo
            aristas_apm.append((origen, destino, costo))
            # Agregamos todas las aristas que parten del nodo visitado al heap
            for destino_sig, costo in grafica[destino].items():
                if destino_sig not in visitados:
                    heapq.heappush(aristas, (costo, destino, destino_sig))
    # Devolvemos el costo del árbol parcial mínimo y la lista de aristas del árbol parcial mínimo
    return costo_apm, aristas_apm

# Ejemplo de uso
n = int(input("Ingrese la cantidad de nodos: "))
grafica = {}
for i in range(n):
    grafica[i] = {}
for i in range(n):
    for j in range(i + 1, n):
        respuesta = input(f"Hay conexión entre el nodo {i} y el nodo {j}? (si/no): ")
        if respuesta.lower() == "si":
            costo = int(input(f"Ingrese el costo entre el nodo {i} y el nodo {j}: "))
            grafica[i][j] = costo
            grafica[j][i] = costo
        elif respuesta.lower() == "no":
            grafica[i][j] = math.inf
            grafica[j][i] = math.inf
        else:
            print("Por favor ingrese una respuesta válida (si/no).")
            exit()
inicio = int(input("Ingrese el nodo inicial: "))
costo_apm, aristas_apm = prim(grafica, inicio)
print("El costo del árbol parcial mínimo es:", costo_apm)
print("Las aristas del árbol parcial mínimo son:")
for origen, destino, costo in aristas_apm:
    print(f"({origen}, {destino}): {costo}")


