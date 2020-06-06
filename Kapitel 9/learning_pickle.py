import pickle


number = 12
file_write = open("D:/Daten/Dokumente/Dev/Python-Buch/Kapitel 9/daten.txt", "wb")
pickle.dump(number, file_write)
file_write.close()
file_read = open("D:/Daten/Dokumente/Dev/Python-Buch/Kapitel 9/daten.txt", "rb")
print(pickle.load(file_read))
file_read.close()
