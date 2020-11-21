def AfficheValeur(a):
    """ Affiche la valeur de a en fonction de son argument """
    if a < 0:
        for i in range(3):
            a -= 7
            print(a)
    else:
        print(1)

    pass


help(AfficheValeur)


def Coordonne(prenom, nom):
    """ print des coordonnées """
    nom = "Dupont"
    ville = "Paris"

    print(prenom + nom + " habite à ville " + ville)

    pass