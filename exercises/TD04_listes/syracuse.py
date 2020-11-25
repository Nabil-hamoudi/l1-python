def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = (n * 3) + 1
        liste.append(n)
    return liste


print(syracuse(3))


def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    for i in range(2, n_max + 1):
        syracuse(i)

    return True


print(testeConjecture(10000))


def tempsVol(n):
    """ Retourne le temps de vol de n """
    return len(syracuse(n))


print("Le temps de vol de", 3, "est", tempsVol(3))


def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    liste = [1]
    for i in range(2, n_max + 1):
        liste.append(tempsVol(i))

    return liste


print(tempsVolListe(100))


def VerTempsDeVol(n_max):
    liste2 = []
    liste = tempsVolListe(n_max)
    liste2 = liste.copy()
    liste2.sort()
    rep = liste.index(liste2[-1]) + 1
    return liste2[-1], rep


print(VerTempsDeVol(10000))


def syracuse2(n_max):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste2 = []
    for i in range(1, n_max + 1):
        liste = syracuse(i)
        liste.sort()
        liste2.append(liste[-1])
    liste = liste2.copy()
    liste2.sort()
    rep = liste.index(liste2[-1]) + 1
    return liste2[-1], rep


print(syracuse2(10000))


