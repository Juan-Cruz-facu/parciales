import re
from collections import deque
from super_heroes_data import superheroes

#  EJERCICIO 1

heroes_15 = [
    "Iron Man", "Spider-Man", "Captain America", "Thor",
    "Black Widow", "Hulk", "Hawkeye", "Ant-Man",
    "Scarlet Witch", "Vision", "Doctor Strange",
    "Black Panther", "Captain Marvel", "Wolverine", "Cyclops"
]


def buscar_capitan_america(lista, indice=0):
    if indice >= len(lista):
        return False
    if lista[indice] == "Captain America":
        return True
    return buscar_capitan_america(lista, indice + 1)


def listar_heroes(lista, indice=0):
    if indice >= len(lista):
        return
    print(f"  {indice + 1}. {lista[indice]}")
    listar_heroes(lista, indice + 1)


# print("=" * 60)
# print("EJERCICIO 1")
# print("=" * 60)

# print("\nListado de 15 heroes:")
# listar_heroes(heroes_15)

# esta = buscar_capitan_america(heroes_15)
# print(f"\nCapitan America {'SI' if esta else 'NO'} esta en la lista.")

#  EJERCICIO 2

# print("\n" + "=" * 60)
# print("EJERCICIO 2")
# print("=" * 60)


# 1. Listado ordenado por nombre ascendente
print(f"\n1. Listado ordenado por nombre ({len(superheroes)} personajes):")
por_nombre = sorted(superheroes, key=lambda h: h["name"])
for h in por_nombre:
    print(f"   {h['name']}")


# 2. Posicion de The Thing y Rocket Raccoon
print("\n2. Posicion de The Thing y Rocket Raccoon en la lista ordenada:")
for i, h in enumerate(por_nombre):
    if h["name"] in ("The Thing", "Rocket Raccoon"):
        print(f"   {h['name']}: posicion {i + 1}")


# 3. Listar villanos
print("\n3. Villanos:")
villanos = [h for h in superheroes if h["is_villain"]]
for v in villanos:
    print(f"   {v['name']}")


# 4. Cola de villanos - filtrar los que aparecieron antes de 1980
print("\n4. Villanos que aparecieron antes de 1980 (usando cola):")
cola = deque(villanos)
antes_1980 = []
while cola:
    v = cola.popleft()
    if v["first_appearance"] < 1980:
        antes_1980.append(v)
for v in antes_1980:
    print(f"   {v['name']} ({v['first_appearance']})")


# 5. Personajes que comienzan con Bl, G, My, W
print("\n5. Personajes que comienzan con Bl, G, My o W:")
prefijos = ("Bl", "G", "My", "W")
for h in superheroes:
    if h["name"].startswith(prefijos):
        print(f"   {h['name']}")


# 6. Ordenados por nombre real ascendente
print("\n6. Personajes ordenados por nombre real:")
por_nombre_real = sorted(
    [h for h in superheroes if h["real_name"]],
    key=lambda h: h["real_name"]
)
for h in por_nombre_real:
    print(f"   {h['real_name']} ({h['name']})")


# 7. Personajes ordenados por fecha de aparicion
print("\n7. Personajes ordenados por primera aparicion:")
por_aparicion = sorted(superheroes, key=lambda h: h["first_appearance"])
for h in por_aparicion:
    print(f"   {h['first_appearance']} - {h['name']}")


# 8. Modificar nombre real de Ant Man a Scott Lang
print("\n8. Modificando nombre real de Ant Man:")
for h in superheroes:
    if h["name"] == "Ant Man":
        print(f"   Nombre anterior: {h['real_name']}")
        h["real_name"] = "Scott Lang"
        print(f"   Nombre actualizado: {h['real_name']}")


# 9. Personajes con 'time-traveling' o 'suit' (palabra exacta) en su biografia
print("\n9. Personajes con 'time-traveling' o 'suit' en su biografia:")
for h in superheroes:
    bio = h["short_bio"]
    if re.search(r'\bsuit\b', bio, re.IGNORECASE) or re.search(r'time-traveling', bio, re.IGNORECASE):
        print(f"   {h['name']}: {bio}")


# 10. Eliminar Electro y Baron Zemo y mostrar su informacion
print("\n10. Eliminando Electro y Baron Zemo:")
a_eliminar = ["Electro", "Baron Zemo"]
for nombre in a_eliminar:
    encontrado = next((h for h in superheroes if h["name"] == nombre), None)
    if encontrado:
        superheroes.remove(encontrado)
        print(f"\n   {encontrado['name']} eliminado:")
        print(f"   Nombre real:       {encontrado['real_name']}")
        print(f"   Primera aparicion: {encontrado['first_appearance']}")
        print(f"   Es villano:        {encontrado['is_villain']}")
        print(f"   Bio:               {encontrado['short_bio']}")
    else:
        print(f"\n   {nombre} no estaba en la lista.")
