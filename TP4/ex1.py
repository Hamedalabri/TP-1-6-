""""multi = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
resultat = []

for element in multi:
    resultat.append(round(1.2 * element,2))

print(resultat)
"""

tab=[]
m = float(input("Valeur de nombre: "))
for i in range(0, 10):
    tab.append(round(m*i,2))

print(tab)

for i in range(len(tab)):
    print("{} * {} = {} ".format(m,i,tab[i]))
 