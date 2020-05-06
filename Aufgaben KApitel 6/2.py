def zufallsbuchstabe():
    buchstaben = "QWERTZUIOPÜASDFGHJKLÖÄYXCVBNM"
    import random
    return str(buchstaben[random.randint(1, 29)])


def kryptographie(s, n=1):
    s.upper()
    text = ""
    for a in s:
        text += a
        for zahl in range(n):
            text += zufallsbuchstabe()
    return text
print(kryptographie("test", 3))