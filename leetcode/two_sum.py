def two_sum(arr, target):
    map = {}
    for i in range(len(arr)):
        x = target - arr[i]
        if x in map:
            return [i, map[x]]
        else:
            map[arr[i]] = i

def two_sum_2poiner(arr,target):
    i=0
    j=len(arr)-1
    while(i<j):
        if arr[i]+arr[j] == target:
            return [i,j]
        elif arr[i]+arr[j] > target:
            j-=1
        else:
            i+=1
    return -1

nums = [2, 7, 11, 15]
target = 9
print(two_sum_2poiner(nums, target))
