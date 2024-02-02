import pygame
from pygame.locals import *

def main():
	x = 50
	y = 70 
	pygame.init()
	fenetre = pygame.display.set_mode([640,480])
	continuer = True		# Variable pour contrôler la boucle principale
	pygame.key.set_repeat(100,40)

	fond = pygame.image.load("Ressources/background.jpg").convert()
	sprite = pygame.image.load("Ressources/perso.png").convert_alpha()
    
	while continuer:		# Entrée dans la boucle principale
		# Boucle de gestion des évènements:
		for evenement in pygame.event.get():
			if evenement.type == QUIT:			# On a cliqué sur la croix pour fermer la fenêtre
				continuer = False				# on va donc sortir de la boucle principale
				if evenement.type == KEYDOWN:
					if evenement.key == K_LEFT or evenement.key == K_q or evenement.key == K_a:
						x -= 10
					if evenement.key == K_RIGHT or evenement.key == K_d:
						x += 10
					if evenement.key == K_DOWN or evenement.key == K_s:
						y += 5
					if evenement.key == K_UP or evenement.key == K_z or evenement.key == K_w:
						y -= 5
					


		
		# Mise à jour de l'état des données du programme (le modèle du programme)
		
		# Mise à jour de l'affichage (les vues du programme)
		fenetre.blit(fond, (0, 0))     # fenetre est la destination et fond est la source
		fenetre.blit(sprite, (x, y))
		pygame.display.flip()
	
	# Sortie de la boucle principale
	pygame.quit() 	# Nécessaire pour fermer proprement pygame
	return 0

if __name__ == '__main__':
	main()