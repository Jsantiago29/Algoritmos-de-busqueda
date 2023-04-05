"""
Created on Tue Apr  4 21:33:44 2023

@author: Jaime Santiago Garcia
Registro: 20310369
"""

# Definir la función para encontrar el camino más corto usando el algoritmo de Dijkstra
def dijkstra(grafico, inicio, fin):
    # Crear un diccionario para rastrear las distancias de los nodos desde el nodo de inicio
    distancias = {nodo: float('inf') for nodo in grafico}
    distancias[inicio] = 0
    
    # Crear un diccionario para rastrear los nodos previos en el camino más corto
    anterior = {}
    
    # Crear un conjunto para rastrear los nodos visitados
    visitados = set()
    
    # Bucle hasta que se visiten todos los nodos o se encuentre el nodo de destino
    while len(visitados) < len(grafico):
        # Encontrar el nodo con la distancia más corta que no haya sido visitado aún
        nodo_actual = None
        distancia_minima = float('inf')
        for nodo in grafico:
            if nodo not in visitados and distancias[nodo] < distancia_minima:
                nodo_actual = nodo
                distancia_minima = distancias[nodo]
        
        # Si no se encuentra un nodo válido, el grafo no está conectado
        if nodo_actual is None:
            print("El grafo no está conectado")
            return None
        
        # Marcar el nodo actual como visitado
        visitados.add(nodo_actual)
        
        # Actualizar las distancias de los nodos adyacentes al nodo actual
        for vecino, distancia in grafico[nodo_actual].items():
            distancia_total = distancias[nodo_actual] + distancia
            if distancia_total < distancias[vecino]:
                distancias[vecino] = distancia_total
                anterior[vecino] = nodo_actual
    
    # Construir el camino más corto desde el nodo de inicio hasta el nodo de destino
    camino_mas_corto = [fin]
    while camino_mas_corto[-1] != inicio:
        camino_mas_corto.append(anterior[camino_mas_corto[-1]])
    camino_mas_corto.reverse()
    
    return camino_mas_corto, distancias[fin]


# Solicitar al usuario ingresar el grafo
grafico = {}
num_nodos = int(input("Ingrese el número de nodos en el grafo: "))
for i in range(num_nodos):
    nodo = input("Ingrese el nombre del nodo #{}: ".format(i+1))
    vecinos = {}
    num_vecinos = int(input("Ingrese el número de nodos adyacentes para el nodo {}: ".format(nodo)))
    for j in range(num_vecinos):
        vecino = input("Ingrese el nombre del nodo adyacente #{} para el nodo {}: ".format(j+1, nodo))
        distancia = int(input("Ingrese el peso del enlace entre el nodo {} y el nodo {}: ".format(nodo, vecino)))
        vecinos[vecino] = distancia
    grafico[nodo] = vecinos

# Solicitar al usuario ingresar los nodos de inicio y fin
nodo_inicio = input("Ingrese el nombre del nodo de inicio: ")
nodo_fin = input("Ingrese el nombre del nodo de fin: ")

# Ejecutar el algoritmo de Dijkstra y obtener el camino más corto y la distancia total
camino_mas_corto, distancia_total = dijkstra(grafico, nodo_inicio, nodo_fin)

# Imprimir el resultado
if camino_mas_corto is not None:
    print("El camino más corto desde {} hasta {} es: {}".format(nodo_inicio, nodo_fin, camino_mas_corto))
    print("La distancia total es: {}".format(distancia_total))