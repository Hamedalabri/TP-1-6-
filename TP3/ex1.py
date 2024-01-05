"""ex: a)
s = 0

n = int(input("Valeur de n: "))
for i in range(0, n+1):
    s = s + i

print("La somme est:", s)

ex b)

while True:
    n = int(input("Valeur de n: "))
    if n== 100:
        break
    
#ex c)
nb10 = 0
nb15 = 0
nb20 = 0

for i in range(10):
    n = int(input("Valeur de n: "))
    
    while n < 0 or n > 20:
        print("n est =", n)
        n = int(input("Valeur de n: "))
    
    if n < 10:
        nb10 += 1
    elif 10 <= n < 15:
        nb15 += 1
    elif n >= 15:
        nb20 += 1
    else:
        print("Il faut réécrire la valeur")

print("Nombre de valeurs inférieures à 10:", nb10)
print("Nombre de valeurs entre 10 et 15 inclus:", nb15)
print("Nombre de valeurs supérieures ou égales à 15:", nb20)


#exd)
s = int(input("Valeur de s: "))
x=0
somme=0
while somme<= s:
    x= x+1
    somme = somme + x

print("la somme est: ", somme ,"et le Nbn le plus grand est:",x)

"""







