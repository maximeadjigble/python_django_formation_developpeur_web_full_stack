# Création
emails = { "email1@gmail.com", "email2@gmail.com","email3@gmail.com" }
emails2 = { "email1@gmail.com", "email2@gmail.com","email3@gmail.com", "email1@gmail.com", "email1@gmail.com", "email1@gmail.com", "email1@gmail.com" }
print(emails)
print(emails2)
print(type(emails))
print(len(emails2))

# Accès (Pas possible)
# emails[0]

# Opérateur in
print("email6@gmail.com" in emails)

# Méthodes
emails.add("email4@gmail.com")
emails.add("email6@gmail.com")
print(emails)

emails.remove("email1@gmail.com")
print(emails)

email = emails.pop()
print(email)
print(emails)