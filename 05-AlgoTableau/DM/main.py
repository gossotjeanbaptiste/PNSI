# -*- coding: utf-8 -*-   # indique l'encodage utilisé dans le fichier source
# ©JustWirelessInc. 2021-2024   # commentaire sur les droits d'auteur
# Path: table_de_chocolat.png  # chemin relatif de l'image d'icône

import pygame   # import de la bibliothèque Pygame pour créer des jeux vidéo
import os   # module permettant l'interaction avec le système d'exploitation

# se déplacer dans le répertoire où se trouve le fichier source
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    display = pygame.display.set_mode((1280, 800))   # créer une fenêtre Pygame
    # définir le titre de la fenêtre
    pygame.display.set_caption("Table de chocolat")
    # charger l'image du morceau de chocolat
    morceau = pygame.image.load("morceau.png")
    # définir l'icône de la fenêtre
    pygame.display.set_icon(pygame.image.load("table_de_chocolat.png"))
    # définir un tableau pour stocker les coordonnées d'affichage des morceaux de chocolat
    affichage = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]

    play = True   # booléen pour indiquer si le jeu est en cours
    while play:   # boucle principale du jeu
        for evenement in pygame.event.get():   # traiter tous les événements Pygame
            if evenement.type == pygame.QUIT:   # si l'événement est de quitter la fenêtre
                play = False   # changer l'état de play pour arrêter la boucle
            if evenement.type == pygame.MOUSEBUTTONDOWN:   # si l'événement est de cliquer sur la souris
                x, y = evenement.pos   # récupérer les coordonnées du clic
                # remplacer la zone de l'image entre (1280, 800) et (x, y)
                for i in range(5):
                    for j in range(8):
                        if j * 160 > x or i * 160 > y:   # si on est sorti de la zone à remplacer, arrêter la boucle
                            continue
                        # mettre la valeur 1 dans le tableau à la position (i, j)
                        affichage[i][j] = 1

        for i in range(len(affichage)):
            for j in range(len(affichage[i])):
                if affichage[i][j] == 0:
                    display.blit(morceau, (j * 160, i * 160))
                else:
                    pygame.draw.rect(display, (0, 0, 0), pygame.Rect(
                        j * 160, i * 160, 160, 160))
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
