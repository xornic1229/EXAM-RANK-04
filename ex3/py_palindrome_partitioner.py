
def palindrome_partitioner(s: str) -> int:
    n = 0
    for c in s:
        n += 1

    if n < 2:
        return 0

    cuts = []
    i = 0
    while i < n:
        cuts += [i]
        i += 1

    i = 0
    while i < n:
        for j in (0, 1):
            left = i
            right = i + j

            while left >= 0 and right < n and s[left] == s[right]:
                if left == 0:
                    new = 0
                else:
                    new = cuts[left - 1] + 1

                if new < cuts[right]:
                    cuts[right] = new

                left -= 1
                right += 1
        i += 1

    return cuts[-1]
