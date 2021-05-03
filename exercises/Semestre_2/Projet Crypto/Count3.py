Text = "dceuq e n'ehfp cg p'kyhhep uqfw cgiy citudm c gzudiq ni ezhd px c jhptv ep cggsht. kg hdtymdt xdzei gdx rzyq wir mvzxpw, cifcchdb znwd ccyw wy lkcsht, dp isgd uqfw wy ?"
TextDec = "dceuq e n'ehfp cg p'kyhhep uqfw cgiy citudm c gzudiq ni ezhd px c jhptv ep cggsht. kg hdtymdt xdzei gdx rzyq wir mvzxpw, cifcchdb znwd ccyw wy lkcsht, dp isgd uqfw wy ?"
Alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#Lettres qui apparaisse le plus
AlphaB = ["e", "a", "i", "s", "n", "r", "t", "o", "l", "u", "d", "c", "m", "p", "e", "g", "b", "v", "h", "f", "q", "y", "x", "j", "e", "a", "k", "w", "z"]

def emplacementlettre(Text, Alpha):
    """Donne l'emplacement de chaque lettre du texte"""
    for i in Text:
        if i in Alpha:
            print(i, " = ", Alpha.index(i))


#emplacementlettre(Text, Alpha)


def decalagelettre(Text, Alpha, Num, Decale):
    """Decale une lettre du texte par raport a son emplacement dans l'alphabet"""
    if Text[Num] not in Alpha:
        print(Text[Num], end="")
    res = Alpha.index(Text[Num])
    res = (res + Decale)%26
    print(Alpha[res], end="")

Code = ["b", "l", "e", "y", "x", "a", "a"]
for i in Code:
    Codei.appened(Alpha.index(i))
