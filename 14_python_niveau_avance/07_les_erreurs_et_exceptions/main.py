annees = 10
vues = 1000
vues_par_an = 0

try:
    vues_par_an = vues/annees
    print("Pas d'exception")
except ZeroDivisionError:
    print("Entrez une année > 0")
except Exception as e:
    print("On a une autre exception", e)

print(vues_par_an)