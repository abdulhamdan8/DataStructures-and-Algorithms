def climbing_stairs(n):
    path = {1:1,2:2}
    for i in range(3,n+1):
        path[i] = path[i-1]+path[i-2]
    return path[n]

print(climbing_stairs(45))