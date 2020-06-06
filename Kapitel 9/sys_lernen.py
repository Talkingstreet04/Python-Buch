import sys
import pickle


daten_einlesen = open("D:/Daten/Dokumente/Dev/Python-Buch/Kapitel 9/daten.txt", "rb")
daten = pickle.load(daten_einlesen)
sys.stdout.write("Hallo " + str(daten))
