
import heapq

def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    heap = []
    result = []

    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i][0], i, 0))

    while heap:
        num, i, j = heapq.heappop(heap)
        result.append(num)

        if j + 1 < len(lists[i]):
            heapq.heappush(heap, (lists[i][j + 1], i, j + 1))

    return result
