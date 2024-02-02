"""
Ce module regroupe des fonctions utiles 
pour travailler en console.
"""

def inputEntier(question1, question2 = ""):
	"""
	Cette fonction permet de demander une saisie sécurisée
	Arguments:
		question1: str utilisée par le input initial
		question2: str utilisée si la saisie doit être répétée
			si question2 vaut "" alors question1 sera utilisée
			à la place
	Renvoi:
		int correspondant à la saisie de l'utilisateur
	"""
	if question2 == "":
		question2 = question1
	saisie = input(question1)
	while not saisie.isnumeric():
		saisie = input(question2)
	return int(saisie)

# Code dans l'espace global
print("Module outilsConsole actif.")
print("Version 0.1")
