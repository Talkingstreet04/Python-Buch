eingegebene_nummer = "0"
while eingegebene_nummer:
    finisher_liste = open("D:/Daten/Dokumente/Dev/Python-Buch/Kapitel 9/finisher_liste.txt", "a")
    eingegebene_nummer = input("Startnummer: ") + "\n"
    finisher_liste.write(eingegebene_nummer)
    finisher_liste.close()
