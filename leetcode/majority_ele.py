def majorityElement(nums):
    x = {}
    majority = len(nums) // 2
    for i in nums:
        if not i in x:
            x[i] = 1
        else:
            x[i] += 1
    print(x)
    for i in x:
        if x[i]>majority:
            return i
arr = [2,2,1,1,1,2,2]
print(majorityElement(arr))