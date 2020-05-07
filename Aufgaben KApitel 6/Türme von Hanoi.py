def bewegungen(n, von, nach, über):
    if n == 1:
        print("Lege eine Scheibe von", von, "nach", nach, ".")
    else:
        bewegungen(n-1, von, über, nach)
        bewegungen(1, von, nach, über)
        bewegungen(n-1, über, nach, von)

bewegungen(2, 1, 7, 5)