import tkinter as tk

taille_fenetre = 50 #Taille de la fenêtre de recherche

def match_size(mot,i,j): #renvoie la longueur du plus grand sous-mot commun, dans le mot aux positions position i et j avec j < i
    k = 0
    while(i+k <len(mot) and mot[i+k]==mot[j+k]):
        k+=1
    return k

def max_match(mot,i): #renvoie le couple (position,taille) du plus grand match 
                      #trouvé dans mot à partir de la position i
    j = max(0,i-taille_fenetre)  #première position où chercher un match
    max_match = (0,0)
    while j < i: #on cherche un match dans la fenetre de recherche
        taille=match_size(mot,i,j)
        if(max_match[1]<taille):
            max_match=(j,taille)
        j +=1
    return max_match


def compresse():
    texte_a_compresser = entree.get()
    texte_compresse = [] #cette liste doit etre étendue pour contenir le texte compressé
    #construction du code LZ77
    i = 0
    while i < len(texte_a_compresser): #pour chaque lettre du texte
        courant=max_match(texte_a_compresser,i)
        if(courant[1] >=2):
            texte_compresse.append((i-courant[0],courant[1]))
            i += courant[1]
        else:
            texte_compresse.append(texte_a_compresser[i])
            i += 1
    affichage_compression.config(text = str(texte_compresse)) #affichage du texte compressé 
    resultat.config(text = "Taille compressée de " + str(taille(texte_compresse)))


def taille(liste_LZ):# calcule la taille de la liste. Un caractère compte 1 et 
                                   # une paire d'entier compte 2
    taille = 0
    for elem in liste_LZ:
        if(len(elem)<2 ):
            taille+=1
        else :
            taille+=2
    return taille

#La fonction de décompression n'est pas intégrée à tkinter attention !!!

def decompresse(textecomp):
    texteoriginal=""
    for i in range(len(textecomp)):
        if isinstance(textecomp[i],str):
            texteoriginal=texteoriginal + textecomp[i]
        else :
            posdepart=i-textecomp[i][0]
            for j in range(posdepart,posdepart+textecomp[i][1]):
                texteoriginal=texteoriginal + texteoriginal[j]
    return(texteoriginal)

    
def chgTaille():
    newtaille=entreet.get()
    global taille_fenetre
    taille_fenetre=int(newtaille)
    taille_fenetr.config(text="Taille de la fenêtre =" + str(newtaille))
    


racine = tk.Tk()
racine.title("Compression de texte")


entree = tk.Entry(racine, width = 50,font = ("helvetica", "20"))
entree.grid(row = 0, column = 0, columnspan=4)



affichage_compression = tk.Message(racine, font = ("helvetica", "20"), width = 1000)
affichage_compression.grid(row = 2, column = 0, columnspan = 3)

bouton_compresser = tk.Button(racine, text = "Compresser", command = compresse, font = ("helvetica", "30"))
bouton_compresser.grid(row = 0, column = 5)

entreet = tk.Entry(racine, width = 50,font = ("helvetica", "20"))
entreet.grid(row = 1, column = 0, columnspan=4)

bouton_chgtaillfen = tk.Button(racine, text = "ChgTaillFenetre", command = chgTaille, font = ("helvetica", "30"))
bouton_chgtaillfen.grid(row = 1, column = 5)

resultat = tk.Label(racine, font = ("helvetica", "20"))
resultat.grid(row = 3, column = 0, columnspan = 2)

taille_fenetr=tk.Label(racine, text="Taille de la fenêtre = 0")
taille_fenetr.grid(row=4, column=0)

racine.mainloop()