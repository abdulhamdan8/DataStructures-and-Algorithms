import math
def jump_search(arr, key):
    n = len(arr)
    left = 0
    right = int(math.sqrt(n))
    while (right < n) and (arr[right] <= key):
        left = right
        right = int(math.sqrt(n)) + right
        if right > (n - 1):
            right = n

    for i in range(left, right):
        if arr[i] == key:
            return i + 1
    else:
        return "not found"


arr = [1, 3, 4, 5, 6, 7, 8, 9, 10]
key = 9
print(jump_search(arr, key))
