import random


cards = [(suit, value) for suit in ["Pik", "Kreuz", "Herz", "Karo"] for value in ["Ass", "König", "Dame", "Bube",
                                    "Zehn", "Neun", "Acht", "Sieben"]]
for i in range(len(cards)):
    zufall = random.randint(0, 31)
    cards[i], cards[zufall] = cards[zufall], cards [i]

print(cards)
