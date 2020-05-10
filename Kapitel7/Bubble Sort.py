import random


def bubblesort(s):
    if len(s) > 1:
        for i in range(len(s) - 1):
            for j in range(len(s) - 1):
                if s[j] > s[j + 1]:
                    s[j], s[j + 1] = s[j + 1], s[j]
            print(s)


liste = [random.randint(1, 100000) for i in range(10000)]
bubblesort(liste)
