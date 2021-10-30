def firstMissingPositive(nums):
    n = len(nums)
    temp = 0
    nums.sort()
    for i in range(n):
        if (nums[i] == temp + 1):
            temp += 1
    return temp + 1

nums = [2,5,0,1,3]
print(firstMissingPositive(nums))