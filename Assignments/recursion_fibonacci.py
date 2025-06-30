# Here the initial values are taken as 1 and 2 instead of the default 0 and 1.
def fibonacci(n):
    if n==0:
        return 1
    if n==1:
        return 2
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))