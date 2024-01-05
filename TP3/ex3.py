import random

random = random.randint(0, 100)

i = 0


print("devinez un Nbr entre 0 et 100")

while True:
    
    n = int(input("Votre guess : "))

    
    i = i + 1

    if n < i:
        print("Plus grand !")
    elif n > i:
        print("Plus petit !")
    else:
        print(f"Bravo ! Vous avez trouvé le nombre mystère en { i} essaie.")
        break