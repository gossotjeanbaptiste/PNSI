#-*- coding: utf-8 -*-

def main():
    #création d'un tableau (list en python)
    liste = [1, 2.05, "Toto", -5, 89765.08]
    #affichage de la liste
    print(liste)
    #accès en lecture a un élément
    print(liste[1])
    #accès en écriture à un élément
    liste[3] = "Jean-Jacques Goldmann"
    print(liste)
main()
