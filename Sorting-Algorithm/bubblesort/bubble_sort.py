# day 1
# bubble sort
#  time complexity = O(n2)

def bubble_sort(a):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

# driver code
arr=[9,8,76,5,4]
print("Before sorting",arr)
print("After Sorting",bubble_sort(arr))



