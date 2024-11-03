import heapq
class GrafoNoDirigido:
    def __init__(self):
        self.grafo = {}
    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []
    def agregar_arista(self, vertice1, vertice2, peso):
        self.agregar_vertice(vertice1)
        self.agregar_vertice(vertice2)
        self.grafo[vertice1].append((vertice2, peso))
        self.grafo[vertice2].append((vertice1, peso))
    def obtener_vertices(self):
        return list(self.grafo.keys())
    def obtener_adyacentes(self, vertice):
        return self.grafo.get(vertice, [])
    def prim_mst(self):
        inicio = next(iter(self.grafo))
        visitados = set([inicio])
        aristas = [(peso, inicio, destino) for destino, peso in self.grafo[inicio]]
        heapq.heapify(aristas)
        mst = []
        total_costo = 0
        while aristas and len(visitados) < len(self.grafo):
            peso, origen, destino = heapq.heappop(aristas)
            if destino not in visitados:
                visitados.add(destino)
                mst.append((origen, destino, peso))
                total_costo += peso
                for siguiente, p in self.grafo[destino]:
                    if siguiente not in visitados:
                        heapq.heappush(aristas, (p, destino, siguiente))

        return mst, total_costo
    def dijkstra(self, inicio, fin):
        distancias = {vertice: float('inf') for vertice in self.grafo}
        distancias[inicio] = 0
        cola = [(0, inicio)]
        previos = {inicio: None}
        while cola:
            distancia_actual, vertice_actual = heapq.heappop(cola)
            if vertice_actual == fin:
                break
            for adyacente, peso in self.grafo[vertice_actual]:
                distancia = distancia_actual + peso
                if distancia < distancias[adyacente]:
                    distancias[adyacente] = distancia
                    previos[adyacente] = vertice_actual
                    heapq.heappush(cola, (distancia, adyacente))
        # Reconstruir el camino desde el final al inicio
        camino = []
        vertice = fin
        while vertice is not None:
            camino.append(vertice)
            vertice = previos[vertice]
        camino.reverse()
        return camino, distancias[fin]
## 
##
##
# Crear el grafo no dirigido
grafo = GrafoNoDirigido()

# Agregar vértices (ambientes)
ambientes = [
    "cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2", 
    "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"
]

for ambiente in ambientes:
    grafo.agregar_vertice(ambiente)

# Agregar aristas (conexiones con distancias en metros)
# Ejemplo de conexiones (las distancias son ficticias)
conexiones = [
    ("cocina", "comedor", 3), ("cocina", "baño 1", 5), ("cocina", "sala de estar", 7),
    ("comedor", "sala de estar", 4), ("comedor", "habitación 1", 6), ("comedor", "baño 2", 3),
    ("cochera", "patio", 8), ("cochera", "cocina", 10), ("cochera", "habitación 2", 7),
    ("quincho", "terraza", 2), ("quincho", "patio", 4), ("quincho", "habitación 2", 5),
    ("baño 1", "habitación 1", 4), ("baño 2", "habitación 2", 6),
    ("habitación 1", "sala de estar", 5), ("habitación 2", "terraza", 8),
    ("sala de estar", "patio", 9), ("terraza", "patio", 3)
]

for vertice1, vertice2, peso in conexiones:
    grafo.agregar_arista(vertice1, vertice2, peso)

##
##
##
mst, metros_totales = grafo.prim_mst()
print("Árbol de Expansión Mínima:", mst)
print("Total de metros de cables para conectar todos los ambientes:", metros_totales)

camino, distancia = grafo.dijkstra("habitación 1", "sala de estar")
print("Camino más corto de Habitación 1 a Sala de Estar:", camino)
print("Total de metros de cables para conectar el router con el Smart TV:", distancia)
