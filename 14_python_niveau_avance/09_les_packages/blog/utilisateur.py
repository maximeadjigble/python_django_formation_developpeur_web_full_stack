class Auteur():
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def info(self):
        print(self.nom, self.prenom)