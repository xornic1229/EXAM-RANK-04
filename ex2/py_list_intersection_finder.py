
def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []

    result = []

    for num in lists[0]:
        if num in result:
            continue

        found = True
        for lista in lists:
            if num not in lista:
                found = False
                break

        if found:
            result += [num]

    return result
