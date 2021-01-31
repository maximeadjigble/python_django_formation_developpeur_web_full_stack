class Utilisateur:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.email = None

    def info(self):
        print(self.nom , self.prenom, self.age, self.email)

    def changer_email(self, email):
        self.email = email


class Administrateur(Utilisateur):
    def interface_admin(self):
        print("Bienvenue dans l'interface administrateur")
        print(self.nom , self.prenom, self.age, self.email)

bruce = Administrateur("Bruce", "Willis", 38)
alice = Utilisateur("Eve", "Alice", 36)

bruce.interface_admin()
alice.info()
