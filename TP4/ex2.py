# Demande le nombre d'étudiants à l'utilisateur
netd = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
somme=0.0
# déclaration d’une liste vide qui va contenir autant de notes que d'étudiants

notes = [] 
c=0
for i in range(0, netd+1):
    noteetd = int(input("Donnez le note d'etudiants : "))
    if 0 <= noteetd <= 20:
     notes.append(noteetd)
     moyenne = moyenne + noteetd
    else:
       print("veuillez saisir un nombre entre 0 et 20")
    
moyenne = moyenne/netd

for i in range(len(notes)):
    print("{} | {} | {}".format(i,notes[i],round(moyenne-notes[i],2)))
