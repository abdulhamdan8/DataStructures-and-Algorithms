def subarraySum(nums, k):
    sum_hash = {0: 1}
    s = 0
    count_sum = 0
    for i in nums:
        s += i
        if s - k in sum_hash:
            count_sum += sum_hash[s-k]
        if s in sum_hash:
            sum_hash[s] += 1
        else:
            sum_hash[s] = 1
    return count_sum


arr = [1,-1,0]
k = 0
# print(nums[1:1])
print(subarraySum(arr, k))
