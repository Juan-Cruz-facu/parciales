# EJERCICIO 2 - Grafo no dirigido de personajes de Star Wars
from graph import Graph

# (clave del vértice, nombre, episodios en los que aparece)
# La clave no lleva guion porque kruskal() de graph.py usa '-' como separador.
personajes = [
    ('Luke Skywalker', 'Luke Skywalker', [4, 5, 6, 7, 8, 9]),
    ('Darth Vader', 'Darth Vader', [3, 4, 5, 6]),
    ('Yoda', 'Yoda', [1, 2, 3, 5, 6, 8]),
    ('Boba Fett', 'Boba Fett', [2, 5, 6]),
    ('C3PO', 'C-3PO', [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ('Leia', 'Leia', [3, 4, 5, 6, 7, 8, 9]),
    ('Rey', 'Rey', [7, 8, 9]),
    ('Kylo Ren', 'Kylo Ren', [7, 8, 9]),
    ('Chewbacca', 'Chewbacca', [3, 4, 5, 6, 7, 8, 9]),
    ('Han Solo', 'Han Solo', [4, 5, 6, 7, 9]),
    ('R2D2', 'R2-D2', [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ('BB8', 'BB-8', [7, 8, 9]),
]


def nombre_de(grafo, clave):
    pos = grafo.search(clave, 'value')
    return grafo[pos].other_values['nombre']


def camino_mas_corto(grafo, origen, destino):
    if not grafo.exist_path(origen, destino):
        print('no existe camino')
        return
    paths = grafo.dijkstra(origen)
    buscado = destino
    peso_total = None
    camino = []
    while paths.size() > 0:
        value = paths.pop()
        if value[0] == buscado:
            if peso_total is None:
                peso_total = value[1]
            camino.append(nombre_de(grafo, value[0]))
            buscado = value[2]
    camino.reverse()
    print(f"{nombre_de(grafo, origen)} -> {nombre_de(grafo, destino)}: "
          f"{' - '.join(camino)} (peso total: {peso_total})")


def mostrar_arbol_expansion_minima(grafo, origen):
    arbol = grafo.kruskal(origen)
    peso_total = 0
    print(f'Árbol de expansión mínimo desde {nombre_de(grafo, origen)}:')
    for arista in arbol.split(';'):
        a, b, peso = arista.split('-')
        print(f'   {nombre_de(grafo, a)} <-> {nombre_de(grafo, b)} ({peso})')
        peso_total += int(peso)
    print(f'   peso total: {peso_total}')


# ------------------------------------------------------------------
# A) Carga: vértices = personajes, aristas = episodios en común
# ------------------------------------------------------------------
grafo = Graph(is_dir=False)

for clave, nombre, episodios in personajes:
    grafo.add_vertex(clave, {'nombre': nombre, 'episodios': episodios})

for i in range(len(personajes)):
    for j in range(i + 1, len(personajes)):
        comunes = 0
        for episodio in personajes[i][2]:
            if episodio in personajes[j][2]:
                comunes += 1
        if comunes > 0:
            grafo.add_edge(comunes, personajes[i][0], personajes[j][0])

# ------------------------------------------------------------------
# B) Árbol de expansión mínimo desde C-3PO, Yoda y Leia
# ------------------------------------------------------------------
print('--- B) Árbol de expansión mínimo ---')
for origen in ['C3PO', 'Yoda', 'Leia']:
    mostrar_arbol_expansion_minima(grafo, origen)
    print()

# ------------------------------------------------------------------
# C) Máximo de episodios compartidos y pares que lo cumplen
# ------------------------------------------------------------------
maximo = 0
for vertice in grafo:
    for arista in vertice.edges:
        if arista.weight > maximo:
            maximo = arista.weight

print(f'--- C) Máximo de episodios compartidos: {maximo}')
for vertice in grafo:
    for arista in vertice.edges:
        # cada par figura dos veces (grafo no dirigido): se muestra una sola
        if arista.weight == maximo and vertice.value < arista.destination:
            print(f'   {nombre_de(grafo, vertice.value)} y {nombre_de(grafo, arista.destination)}')

# ------------------------------------------------------------------
# D) Caminos más cortos
# ------------------------------------------------------------------
print('\n--- D) Caminos más cortos ---')
camino_mas_corto(grafo, 'C3PO', 'R2D2')
camino_mas_corto(grafo, 'Yoda', 'Darth Vader')

# ------------------------------------------------------------------
# E) Personajes que aparecieron en los nueve episodios
# ------------------------------------------------------------------
print('\n--- E) Personajes presentes en los 9 episodios ---')
for vertice in grafo:
    if len(vertice.other_values['episodios']) == 9:
        print(f"   {vertice.other_values['nombre']}")
