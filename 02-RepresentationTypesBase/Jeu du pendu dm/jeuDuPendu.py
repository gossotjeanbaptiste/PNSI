# -*- coding: utf-8 -*-
#Copyright JustWireless Inc© with the help of Florence Duchêne and Stack Overflow
#J'ai eu un manque de temps
def main():
    print("Bienvenue au jeu du pendu Version Python 3.11.0 \n Les règles sont simples : \n - 2 joueurs \n - Proposez un mot (Comme Pizza, et non composé d'un espace ou d'une quelconque forme de mot composé.) \n - Proposez un nombre d'essai \n - Le deuxième joueur doit trouver le mot dans le nombre d'essai imposez par le premier joueur. \n Si il le trouve il gagne ! \n\n /!\ ATTENTION \n\n Pas de retour en arrière possible dans le mot ! \n Si plusieurs lettre sont proposés le jeu comptera sa comme une erreur et vous aurez un essai en moins (Oui c'est traitre mais c'est le jeu) \n Vous devez mettre vos saisies en majuscules ! \n BON JEU !")
    #affiche les règles du jeu

def essais(question1="Combien d'essai ? ", question2="Saisie invalide veuillez recommencez : Combien d'essai ? "):
    essai = input(question1)  # demande un entier

    while not essai.isnumeric():
        # si saisie non valide alors répeté la question et récuperer l'entier
        essai = input(question2)

    print(str(essai) + ' essai(s).')
    
    return essai

def majuscule(mot):

    for i in range(len(mot)):

        if ord(mot[i]) >= ord('a') and ord(mot[i]) <= ord('z') or ord(mot[i]) >= ord('A') and ord(mot[i]) <= ord('Z'):   #sert a savoir si c'est uniquement des lettres dans la chaine de caractères
            print("Mot valide")
        else:
            mot = input("Quel mot voulez vous faire devinez ? ") #redemande le mot si il ne remplie pas les conditions plus haut

    resultat = ""

    for i in range(len(mot)):
        caractere = mot[i]

        if (ord(caractere) >= ord("a")) and (ord(caractere) <= ord("z")):  # si on détecte une minuscule
            valeur_lettre = ord(caractere)
            valeur_lettre -= 32  # equivalent en maj
            # transfo valeur de la lettre minuscule en lettre maj
            caractere = chr(valeur_lettre)

        resultat += caractere

    print(resultat)
    return resultat

def mot_cacher(resultat):
    mot_cache=""
    for n in range(len(resultat)):  #fonction mot caché sert a prendre le mot de la variable resultat et de le transformer en chaine de caractères uniquemennt composés d'étoiles selon la taille du mot
        mot_cache +="*"
    return mot_cache

def play(resultat, mot_cache):
    
    '''
        Fonction de jeu du pendu 
        argument: 
            resultat : le mot en clair et en majuscule
            demande : str de 1 caractère proposé par le user(en majuscule si possible). 
        renvoi : 
            une chaine de caractère mise a jour avec une analyse pour savoir si la demande de l'user est dans le mot. 
    '''

    solution = ""
    trouver = False
    lettre_propose=input('Quel lettre ?')
    i = 0

    while i in range(len(resultat)):

        a_trouver=mot_cache[i]

        if (ord(a_trouver) == ord("*")) and (ord(resultat[i]) == ord(lettre_propose)) and trouver == False:

            solution += lettre_propose
            print(solution)
            lettre_propose=input('Quel lettre ? ')

            if solution == resultat:
                trouver = True
            else:
                trouver = False

        else:
            solution += "*"
            lettre_propose=input('Invalide. Quel lettre ? ')
        
        i += 1
    
main()
essai = essais()
print(essai)
mot=input("Quel mot voulez vous faire devinez ? ")
resultat=(majuscule(mot))
mot_cache = mot_cacher(resultat)
print(mot_cache)
play(resultat, mot_cache)
