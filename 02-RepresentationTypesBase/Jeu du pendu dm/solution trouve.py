def trouve(texte, caractere):
    """
    fonction pour trouver la position d'un caractère dans un texte.
    arguments : 
        texte (str) : texte dans lequel on cherche
        caractère (str) : le caractère chercher (attention len(caractère) doit valoir 1, pas de verif effectué)
    renvoi : 
        int de la position de la première apparition de caractère dans le texte renvoi -1 si caractère non trouver.
    """
    resultat =  -1
    i = 0 #pos caractère lu dans texte
    trouve = False #indique si trouver ou pas 
    while i < len(texte) and not trouve:
        if texte[i] == caractere:
            trouve = True
        else:
            i += 1
    if trouve:
        resultat = i 
    return resultat 
def main():
    res=trouve("Bonjour", "j")
    print(res)
    res=trouve("Bonjour", "h")
    print(res)

main()