def suche(num, vorwahl):
    if len(num) == 1:
        if num[0][:len(vorwahl)] == vorwahl:
            return num
        else:
            return []
    else:
        return suche((num[:len(num) // 2]), vorwahl) + \
               suche(num[len(num) // 2:], vorwahl)


nummernliste = ["123456789", "12308476456", "41238765678"]
print(suche(nummernliste, "123"))
