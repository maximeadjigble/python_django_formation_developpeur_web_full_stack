class Utilisateur:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.email = None

    def changer_email(self, email):
        self.email = email

    def nom_complet(self):
        print(self.nom , self.prenom, self.age, self.email)

    def age_an_prochain(self):
        return self.age + 1


bruce = Utilisateur("Bruce", "Willis", 38)
alice = Utilisateur("Eve", "Alice", 36)


bruce.changer_email("bruce.willis@gmail.com")

bruce.nom_complet()
alice.nom_complet()

# age_bruce_an_prochain = bruce.age_an_prochain()
# print(age_bruce_an_prochain)

# print("Bruce |", bruce.nom, bruce.prenom, bruce.age)
# print("Alice |", alice.nom, alice.prenom, alice.age)





# texte = "Hello World!"
# print(texte.lower())