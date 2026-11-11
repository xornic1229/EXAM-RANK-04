
def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if len(arr1)!=len(arr2):
        return 0
    i = 0
    while i<len(arr1):
        if arr1[i:]+arr1[:i] == arr2:
            return 1
        i+=1
    return 0

def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    resultado = []
    i = 0
    while i<dim:
        row = ''
        j = 0
        while j<dim:
            if (i,j) in stars:
                row+='*'
            else:
                row+='.'
            j+=1
        resultado+=[row]
        i+=1
    return resultado

def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    resultado = []
    for i in lists[0]:
        if i not in resultado:
            resultado.append(i)
    for list in lists:
        resultado = [num for num in resultado if num in list]
    return resultado

def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    grande = []
    for list in lists:
        grande += list
    resultado = []
    for i in range(len(grande)):
            minimo = min(grande)
            result += [minimo]
            grande.remove(minimo)
    return resultado



def palindrome_partitioner(s: str) -> int:
    if s == s[::-1]:
        return 0

    tamaño = 0
    for c in s:
        tamaño += 1

    mejor = tamaño - 1
    i = 1

    while i < tamaño:
        parte = s[:i]

        if parte == parte[::-1]:
            coste = 1 + palindrome_partitioner(s[i:])
            if mejor > coste:
                mejor = coste

        i += 1

    return mejor


def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    pendientes = sorted(packages)
    resultado = []
    while pendientes:
        ready = []
        for paquete in pendientes:
            listo = 1
            for dependencia in packages[paquete]:
                if dependencia not in resultado and dependencia in pendientes:
                    listo = 0
            if listo ==1:
                ready.append(paquete)
        if ready== []:
            return []
        for paquete in ready:
            resultado.append(paquete)
            pendientes.remove(paquete)
    return resultado


def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    n = 0
    for num in nums:
        n += 1

    if k <= 0 or k > n:
        return []

    resultado = []
    i = 0
    while i+k<=n:
        mejor = nums[i]
        a = 1
        while a < k:
            if nums[i+a] > mejor:
                mejor = nums[i+a]
            a+=1
        resultado += [mejor]
        i+=1
    return resultado


