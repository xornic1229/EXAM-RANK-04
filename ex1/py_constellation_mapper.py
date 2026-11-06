
def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    result = []
    i = 0

    while i < dim:
        row = ""
        j = 0
        while j < dim:
            if (i, j) in stars:
                row += "*"
            else:
                row += "."
            j += 1
        result += [row]
        i += 1

    return result
