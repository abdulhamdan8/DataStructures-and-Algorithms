def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return f"key found at position {i+1}"
    else:
        return "key not found"


array = list(map(int, input().split()))
key = int(input())
print(linear_search(array, key))
