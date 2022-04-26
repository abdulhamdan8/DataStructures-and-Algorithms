def generate(numRows: int):
    result = []
    for i in range(numRows):
        temp_list = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(result[i - 1][j - 1] + result[i - 1][j])
        result.append(temp_list)
    return result

print(generate(5))