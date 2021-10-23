def merge_interval(arr):
    if arr == []:
        return []
    result = []
    arr.sort(key = lambda x:x[0])
    for i in arr:
        if result == [] or result[-1][1] < i[0]:
            result.append(i)
        else:
            result[-1][1] = max(result[-1][1],i[1])
    return result


intervals = [[1,4],[0,4]]
print(merge_interval(intervals))