def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    seconde = temps[3]
    minute = temps[2] * 60
    heure = temps[1] * 3600
    jours = temps[0] * 86400

    return seconde + minute + heure + jours


def secondeEnTemps(temps):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jours = temps // 86400 
    heure = (temps // 3600) % 24
    minute = (temps // 60) % 60
    seconde = temps % 60

    return jours, heure, minute, seconde


def afficheTemps(temps):

    A = ["jour", "heure", "minute" ,"seconde"]  

    for i in range(0, 4) :
    
        if temps[i] > 1 :
        
            A[i] += "s"

            print(temps[i], A[i], end=" ")

        elif temps[i] == 1 :

            print(temps[i], A[i], end=" ")

    pass


def demandeTemps(temps):
    
    temps = [0, 0, 0, 0]

    for i in range(0, 4) :
        
        G = 0
        
        temps[i] = int(input("entrer jours heures minutes et secondes"))

        if temps[i] < 0 or (temps[i] > 60 and i != 0) :
            
            G = 1 
        
        while G == 1 :

            temps[i] = int(input("entrer une information valide")) 

            if temps[i] < 0 or (temps[i] > 60 and i != 0) :
                
                G = 1
            
            else :

                G = 0 
        
    temps = secondeEnTemps(tempsEnSeconde(temps))
     
    return temps


def sommeTemps(temps1,temps2):
    
    temps = [0, 0, 0, 0]

    for i in range(0, 4) :
        
        temps[i] = temps1[i] + temps2[i]

    temps = secondeEnTemps(tempsEnSeconde(temps))
    
    return temps


def proportionTemps(temps, proportion):#Sert a calculer une proportion de temp

    proTemps = [0, 0, 0, 0] 

    for i in range(0, 4) :

        proTemps[i] = temps[i] * proportion
    
    proTemps = secondeEnTemps(tempsEnSeconde(proTemps))
    
    return proTemps 


def tempsEnDate(temps):

    Dtemps = [0, 0, 0, temps[1], temps[2], temps[3]]

    Dtemps[0] = temps[0] // 365
    Feb = 28
    Month = 1
    Dtemps[1] = temps[0] % 365

    while Dtemps[1] > 0 :
        Dtemps[2] = Dtemps[1]

        if Month == 4 or Month == 6 or Month == 9 or Month == 11 :
            Dtemps[1] -= 30

        elif Month == 2 :  
            Dtemps[1] -= Feb

        else :
            Dtemps[1] -= 31
        Month += 1
        
    Dtemps[1] = Month - 1
    Dtemps[0] += 1970

    return Dtemps


def afficheDate(date):

    date[1] -= 1

    Month = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "décembre"]
    
    i = date[1]
    date[1] = Month[i]
    
    print(date[2], date[1], date[0], end=" ")
    
    print("à", date[3], end=":")
    print(date[4], end=":")
    print(date[5], end=" ")

    pass


def nombreBisextile(jour):
        
    Year = (jour // 365)
    N = 0

    for i in range(1972, Year + 1971, 4) :
        
        Bis = i % 100
        Bis2 = i % 400
        jour -= 1095

        if Bis == 0 and Bis2 != 0 :
            jour -= 365

        else :
            jour -= 366
            
            N += 1

    N -= 1

    return N


def tempsEnDateBisextile(temps):
    
    Bis = nombreBisextile(temps[0])
    temps = [temps[0] - Bis, temps[1], temps[2], temps[3]]
    temps = tempsEnDate(temps)
        
    return temps




