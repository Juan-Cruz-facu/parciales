class nodoCola(object):
    info, sig = None, None


class Cola(object):
    def __init__(self):
        self.frente, self.final = None, None
        self.tamaño = 0


def arribo(cola, dato):
    nodo = nodoCola()
    nodo.info = dato
    if cola.frente is None:
        cola.frente = nodo
    else:
        cola.final.sig = nodo
    cola.final = nodo
    cola.tamaño += 1


def atencion(cola):
    dato = cola.frente.info
    cola.frente = cola.frente.sig
    if cola.frente is None:
        cola.final = None
    cola.tamaño -= 1
    return dato


def cola_vacia(cola):
    return cola.frente is None


def en_frente(cola):
    return cola.frente.info


def tamaño(cola):
    return cola.tamaño


def mover_al_final(cola):
    dato = atencion(cola)
    arribo(cola, dato)
    return dato


def barrido(cola):
    i = 0
    while i < tamaño(cola):
        print(mover_al_final(cola))
        i += 1
