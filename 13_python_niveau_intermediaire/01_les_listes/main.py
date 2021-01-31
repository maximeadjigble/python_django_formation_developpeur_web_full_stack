# Création de liste
loto = [10, 17, 19, 23, 42]

# print(loto)
# print(loto[2])

villes = ["Paris", "New York", "Londres"]

# print(villes)
# print(villes[1])

ma_liste = [17, "Paris", 16.5]

# print(ma_liste)

# Méthodes de liste
# print(len(loto))
# print(len(villes))

villes.append("Rome")
villes.append("Tokyo")
print(villes)

villes.remove("New York")
print(villes)
print(len(villes))

# Tranchâge
print(loto[1:4])