def calculer_prix_location(heure_debut, heure_fin):
    # Vérifier si les heures sont valides
    if heure_debut < 0 or heure_debut > 24 or heure_fin < 0 or heure_fin > 24:
        print("Les heures doivent être comprises entre 0 et 24 !\n")
        return

    # Vérifier si l'heure de début est identique à l'heure de fin
    if heure_debut == heure_fin:
        print("Attention ! L'heure de fin est identique à l'heure de début.\n")
        return

    # Vérifier si l'heure de début est supérieure à l'heure de fin
    if heure_debut > heure_fin:
        print("Attention ! L'heure de début de la location est après l'heure de fin.\n")
        return

    # Calculer le coût de la location en fonction des tarifs
    if heure_debut >= 0 and heure_debut < 7 or heure_debut >= 17 and heure_debut <= 24:
        tarif = 1
    else:
        tarif = 2

    duree_location = heure_fin - heure_debut
    cout_location = tarif * duree_location

    # Afficher le coût de la location
    print(f"Le coût de la location est de {cout_location} euros.")

# Demander à l'utilisateur les heures de début et de fin de location
try:
    heure_debut = int(input("Veuillez entrer l'heure de début de la location : "))
    heure_fin = int(input("Veuillez entrer l'heure de fin de la location : "))

    # Appeler la fonction de calcul du prix de location
    calculer_prix_location(heure_debut, heure_fin)

except ValueError:
    print("Erreur ! Veuillez entrer des valeurs numériques pour les heures de début et de fin.")
