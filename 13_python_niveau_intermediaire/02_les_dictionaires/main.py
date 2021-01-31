# Création de dictionaire
notes = {
    "Maxime": 12.4,
    "Romaric": 16.5,
    "Stephanie": 14.2,
    "Benois": 13 
}

print(type(notes))

# Accès aux valeurs
print(notes["Maxime"])
print(notes["Stephanie"])

# Modification
print(notes)
notes["Romaric"] = 14.0
print(notes)

# Méthodes et fonctions
print(len(notes))
print(type(notes.keys()))
cles = list(notes.keys())
print(type(cles))

print(notes.values())

# Opérateur in
print( "Maxime" in notes  )
print( "Celestine" in notes  )
resultat = "Maxime" in notes
print(resultat)