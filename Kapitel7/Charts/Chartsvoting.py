import pickle


def laden():
    try:
        f = open("C:\\Users\pepat\\OneDrive\\Dokumente\\Dev\\Python-Buch\\Kapitel7\\Charts\\Charts", "rb")
        charts = pickle.load(f)
        f.close()
    except:
        charts = []
    return  charts


def ausgabe(charts):
    print("Die Charts")
    print("------------")
    for i in range(len(charts)):
        eintrag = charts[i]
        print("Paltz", i+1, ":", eintrag[1], "\t von",
              eintrag[2], "\t", eintrag[0], "Stimmen")


def voting(charts):
    if charts == []:
        print("Sorry, keine Wahl möglich.")
    else:
        print("Die Charts")
        print()
        ausgabe(charts)
        print("Bitte wählen Sie Ihren Favoriten!",
              "(1 bis "+str(len(charts))+")")
        wahl = int(input("Nummer: ")) - 1
        charts[wahl][0] += 1
        charts.sort(reverse=True)
        print("Vielen Dank für Ihr Voting!")


def speichern(charts):
    f = open("C:\\Users\pepat\\OneDrive\\Dokumente\\Dev\\Python-Buch\\Kapitel7\\Charts\\Charts", "wb")
    pickle.dump(charts, f)
    f.close()


charts = laden()
voting(charts)
speichern(charts)
print("Hier der aktuelle Stand")
ausgabe(charts)
