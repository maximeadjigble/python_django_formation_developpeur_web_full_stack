# if False:
#     print("Condition valide")
# else:
#     print("Condition invalide")

# print("Fin du code")

username = "maxime" 
standard_users = ["romaric","hugo","benois"]
gold_users = ["clement", "maxime"]

if username in standard_users: 
    print("Bienvenue", username)
elif username in gold_users:
    print("Bienvenue dans la section Gold")
    print("Mr", username)
# elif username in premium_users:
#     print("Bienvenue dans la section Gold")
#     print("Mr", username)
else:
    print("Cette ressource n'est pas accéssible")
    print("Veuillez créer un compte")


print("Fin")



