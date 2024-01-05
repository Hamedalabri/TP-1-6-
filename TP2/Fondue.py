BASE = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400
print("Entrez le nombre de personne(s) conviées à la fondue :")
nbConvives =input()
nbConvives =int(nbConvives)
fromage = fromage * nbConvives / BASE
eau = eau * nbConvives / BASE
ail = ail * nbConvives / BASE
pain = pain * nbConvives / BASE
print("Pour faire une fondue fribourgeoise pour 3 personnes, il vous faut: ")
print(fromage," gr de fromage")
print(eau," dl d'eau")
print(ail," gousse(s) d'ail")
print(pain,"gr de pain")
