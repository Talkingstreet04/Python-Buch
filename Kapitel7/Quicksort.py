import random


def quicksort(s):
    if len(s) <= 1:
        return s
    else:
        return quicksort([x for x in s[1:] if x < s[0]]) \
        +[s[0]] \
        + quicksort([y for y in s[1:] if y >= s[0]])


list = [random.randint(1, 1000000) for i in range(10000)]
print(quicksort(list))
