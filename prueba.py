
def rotation(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    for i in range(len(arr1)):
        if arr1[i:] + arr1[:i] == arr2:
            return True

    return len(arr1) == 0


def estrellas(estrellas, tamaño):
    i = 0
    solucion = []

    while i < tamaño:
        j = 0
        row = ''

        while j < tamaño:
            if (i, j) in estrellas:
                row += '*'
            else:
                row += '.'
            j += 1

        i += 1
        solucion += [row]

    return solucion

def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []

    result = []
    for num in lists[0]:
        if num not in result:
            result.append(num)
    for lista in lists[1:]:
        result = [num for num in result if num in lista]
    return result


def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    lista_grande = []
    for lista in lists:
        lista_grande += lista

    result = []
    for i in range(len(lista_grande)):
        minimo = min(lista_grande)
        result += [minimo]
        lista_grande.remove(minimo)

    return result
