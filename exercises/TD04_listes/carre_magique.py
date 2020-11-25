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
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
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
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    A = []

    for i in carre:
        o = 0

        for n in range(4):
            o +=i[n] 

        A.append(o)

    if A.count(A[0]) == 4:
        return A[0]

    return -1

    pass

print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))