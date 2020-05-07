def wurzel(x, n=10):
    if n == 1:
        return 1
    else:
        return 0.5 * (wurzel(x, n - 1) + x / wurzel(x, n - 1))


print(wurzel(20))
