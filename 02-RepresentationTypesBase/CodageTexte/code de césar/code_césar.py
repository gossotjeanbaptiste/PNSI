def cesar(texteClaire, cle):
    '''
    fonction de cryptage de césar:
    arguments : 
        texteClair: str contenant le texte en clair, 
        cle: str de longueur 1 contenant la lettre remplacant A
    Renvoi :
        str correspondant au txt crypté
    tout le texte doit etre en majs 
    tous les caractères autres que les majuscules sont inchangés. 
    '''
    texteCrypte=""
    #lecture de texteClaire caractère par caractère
    for i in range(len(texteClaire)):
        caractere = texteClaire[i]
        #cryptage des majs
        valeur = ord(caractere)
        if valeur >= ord("A") and valeur <= ord("Z"):
            valeur += ord(cle) - ord("A")
            #dépassé Z ? 
            if valeur > ord("Z"):
                valeur -= 26
        texteCrypte += chr(valeur)
        print(texteCrypte)
    return texteCrypte

texte = "BONJOURYZ"
crypte= cesar(texte, "Z")
print("Le texte crypté est " + crypte)
