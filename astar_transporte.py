import heapq

# Definir el grafo del sistema de transporte como un diccionario
reglas_transporte = {
    '1': {'2': 5, '3': 2},
    '2': {'1': 5, '4': 3},
    '3': {'1': 2, '4': 4},
    '4': {'2': 3, '3': 4}
}

# Función heurística
def heuristica(nodo, objetivo):
    heuristicas = {
        '1': 3,
        '2': 2,
        '3': 1,
        '4': 0
    }
    return heuristicas[nodo]

# Algoritmo A* (A-Star)
def a_estrella(grafo, inicio, fin):
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (0, inicio))
    costo_total = {inicio: 0}
    camino = {inicio: None}
    
    while cola_prioridad:
        costo_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        if nodo_actual == fin:
            ruta = []
            while nodo_actual:
                ruta.append(nodo_actual)
                nodo_actual = camino[nodo_actual]
            return ruta[::-1]  # Devolver la ruta desde el inicio al final

        for vecino, costo in grafo[nodo_actual].items():
            nuevo_costo = costo_total[nodo_actual] + costo
            if vecino not in costo_total or nuevo_costo < costo_total[vecino]:
                costo_total[vecino] = nuevo_costo
                prioridad = nuevo_costo + heuristica(vecino, fin)
                heapq.heappush(cola_prioridad, (prioridad, vecino))
                camino[vecino] = nodo_actual

    return None  # Si no se encuentra una ruta

# Entrada del usuario
inicio = str(input("Introduce el nodo de inicio: "))
fin = str(input("Introduce el nodo de destino: "))

# Debugging
print("Grafo de transporte:", reglas_transporte)
print("Nodo de inicio:", inicio)
print("Nodo de destino:", fin)

mejor_ruta = a_estrella(reglas_transporte, inicio, fin)

if mejor_ruta:
    print(f"La mejor ruta de {inicio} a {fin} es: {mejor_ruta}")
else:
    print(f"No se encontró una ruta de {inicio} a {fin}")


