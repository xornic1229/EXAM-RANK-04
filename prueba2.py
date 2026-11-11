
def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i:] + arr1[:i] == arr2:
            return True
    return len(arr1) == 0


def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    resultado = []
    i = 0
    while i < dim:
        row = ""
        j = 0
        while j < dim:
            if (i, j) in stars:
                row += '*'
            else:
                row += '.'
            j += 1
        resultado += [row]
        i += 1
    return resultado


def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if lists == []:
        return []
    resultado = []
    for i in lists[0]:
        if i not in resultado:
            resultado += [i]
    for lista in lists:
        resultado = [num for num in resultado if num in lista]
    return resultado


def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    resultado = []
    for lista in lists:
        resultado += lista
    resultado2 = []
    while resultado != []:
        numero = min(resultado)
        resultado2 += [numero]
        resultado.remove(numero)
    return resultado2

def palindrome_partitioner(s: str) -> int:
    if s== s[::-1]:
        return 0
    tamaño = len(s)
    i = 1
    mejor = tamaño - 1
    while i<tamaño:
        trozo = s[:i]
        if trozo == trozo[::-1]:
            cortes = 1+ palindrome_partitioner(s[i:])
            if mejor > cortes:
                mejor = cortes
        i +=1
    return mejor


def palindrome_partitioner(s: str) -> int:
    if s== s[::-1]:
        return 0
    tamaño = len(s)
    mejor = tamaño-1
    i = 1
    while i<tamaño:
        trozo = s[:i]
        if trozo == trozo[::-1]:
            cortes = 1+ palindrome_partitioner(s[i:])
            if mejor>cortes:
                mejor = cortes
        i+=1
    return mejor

def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    pendientes = packages
    resultado  = []
    while pendientes:
        ready = []
        for paquete in pendientes:
            listo = 1
            necesita = packages[paquete]
            for requerimiento in necesita:
                if requerimiento not in resultado:
                    listo = 0
            if listo == 1:
                ready.append(paquete)
        if ready== []:
            return []
        resultado+=ready
        for paquete in ready:
            pendientes.remove(paquete)
    return resultado


def palindrome_partitioner(s: str) -> int:
    if s==s[::-1]:
        return 0
    tamaño = len(s)
    coste = tamaño -1
    i = 1
    while i<tamaño:
        trozo = s[:i]
        if trozo == trozo[::-1]:
            cortes = 1 + palindrome_partitioner(s[i:])
            if coste > cortes:
                coste == cortes
        i+=1
    return coste

def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    pendientes = sorted(packages)
    solucion = []
    while pendientes:
        ready = []
        for paquete in packages:
            listo = 1
            necesita = packages[paquete]
            for elemento in necesita:
                if elemento in packages and packages not in solucion:
                    listo = 0
            if listo == 1:
                ready.append(paquete)
        if ready == []:
            return []
        solucion += ready
        for e in ready:
            pendientes.remove(e)
    return solucion