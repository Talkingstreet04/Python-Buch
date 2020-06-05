import random
def zahlen():
     x = random.randint(10, 100)
     y = random.randint(10, 100)
     return  [x, y]
while True:
    nummern = zahlen()
    antwort = int(input("Multipliziere" + str(nummern) + ":" ))
    if antwort == nummern[0] * nummern[1]:
        print("Richtig")
    else:
        print("Falsch")