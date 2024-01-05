import time
"""n = int(input("Veuillez saisir un nombre entier positif : "))


if n < 0:
    print("Veuillez saisir un nombre entier positif.")
else:
    
    for i in range(n, -1, -1):
        print(i)
"""


n = int(input("Veuillez saisir un nombre entier positif : "))


if n < 0:
    print("Veuillez saisir un nombre entier positif.")
else:
    
    i = n
    while i >= 0:
        print(i)
        i = i -1
        time.sleep(1)
