from time import sleep
from outilsConsole import inputEntier
from random import randint 

nb = randint(1, 1000)
nb_essai = 0

#print(nb)
trouver = False


while nb_essai < 10 and not trouver:
    jouer = True
    prop = inputEntier()
    if prop < nb:
        print("C'est plus ! ")
    elif prop > nb:
        print("C'est moins ! ")
    else:
        trouver = True
    nb_essai += 1
    if trouver:
        print('Félécitations vous avez gagnez en ' +str(nb_essai)+ ' essais.')
        sleep(5000)
    elif nb_essai >= 10 and not trouver:
        print('Désolé il fallait trouver ' + str(nb) + '.')
        sleep(5000)


'''
def play():
    jouer = True
    while jouer:
        print('Bienvenue au juste prix version python')
        sleep(200)
        print('Vous devez devinez un nombre entre 1 et 1000')
        while nb_essai < 10 and not trouver:
            nb_essai += 1
            print('Essai n°' +str(nb_essai))
            proposition = inputEntier('Quel est votre proposition ? ', "La saisie est invalide veuillez recommencer s'il vous plait")
            if nb > proposition:
                print("C'est plus ! ")
            elif nb < proposition:
                print("C'est moins ! ")
            else: 
                trouver = True
        if trouver:
            print('Bravo vous avez gagnez en ' +str(nb_essai)+ 'essais.')
        else:
            print('Désolé il fallait trouver ' +str(nb)+ '.')
        choix = input("Voulez vous rejouez ? O/N ")
        if choix == "N" or choix == "n" or choix == "non":
            jouer = False
        return 0
'''




#evo cas ou gagne bravo vous gagné en tel essais 
#perdu + nb a trouver
#demande de rejouer
#nv dif demande intervalle + cb essais 