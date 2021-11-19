memo = {}
# with memo
def fib(n):
    if n<=2:
        return 1
    if n in memo:
        return memo[n]
    else:
        f = fib(n-1)+fib(n-2)
    memo[n] = f
    return f
# without memo
def fib2(n):
    if(n<=2):
        return 1
    else:
        return fib2(n-1)+fib2(n-2)
print(fib(55))
