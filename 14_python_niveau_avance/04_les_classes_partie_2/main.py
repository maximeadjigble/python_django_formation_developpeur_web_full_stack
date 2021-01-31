# age = 25
# prenom = "Olivier"
# utilisateurs = ["Oliver", "Benois", "Clement"]

# print(type(age))
# print(type(prenom))
# print(type(utilisateurs))

# print(prenom.upper())

# class Utilisateur:
#     nom = "Willis"
#     prenom = "Bruce"
#     age = 65

# bruce = Utilisateur()
# alice = Utilisateur()


class Utilisateur:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

bruce = Utilisateur("Bruce", "Willis", 38)
alice = Utilisateur("Eve", "Alice", 36)

print("Bruce |", bruce.nom, bruce.prenom, bruce.age)
print("Alice |", alice.nom, alice.prenom, alice.age)
# print("Class |", Utilisateur.nom, Utilisateur.prenom, Utilisateur.age)
