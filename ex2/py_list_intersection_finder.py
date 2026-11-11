
def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []

    result = []

    for num in lists[0]:
        if num not in result:
            result += [num]

    for lista in lists[1:]:
        result = [num for num in result if num in lista]

    return result
