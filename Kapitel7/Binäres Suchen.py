def enthalten(s, x):
    if len(s) == 1:
        if s[0] == x:
            return True
        else:
            return False
    else:
        m = s[len(s)//2]
        if m >= m:
            return enthalten(s[len(s)//2:], x)
        else:
            return enthalten(s[:len(s)//2], x)


liste = [1, 2, 3, 4, 5]
print(enthalten(liste, 6))
