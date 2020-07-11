# iterative search

def binary_search(arr, l, r, key):
    while r >= l:
        mid = (l + r) // 2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            l = mid + 1
        else:
            r = mid - 1
    return False


arr = [1, 2, 3, 4, 5]
key = 10
x = binary_search(arr, 0, len(arr) - 1, key)
print(x)

# recursive search

# def binary_search(arr, l, r, key):
#     if r >= l:
#         mid = (l + r) // 2
#         if arr[mid] == key:
#             return f"found at position {mid + 1}"
#         elif arr[mid] > key:
#             return binary_search(arr, l, mid - 1, key)
#         else:
#             return binary_search(arr, mid + 1, r, key)
#     else:
#         return "not found"

