# chartmanager.py

# Funktionsdefinitionen
def eingabe(charts):
    print("Eintragungen (mit ENTER beenden)")
    titel = input("Titel: ")
    while titel:
        interpret = input("Interpret: ")
        charts += [[0, titel, interpret]]
        titel = input("Titel: ")
    print()
    print("Vielen Dank. Die Liste wird gespeichert")


def speichern(charts):
    import pickle
    f = open("C:\\Users\pepat\\OneDrive\\Dokumente\\Dev\\Python-Buch\\Kapitel7\\Charts\\Charts", "wb")
    pickle.dump(charts, f)
    f.close()


def ausgabe(charts):
    print("Die Charts")
    print("---------------")
    for i in range(len(charts)):
        eintrag = charts[i]
        print("Platz", i+1, ":", eintrag[1], "\t von",
              eintrag[2], "\t", eintrag[0], "Stimmen")


# Hauptprogramm
print("Erstellen sie eine Hitliste")
charts = []
eingabe(charts)
ausgabe(charts)
speichern(charts)
