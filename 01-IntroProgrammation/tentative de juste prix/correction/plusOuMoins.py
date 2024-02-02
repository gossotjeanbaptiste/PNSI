"""
Exemple de correction pour le jeu du plus ou moins

"""
from outilsConsole import inputEntier
from random import randint

def main():
	jouer = True
	while jouer:
		# Début de partie : initialisation
		nb_essais = 0
		tirage = randint(1, 1000)
		trouve = False
		print("Bienvenue au jeu du plus ou moins.")
		print("Essayez de deviner un nombre entre 1 et 1000")
		#boucle de jeu
		while nb_essais < 10 and not trouve:
			nb_essais += 1
			print ("Essai n°" + str(nb_essais))
			proposition = inputEntier("Quel nombre proposez-vous ? ", "Saisie incorrecte, veuillez recommencer : ")
			if tirage > proposition:
				print("C'est plus.")
			elif tirage < proposition:
				print("C'est moins.")
			else:
				trouve = True
			#fin de partie
		if trouve:
			print("Bravo, vous avez gagne en " + str(nb_essais) + " essais.")
		else:
			print("Desole, vous avez perdu. Il fallait trouver " + str(tirage))
		#demande de nv partie
		choix = input("Voulez-vous refaire une partie (O/N) ? ")
		if choix == "N" or choix == "n":
			jouer = False
	return 0
