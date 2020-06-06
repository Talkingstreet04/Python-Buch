"""
In files kann man nur Strings speichern.
"""
def speichern(s, dateiname):
    try:
        datei = open(dateiname, "w")
        for i in s:
            datei.write(str(i)+"\n")
        datei.close()
    except:
        print("Speichern war nicht möglich.")



liste = ["abaufa", 234567.4, -17]
speichern(liste, "D:\Daten\Dokumente\Dev\Python-Buch\Kapitel 9\\name")
file = open("D:\Daten\Dokumente\Dev\Python-Buch\Kapitel 9\\name", "r")
daten = file.read()
print(daten)
