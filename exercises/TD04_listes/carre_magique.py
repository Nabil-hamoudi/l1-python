carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
carre_pas_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 7, 13]]


def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for i in carre:
        print(' '.join([str(j) for j in i]))
    print()
    pass


afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre """
    A = []

    for i in carre:
        o = 0

        for n in i:
            o += n

        A.append(o)

    if A.count(A[0]) == 4:
        return A[0]

    return -1


print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))


def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre """
    A = []

    for p in range(4):
        o = 0

        for i in carre:
            o += i[p]

        A.append(o)

    if A.count(A[0]) == 4:
        return A[0]

    return -1


print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))


def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre"""
    o = []
    for n in range(-4, 4):
        o.append(carre[n][n])

    o = [sum(o[:4]), sum(o[4:])]

    if o.count(o[0]) == 2:
        return o[0]

    return -1


print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))


def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    o = []
    o.append(testLignesEgales(carre))
    o.append(testColonnesEgales(carre))
    o.append(testDiagonalesEgales(carre))

    if o.count(o[0]) == 3:
        return True

    return False


print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))


def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    liste = [1 + i for i in range((len(carre)) ** 2)]
    liste2 = []

    for i in carre:
        liste2.extend(i)
        if len(i) != len(carre):
            return False

    liste2.sort()

    if liste == liste2:
        return True
    
    return False


print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))
