class nodoLista(object):
    info, sig = None, None


class Lista(object):
    def __init__(self):
        self.inicio = None
        self.tamaño = 0


def criterio(dato, campo=None):
    if campo is not None:
        if isinstance(dato, dict) and campo in dato:
            if dato[campo] is None and campo == "real_name":
                return ""
            return dato[campo]
        if hasattr(dato, campo):
            return getattr(dato, campo)
    return dato


def insertar(lista, dato, campo=None):
    nodo = nodoLista()
    nodo.info = dato
    if (lista.inicio is None or
            criterio(lista.inicio.info, campo) > criterio(nodo.info, campo)):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        anterior = lista.inicio
        actual = lista.inicio.sig
        while (actual is not None and
               criterio(actual.info, campo) < criterio(nodo.info, campo)):
            anterior = actual
            actual = actual.sig
        nodo.sig = actual
        anterior.sig = nodo
    lista.tamaño += 1


def buscar(lista, buscado, campo=None):
    aux = lista.inicio
    while (aux is not None and
           criterio(aux.info, campo) != criterio(buscado, campo)):
        aux = aux.sig
    return aux


def eliminar(lista, clave, campo=None):
    dato = None
    if lista.inicio is not None:
        if criterio(lista.inicio.info, campo) == criterio(clave, campo):
            dato = lista.inicio.info
            lista.inicio = lista.inicio.sig
            lista.tamaño -= 1
        else:
            anterior = lista.inicio
            actual = lista.inicio.sig
            while (actual is not None and
                   criterio(actual.info, campo) != criterio(clave, campo)):
                anterior = actual
                actual = actual.sig
            if actual is not None:
                dato = actual.info
                anterior.sig = actual.sig
                lista.tamaño -= 1
    return dato


def lista_vacia(lista):
    return lista.inicio is None


def tamaño(lista):
    return lista.tamaño


def barrido_lista(lista):
    aux = lista.inicio
    while aux is not None:
        print(aux.info)
        aux = aux.sig
