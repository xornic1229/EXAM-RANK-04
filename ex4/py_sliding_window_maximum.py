
def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    n = 0
    for x in nums:
        n += 1

    if k <= 0 or k > n:
        return []

    queue = [0] * n
    head = 0
    tail = 0
    result = []

    i = 0
    while i < n:
        if head < tail and queue[head] <= i - k:
            head += 1

        while head < tail and nums[queue[tail - 1]] <= nums[i]:
            tail -= 1

        queue[tail] = i
        tail += 1

        if i >= k - 1:
            result += [nums[queue[head]]]

        i += 1

    return result
