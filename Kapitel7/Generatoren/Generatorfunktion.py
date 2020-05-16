def generiereZahlen(n):
    for i in range(n):
        yield i*i

g = generiereZahlen(9)
for z in g:
    print(z, end=" ")