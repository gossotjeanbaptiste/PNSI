import random
import pygame
from pygame import *
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def generate_custom_table(width, height, rate_0=0.5, rate_1=0.5):
    global table
    choix = [0, 1]
    probabilities = [rate_0, rate_1]
    table = [[random.choices(choix, probabilities)[0]
              for _ in range(width)] for _ in range(height)]
    return table


def main():
    global table
################ Initialisation ######################################################

    init()
    fenetre = display.set_mode([640, 480])
    continuer = True		# Variable pour contrôler la boucle principale
    key.set_repeat(100, 40)
    toto_x = 1  # Position initiale de toto en colonne
    toto_y = 1  # Position initiale de toto en ligne

    fond = image.load("Mur.png").convert()
    sol = image.load("Sol.png").convert()
    toto = image.load("Toto.png")
    toto.set_colorkey((255, 0, 255))
    display.set_icon(toto)
    display.set_caption("Toto l'explorateur !")

################ Début boucle principale ##############################################
    while continuer:
        for evenement in event.get():
            if evenement.type == QUIT:
                continuer = False
            if evenement.type == KEYDOWN:  # Détecte une touche enfoncée
                if evenement.key == K_z and toto_y > 0 and table[toto_y - 1][toto_x] != 0:
                    toto_y -= 1
                if evenement.key == K_s and toto_y < len(table) - 1 and table[toto_y + 1][toto_x] != 0:
                    toto_y += 1
                if evenement.key == K_q and toto_x > 0 and table[toto_y][toto_x - 1] != 0:
                    toto_x -= 1
                if evenement.key == K_d and toto_x < len(table[0]) - 1 and table[toto_y][toto_x + 1] != 0:
                    toto_x += 1

        # Limite la position de toto en x entre 0 et 15
        toto_x = min(max(toto_x, 0), 15)
        # Limite la position de toto en y entre 0 et 11
        toto_y = min(max(toto_y, 0), 11)

################ Debut Dessin #########################################################

        for x in range(0, 16):
            for y in range(0, 12):
                if table[y][x] == 0:
                    fenetre.blit(fond, (x * 40, y * 40))
                elif table[y][x] == 1:
                    fenetre.blit(sol, (x * 40, y * 40))
                    if x == toto_x and y == toto_y:
                        fenetre.blit(toto, (x * 40, y * 40))

        display.flip()  # Affichage final
    quit()  # quitte proprement

    return 0


################ Fin de la boucle principale ##########################################
generate_custom_table(16, 12)

if __name__ == '__main__':
    main()
################ Ligne de commentaire référence ######################################################
