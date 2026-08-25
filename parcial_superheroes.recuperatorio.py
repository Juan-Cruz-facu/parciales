from cola import Cola, arribo, atencion, cola_vacia
from lista import Lista, insertar, buscar, eliminar, tamaño
from super_heroes_data import superheroes


heroes_15 = [
    "Iron Man", "Spider-Man", "Capitan America", "Thor", "Black Widow",
    "Hulk", "Hawkeye", "Ant-Man", "Scarlet Witch", "Vision",
    "Doctor Strange", "Black Panther", "Captain Marvel", "Wolverine",
    "Cyclops"
]


def buscar_capitan_america(lista, indice=0):
    if indice == len(lista):
        return False
    if lista[indice] == "Capitan America":
        return True
    return buscar_capitan_america(lista, indice + 1)


def listar_heroes(lista, indice=0):
    if indice < len(lista):
        print("  {}. {}".format(indice + 1, lista[indice]))
        listar_heroes(lista, indice + 1)


def mostrar_personaje(personaje):
    print("   Nombre:            {}".format(personaje["name"]))
    print("   Nombre real:       {}".format(personaje["real_name"]))
    print("   Primera aparicion: {}".format(personaje["first_appearance"]))
    print("   Es villano:        {}".format(personaje["is_villain"]))
    print("   Bio:               {}".format(personaje["short_bio"]))


def posicion_personaje(lista, nombre):
    posicion = 1
    aux = lista.inicio
    while aux is not None:
        if aux.info["name"] == nombre:
            return posicion
        aux = aux.sig
        posicion += 1
    return None



print("EJERCICIO 1")

print("\nListado de 15 heroes:")
listar_heroes(heroes_15)
print("\nCapitan America {} esta en la lista.".format(
    "SI" if buscar_capitan_america(heroes_15) else "NO"
))



print("EJERCICIO 2")


lista_personajes = Lista()
for personaje in superheroes:
    insertar(lista_personajes, personaje, "name")


print("\n1. Listado ordenado por nombre ({} personajes):".format(
    tamaño(lista_personajes)
))
aux = lista_personajes.inicio
while aux is not None:
    print("   {}".format(aux.info["name"]))
    aux = aux.sig


print("\n2. Posicion en la lista ordenada por nombre:")
for nombre in ("The Thing", "Rocket Raccoon"):
    posicion = posicion_personaje(lista_personajes, nombre)
    if posicion is not None:
        print("   {}: posicion {}".format(nombre, posicion))
    else:
        print("   {} no se encuentra en la lista.".format(nombre))


print("\n3. Villanos:")
aux = lista_personajes.inicio
while aux is not None:
    if aux.info["is_villain"]:
        print("   {}".format(aux.info["name"]))
    aux = aux.sig


cola_villanos = Cola()
aux = lista_personajes.inicio
while aux is not None:
    if aux.info["is_villain"]:
        arribo(cola_villanos, aux.info)
    aux = aux.sig

print("\n4. Villanos aparecidos antes de 1980 (usando Cola):")
while not cola_vacia(cola_villanos):
    villano = atencion(cola_villanos)
    if villano["first_appearance"] < 1980:
        print("   {} ({})".format(villano["name"], villano["first_appearance"]))


print("\n5. Personajes que comienzan con Bl, G, My o W:")
aux = lista_personajes.inicio
while aux is not None:
    nombre = aux.info["name"]
    if (nombre.startswith("Bl") or nombre.startswith("G") or
            nombre.startswith("My") or nombre.startswith("W")):
        print("   {}".format(nombre))
    aux = aux.sig


lista_nombre_real = Lista()
aux = lista_personajes.inicio
while aux is not None:
    insertar(lista_nombre_real, aux.info, "real_name")
    aux = aux.sig

print("\n6. Personajes ordenados por nombre real:")
aux = lista_nombre_real.inicio
while aux is not None:
    nombre_real = aux.info["real_name"]
    if nombre_real is None:
        nombre_real = "Sin nombre real"
    print("   {} ({})".format(nombre_real, aux.info["name"]))
    aux = aux.sig


lista_superheroes_fecha = Lista()
aux = lista_personajes.inicio
while aux is not None:
    if not aux.info["is_villain"]:
        insertar(lista_superheroes_fecha, aux.info, "first_appearance")
    aux = aux.sig

print("\n7. Superheroes ordenados por fecha de aparicion:")
aux = lista_superheroes_fecha.inicio
while aux is not None:
    print("   {} - {}".format(
        aux.info["first_appearance"], aux.info["name"]
    ))
    aux = aux.sig


print("\n8. Modificando nombre real de Ant Man:")
nodo_ant_man = buscar(lista_personajes, "Ant Man", "name")
if nodo_ant_man is not None:
    print("   Nombre anterior: {}".format(nodo_ant_man.info["real_name"]))
    nodo_ant_man.info["real_name"] = "Scott Lang"
    print("   Nombre actualizado: {}".format(nodo_ant_man.info["real_name"]))
else:
    print("   Ant Man no se encuentra en la lista.")


print("\n9. Personajes con 'time-traveling' o 'suit' en su biografia:")
aux = lista_personajes.inicio
while aux is not None:
    biografia = aux.info["short_bio"].lower()
    if "time-traveling" in biografia or "suit" in biografia:
        print("   {}: {}".format(aux.info["name"], aux.info["short_bio"]))
    aux = aux.sig


print("\n10. Eliminando Electro y Baron Zemo:")
for nombre in ("Electro", "Baron Zemo"):
    personaje_eliminado = eliminar(lista_personajes, nombre, "name")
    if personaje_eliminado is not None:
        print("\n   {} eliminado:".format(nombre))
        mostrar_personaje(personaje_eliminado)
    else:
        print("\n   {} no estaba en la lista.".format(nombre))
