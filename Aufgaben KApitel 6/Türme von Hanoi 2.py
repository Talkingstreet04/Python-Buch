def bewege(AnzahlanBausteinen, von, über, nach):
    if AnzahlanBausteinen == 1:
        print("von", von, "nach", nach)
    else:
        bewege(AnzahlanBausteinen - 1, von, nach, über)
        bewege(1, von, über, nach)
        bewege(AnzahlanBausteinen - 1, über, von, nach)


zahl = 0
bewege(10, 1, 2, 3)
