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
