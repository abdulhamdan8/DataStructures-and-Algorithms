# day 3
# merge Sort
# time complexity O(n2)


def insertion_sort(ar):
    for i in range(1, len(ar)):
        current = ar[i]
        j = i - 1
        while j >= 0 and ar[j] > current:
            ar[j + 1] = ar[j]
            j -= 1
        ar[j + 1] = current
    return ar


# driver code
arr = list(map(int, input().split()))
print(insertion_sort(arr))
