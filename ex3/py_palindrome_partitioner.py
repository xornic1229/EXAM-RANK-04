
def palindrome_partitioner(s: str) -> int:
    if s == s[::-1]:
        return 0

    n = 0
    for c in s:
        n += 1

    mejor = n - 1
    i = 1

    while i < n:
        parte = s[:i]

        if parte == parte[::-1]:
            cortes = 1 + palindrome_partitioner(s[i:])
            if mejor>cortes:
                mejor = cortes

        i += 1

    return mejor
