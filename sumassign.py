def summed(n):
    if n==0:
        return 0
    else:
        return n + summed(n-1)
print(summed(n=int(input())))