carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
carre_pas_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 7, 13]]


def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for i in carre:
        print(" ".join([str(j) for j in i]))
    print()
    pass


afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre """
    Lignes = []
    for i in carre:
        Lignes.append(sum(i))

    if Lignes.count(Lignes[0]) == 4:
        return Lignes[0]

    return -1


print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))


def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre """
    Collones = []

    for i in range(4):
        o = 0
        for j in carre:
            o += j[i]
        Collones.append(o)

    if Collones.count(Collones[0]) == 4:
        return Collones[0]

    return -1


print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))


def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre"""
    Diagonnales = [[], []]
    for n in range(4):
        Diagonnales[0].append(carre[n][n])
        Diagonnales[1].append(carre[n][3 - n])

    Diagonnales = [sum(Diagonnales[0]), sum(Diagonnales[1])]

    if Diagonnales.count(Diagonnales[0]) == 2:
        return Diagonnales[0]

    return -1


print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))


def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    o = []
    o.append(testColonnesEgales(carre))
    o.append(testLignesEgales(carre))
    o.append(testDiagonalesEgales(carre))

    if o.count(o[0]) == 3:
        return True

    return False


print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))


def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille
        du carré, et False sinon """
    Liste = []
    for i in carre:
        for n in i:
            Liste.append(n)

    Liste.sort()
    Valeurs = [i + 1 for i in range(len(carre) ** 2)]

    if Liste == Valeurs:
        return True

    return False


print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))
