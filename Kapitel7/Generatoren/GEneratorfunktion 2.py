def generiereZahlen(n):
    i = 1
    while i <= n:
        yield i*i
        i += 1


g = generiereZahlen(3)
print(next(g))
print(next(g))
print(next(g))
