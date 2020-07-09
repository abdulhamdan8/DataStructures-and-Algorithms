# quick sort
# time complexity=O(n2)


def quick_sort(arr, l, h):
    if l < h:
        pi = partition(arr, l, h)
        quick_sort(arr, l, pi - 1)
        quick_sort(arr, pi + 1, h)


def partition(arr, l, h):
    pivot = arr[l]
    i = l + 1
    j = h
    done = True
    while done:
        while i <= j and arr[i] < pivot:
            i += 1
        while arr[j] >= pivot and j >= i:
            j -= 1
        if j < i:
            done = False
        else:
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j


arr = list(map(int, input().split()))
quick_sort(arr, 0, len(arr) - 1)
print(arr)
