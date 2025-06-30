def sum_(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return n + sum_(n-1)
print(sum_(8))