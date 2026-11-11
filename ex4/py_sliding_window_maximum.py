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