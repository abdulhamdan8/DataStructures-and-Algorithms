# day 4
# Time complexity=O(n2)
# space complexity=O(n)


def selection_sort(ar):
    for i in range(len(ar)):
        min_index = i
        for j in range(i + 1, len(ar)):
            if ar[min_index] > ar[j]:
                min_index = j
        ar[i], ar[min_index] = ar[min_index], ar[i]

    return ar


arr = list(map(int, input().split()))
print(selection_sort(arr))
