# day 1
# bubble sort
def bubble_sort(a):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

# driver code
arr=[9,8,76,5,4]
print(bubble_sort(arr))

# space and tim complexity = O(n2)


