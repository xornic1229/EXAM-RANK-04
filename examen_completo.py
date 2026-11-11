
# 01
def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if len(arr1)!= len(arr2):
        return 0
    i = 0
    while i<len(arr1):
        if arr1[i:]+arr1[:i]==arr2:
            return 1
        i+=1
    return 0


# 02
def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    resultado = []
    i = 0
    while i<dim:
        row = ''
        j= 0
        while j<dim:
            if (i,j) in stars:
                row+='*'
            else:
                row+='.'
            j+=1
        resultado+=[row]
        i+=1


# 03
def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    resultado = []
    for numero in lists[0]:
        if numero not in resultado:
            resultado.append(numero)
    for lista in lists:
        resultado = [num for num in resultado if num in lista]
    return resultado


# 04
def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    grande = []
    resultado = []
    for lista in lists:
        grande+=lista
    for i in range(len(grande)):
        minimo = min(grande)
        grande.remove(minimo)
        resultado.append(minimo)
    return resultado


# 05
def palindrome_partitioner(s: str) -> int:
    if s==s[::-1]:
        return 0
    mejor = len(s)-1
    i = 1
    while i<len(s):
        parte = s[:i]
        if parte == parte[::-1]:
            corte = 1+ palindrome_partitioner(s[i:])
            if mejor > corte:
                mejor = corte
        i+=1
    return mejor


# 06
def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    paquetes = sorted(packages)
    resultado = []
    while paquetes:
        ready = []
        for paquete in paquetes:
            listo = 1
            for dependencia in packages[paquete]:
                if dependencia not in resultado and dependencia in paquetes:
                    listo = 0
            if listo ==1:
                ready.append(paquete)
        if ready==[]:
            return []
        for paq in ready:
            resultado.append(paq)
            paquetes.remove(paq)
    return resultado


# 07

def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    n = 0
    for num in nums:
        n += 1
    if k <= 0 or k > n:
        return []
    resultado = []
    i = 0
    while i + k <= n:
        mejor = nums[i]
        j = 1
        while j < k:
            if nums[j+i] > mejor:
                mejor = nums[j+i]
            j += 1
        resultado += [mejor]
        i += 1
    return resultado
