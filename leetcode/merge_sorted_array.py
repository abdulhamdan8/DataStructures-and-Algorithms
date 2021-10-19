def merge_sorted_array(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    i = j = k = 0
    temp = [None]*(n+m)
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            temp[k] = arr1[i]
            i += 1
            k += 1
        else:
            temp[k] = arr2[j]
            j += 1
            k += 1
    if(i<m):
        while(i<m):
            temp[k] = arr1[i]
            k+=1
    if j<n:
        while j<n:
            temp[k]=arr2[j]
            j+=1
            k+=1
    print(temp)




nums1 = [1, 2, 3]
nums2 = [2, 5, 6]
merge_sorted_array(nums1, nums2)
