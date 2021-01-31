# Création
villes = ("Paris", "Marseille", "Strasbourg")
print(villes)

pays = "France", "USA", "Maroc", "Italy"
print(type(pays))
print(pays)

loto = 1, 5, 10, 32, 24
print(loto)

# Accès
print(villes[2])

# Modification/Ajout (Pas possible)
# villes[0] = "Lille" 

# Déballage
n1 = loto[0]
n2 = loto[1]
print(n1, n2)

n1, n2, n3, n4, n5 = loto
print(n1, n2, n3)
print(len(loto))

# Concaténation
loto2 = 2, 6, 4
print(loto, loto2)

loto3 = loto + loto2
print(loto3)

