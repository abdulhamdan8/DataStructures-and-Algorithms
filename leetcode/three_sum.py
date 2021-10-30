def three_sum(arr):
    final_array = []
    arr.sort()
    for i in range(len(arr)-2):
        j=i+1
        k= len(arr)-1
        # if i>0 and arr[i]==arr[i-1]:continue
        while( j<k ):
            res = arr[i]+arr[j]+arr[k]
            if res<0:
                j-=1
            elif res>0:
                k-=1
            elif res == 0:
                final_array.append([arr[i],arr[j],arr[k]])
                # while j < len(arr) - 1 and arr[j] == arr[j + 1]: j += 1
                # while k > 0 and arr[k] == arr[k - 1]: k -= 1
                j += 1
                k -= 1
    return final_array

# def threeSum(nums):
#     nums.sort()
#     result = []
#     for i in range(len(nums) - 2):
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
#         l = i + 1
#         r = len(nums) - 1
#         while (l < r):
#             sum = nums[i] + nums[l] + nums[r]
#             if sum < 0:
#                 l += 1
#             elif sum > 0:
#                 r -= 1
#             else:
#                 result.append([nums[i], nums[l], nums[r]])
#                 while l < len(nums) - 1 and nums[l] == nums[l + 1]: l += 1
#                 while r > 0 and nums[r] == nums[r - 1]: r -= 1
#                 l += 1
#                 r -= 1
#     return result



nums =[-1,0,1,2,-1,-4]
print(three_sum(nums))