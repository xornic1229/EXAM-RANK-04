
def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if len(arr1) != len(arr2):
        return False

    for i in range(len(arr1)):
        if arr1[i:] + arr1[:i] == arr2:
            return True

    return len(arr1) == 0
