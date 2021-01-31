prenom = "Benois"

print("Avant", prenom)
# def salutations():
#     prenom = "Romaric"
#     print("Dans", prenom)
#     print("Bonjour", prenom)

def salutations(prenom = "Romaric"):
    print("Dans", prenom)
    print("Bonjour", prenom)

salutations("Alexandres")

print("Après", prenom)
