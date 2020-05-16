def findeNachbarräume(plan, raum):
    """ Menge aller Nachbarräume """
    raeume, tueren = plan
    t_raum = set(t for t in tueren if raum in t)
    nachbarraeume = set()
    for t in t_raum:
        nachbarraeume = nachbarraeume | t
    return nachbarraeume - set([raum])


def vereinige(plan1, plan2):
    """ füge zwei Pläne zusammen """
    return (plan1[0] | plan2[0], plan1[1] | plan2[1])


V1 = {1, 2, 3, 4, 5}
E1 = set(frozenset(t)
         for t in [(1, 2), (2, 3), (2, 4), (3, 4), (4, 5)])
raumplan1 = (V1, E1)

V2 = {4, 5, 6, 7}
E2 = set(frozenset(t)
         for t in [(4, 5), (5, 6), (6, 7), (5, 7)])
raumplan2 = (V2, E2)

gesamtplan = vereinige(raumplan1, raumplan2)
nachbarraume = findeNachbarräume(gesamtplan, 7)
print("Die Räume des Gesamtplans:")
for r in gesamtplan[0]: print(r, end=" ")
print()
print("Türen des Gesamtplans:")
for t in gesamtplan[1]: print(tuple(t), end=" ")
print()
print("Nachbarräume:")
for r in nachbarraume: print(r, end=" ")
