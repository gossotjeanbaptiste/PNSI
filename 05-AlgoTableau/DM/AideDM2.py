"""
Ce fichier a pour but de vous montrer comment détecter la position
d'un clic de souris et comment afficher du texte à l'écran

Pour la souris, il faut consulter la gestion des évènements:
https://www.pygame.org/docs/ref/event.html

Pour l'affichage de texte, la doc complète est disponible sur:
https://www.pygame.org/docs/ref/font.html

"""

import pygame
from pygame.locals import *

def main():
	continuer = True

	pygame.init()
	fenetre = pygame.display.set_mode([640,480])


	####################################################################
	# Concerne le clic de la souris
	####################################################################

	# Booléen pour que l'affichage reste tant que le bouton de la souris est enfoncé
	# Ce n'est pas indispensable pour votre projet
	clic = False
	# Variable pour contenir les coordonnées du clic
	x = 0
	y = 0



	####################################################################
	# Boucle principale
	####################################################################
	while continuer:
		####################################################################
		# Boucle de gestion des évènements:
		####################################################################
		for evenement in pygame.event.get():
			if evenement.type == QUIT:
				continuer = False
			if evenement.type == MOUSEBUTTONDOWN:
				clic = True
				# récupération des coordonnées du clic
				x = evenement.pos[0]
				y = evenement.pos[1]
			if evenement.type == MOUSEBUTTONUP:
				clic = False

		####################################################################
		# Actualisation de l'affichage
		####################################################################

		fenetre.fill(0xFFFFFF)	# Fond blanc

		if clic: 	# affichage des coordonnées du clic
			# La variable ci-dessous permet de définir la police de caractères utilisée
			police =  pygame.font.SysFont("Arial", 30)	# Ouverture de la police système Arial en taille 30

			# On crée une Surface avec le texte à afficher (le fond est transparent par défaut)
			# Voir :
			# https://www.pygame.org/docs/ref/font.html#pygame.font.Font.render
			texte = "Clic en X = " + str(x) + " et Y = " + str(y)
			imageTexte = police.render(texte, True, 0xFF000000)
			# Pour le code de couleur (ici 0xFF000000 est le rouge), utilisez
			# le sélecteur de couleur de Geany, remplacez le # par 0x
			# et ajoutez 00 à la fin.

			# On peut aussi utiliser pygame.Color en donnant les niveaux
			# de rouge, vert et bleu de 0 à 255
			# exemple pour du rouge:
			# imageTexte = police.render(texte, True, pygame.Color(255, 0, 0))
			# Vert : 	0x00FF0000		ou 		pygame.Color(0, 255, 0)
			# Bleu : 	0x00		ou 		pygame.Color(255, 255, 255)
			# Noir:		0x0000000000FF00		ou 		pygame.Color(0, 0, 255)
			# Jaune : 	0xFFFF0000		ou 		pygame.Color(255, 255, 0)
			# Cyan : 	0x00FFFF00		ou 		pygame.Color(0, 255, 255)
			# Magenta : 0xFF00FF00		ou 		pygame.Color(255, 0, 255)
			# Blanc:	0xFFFFFF00		ou		pygame.Color(0, 0, 0)		ou simplement 0

			# Une fois la Surface avec l'image du texte créée, on la blitte comme
			# n'importe quelle Surface
			# Ici, à la position du clic
			fenetre.blit(imageTexte, (x, y))
			# Et en copie en haut à gauche de l'écran
			fenetre.blit(imageTexte, (0, 0))


		pygame.display.flip()
		pygame.time.wait(40)
	# Sortie de la boucle principale

	pygame.quit() 	# Nécessaire pour fermer proprement pygame
	return 0

if __name__ == '__main__':
	main()
