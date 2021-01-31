for i in [0,1,2,3,4,5,6]:
    # print(i*i)
    print(i**2)

for i in range(7):
    print(i)

villes = ["Paris", "Londres", "Rome", "Milan"]
for v in villes:
    print(v.upper())

population = {
    "Paris": 2.148,
    "Londres": 8.982,
    "Rome": 2.873,
    "Milan": 1.352
}

for v in population:
    # print(v)
    print(v, population[v])

for v in population.items():
    print(v[0], v[1])

for v, pop in population.items():
    print(v, pop)


print("Fin de la boucle")