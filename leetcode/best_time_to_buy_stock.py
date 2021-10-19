def buyStock(arr):
    least_stock_value = arr[0]
    max_profit = 0
    for i in range(1, len(arr)):
        if arr[i] < least_stock_value:
            least_stock_value = arr[i]
        if arr[i] - least_stock_value > max_profit:
            max_profit = arr[i] - least_stock_value
    print(max_profit)


inp = [7,6,4,3,1]
buyStock(inp)
