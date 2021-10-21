def pivotIndex(nums):

    N = len(nums)
    if N == 0:
        return -1

    if N == 1:
        return 0

    summ = sum(nums)
    left_sum, right_sum = 0, summ
    for i in range(N):
        right_sum -= nums[i]
        if left_sum == right_sum:
            return i

        left_sum += nums[i]

    return -1

arr = [1,7,3,6,5,6]
print(pivotIndex(arr))