# EJERCICIO 1 - Pokémons con tres árboles (nombre, número y tipo)
from tree import BinaryTree
from pokemon_data import pokemons


# ------------------------------------------------------------------
# Funciones auxiliares (mismo estilo de recorrido recursivo que tree.py)
# ------------------------------------------------------------------
def recorrer_inorden(root, accion):
    if root is not None:
        recorrer_inorden(root.left, accion)
        accion(root)
        recorrer_inorden(root.right, accion)


def mostrar_pokemon(pokemon):
    print(
        f"#{pokemon['numero']} {pokemon['nombre']} | "
        f"tipos: {', '.join(pokemon['tipos'])} | "
        f"debilidades: {', '.join(pokemon['debilidades'])} | "
        f"mega: {'Sí' if pokemon['mega'] else 'No'} | "
        f"gigamax: {'Sí' if pokemon['gigamax'] else 'No'}"
    )


def busqueda_por_proximidad(arbol, texto):
    # muestra los Pokémons cuyo nombre comienza o contiene el texto
    texto = texto.lower()

    def mostrar_si_coincide(nodo):
        if texto in nodo.value.lower():
            mostrar_pokemon(nodo.other_values)

    recorrer_inorden(arbol.root, mostrar_si_coincide)


def debiles_frente_a_tipos(arbol, tipos):
    def mostrar_si_es_debil(nodo):
        if any(tipo in nodo.other_values['debilidades'] for tipo in tipos):
            print(f"   {nodo.other_values['numero']} - {nodo.value}")

    recorrer_inorden(arbol.root, mostrar_si_es_debil)


def contar_por_atributo(root, atributo):
    cantidad = 0
    if root is not None:
        cantidad += contar_por_atributo(root.left, atributo)
        if root.other_values[atributo]:
            cantidad += 1
        cantidad += contar_por_atributo(root.right, atributo)
    return cantidad


# ------------------------------------------------------------------
# A) Carga de los tres árboles (índices: nombre, número y tipo)
# ------------------------------------------------------------------
arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

for pokemon in pokemons:
    arbol_nombre.insert_node(pokemon['nombre'], pokemon)
    arbol_numero.insert_node(pokemon['numero'], pokemon)
    # un nodo por tipo, con la lista de nombres de los Pokémons de ese tipo
    for tipo in pokemon['tipos']:
        nodo_tipo = arbol_tipo.search(tipo)
        if nodo_tipo is None:
            arbol_tipo.insert_node(tipo, [pokemon['nombre']])
        else:
            nodo_tipo.other_values.append(pokemon['nombre'])

print(f'Pokémons cargados: {len(pokemons)}')

# ------------------------------------------------------------------
# B) Datos de un Pokémon por número y por nombre (proximidad)
# ------------------------------------------------------------------
print('\n--- B) Búsqueda por número (25) ---')
nodo = arbol_numero.search(25)
if nodo is not None:
    mostrar_pokemon(nodo.other_values)
else:
    print('no se encontró el número')

print('\n--- B) Búsqueda por proximidad de nombre ("bul") ---')
busqueda_por_proximidad(arbol_nombre, 'bul')

# ------------------------------------------------------------------
# C) Nombres de los Pokémons de un tipo
# ------------------------------------------------------------------
print('\n--- C) Pokémons por tipo ---')
for tipo in ['fantasma', 'fuego', 'acero', 'eléctrico']:
    nodo_tipo = arbol_tipo.search(tipo)
    print(f'Tipo {tipo}:')
    if nodo_tipo is not None:
        for nombre in nodo_tipo.other_values:
            print(f'   {nombre}')

# ------------------------------------------------------------------
# D) Listados: ascendente por número, por nombre y por nivel por nombre
# ------------------------------------------------------------------
print('\n--- D) Listado ascendente por número ---')
recorrer_inorden(arbol_numero.root, lambda n: print(f"{n.value} - {n.other_values['nombre']}"))

print('\n--- D) Listado ascendente por nombre ---')
recorrer_inorden(arbol_nombre.root, lambda n: print(f"{n.value} - {n.other_values['numero']}"))

print('\n--- D) Listado por nivel (árbol de nombres) ---')
arbol_nombre.by_level()

# ------------------------------------------------------------------
# E) Pokémons débiles frente a Jolteon, Lycanroc y Tyrantrum
#    (se toman los tipos de cada uno y se buscan los que tengan esa debilidad)
# ------------------------------------------------------------------
print('\n--- E) Débiles frente a Jolteon, Lycanroc y Tyrantrum ---')
for nombre in ['Jolteon', 'Lycanroc', 'Tyrantrum']:
    nodo = arbol_nombre.search(nombre)
    if nodo is not None:
        tipos_atacante = nodo.other_values['tipos']
        print(f"Débiles frente a {nombre} (tipo {', '.join(tipos_atacante)}):")
        debiles_frente_a_tipos(arbol_nombre, tipos_atacante)
    else:
        print(f'{nombre} no está cargado')

# ------------------------------------------------------------------
# F) Todos los tipos y cuántos Pokémons hay de cada uno
# ------------------------------------------------------------------
print('\n--- F) Cantidad de Pokémons por tipo ---')
recorrer_inorden(arbol_tipo.root, lambda n: print(f'{n.value}: {len(n.other_values)}'))

# ------------------------------------------------------------------
# G) Cantidad con megaevolución
# ------------------------------------------------------------------
print(f"\n--- G) Pokémons con megaevolución: {contar_por_atributo(arbol_numero.root, 'mega')}")

# ------------------------------------------------------------------
# H) Cantidad con forma gigamax
# ------------------------------------------------------------------
print(f"--- H) Pokémons con forma gigamax: {contar_por_atributo(arbol_numero.root, 'gigamax')}")