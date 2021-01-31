# Déclaration
def ma_fonction():
    print("Hello World!")
    print("Bonjour à tous")


# Utilisation
ma_fonction()
ma_fonction()
ma_fonction()

# Arguments de fonction
def salutations(prenom):
    print("Bonjour:", prenom)

salutations("Maxime")
salutations("Benois")

# def salutations(prenom, nom):
#     print("Bonjour", prenom, nom)

# salutations("Georges", "Agier")


# Valeur retournée
def carre(x = 2):
    # print(x, "au carré =", x*x)
    return x*x

# nombre_carre = carre(6)
# print(nombre_carre)

# Parametres par défaut
nombre_carre = carre(5)
print(nombre_carre)
