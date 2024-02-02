#!/usr/bin/python3
# -*- coding: utf8 -*-
#
#  affichage.py
#  

"""
Auteurs: Gilles BECKER & Rachid CHOUCHI

Ce module regroupe tout ce qui concerne l'affichage.
"""

########################################################################
#	imports
########################################################################
import tkinter
import os
from enum import Enum


########################################################################
#	fonctions
########################################################################

	####################################################################
	#	Affichage de menu
	####################################################################
def texte_menu(menu, titre = "", invite_utilisateur = ""):
	"""
	Construit le texte d'un menu sous la forme:
	Titre
	1) Item 1
	2) Item 2
	...
	0) Quitter
	Invite utilisateur
	Auteurs: Gilles BECKER & Rachid CHOUCHI
	Arguments:
		menu: liste de str correspondants aux items du menu
		titre: le titre à afficher en tête du menu
		invite_utilisateur: str de l'invite utilisateur
	Renvoi:
		str du texte à afficher
	"""
	texte = titre + "\n"
	for i in range(len(menu)):
		texte += str(i + 1) + ") " + menu[i] +"\n"
	texte += "0) Quitter\n"
	texte += invite_utilisateur
	return texte


def affiche_menu(menu, titre = "", invite_utilisateur = ""):
	"""
	Efface la console et y affiche un menu à partir de texte_menu
	suivi d'une invite à l'utilisateur (input).
	Boucle tant que la saisie est incorrecte.
	Auteurs: Gilles BECKER & Rachid CHOUCHI
	Arguments:
		menu: liste de str correspondants aux items du menu
		titre: le titre à afficher en tête du menu
		invite_utilisateur: str de l'invite utilisateur
	Renvoi:
		int de l'item sélectionné par l'utilisateur
	"""
	texte = texte_menu(menu, titre, invite_utilisateur)
	# On traite le choix de l'utilisateur
	choix = 0
	continuer = True
	while continuer:
		os.system("cls")
		print(texte)
		try:
			choix = int(input())
			if choix > len(menu) or choix < 0:
				raise(ValueError())
			else:
				continuer = False
		except ValueError:
			input("Entrée incorrecte. Appuyez sur ENTREE pour continuer.")
	return choix


	####################################################################
	#	Affichage de table
	####################################################################
def trace_ligne_separation(taille_colonnes):
	"""
	Construit les lignes de séparation du tableau
	Auteurs: Gilles BECKER & Rachid CHOUCHI
	Arguments:
		taille_colonnes: la liste de la largeur de chaque colonne
			Attention: il s'agit de la taille maximale de chaque colonne 
			sans l'espace final
	Renvoi:
		Une chaine de caractères au format: +-----+----+--------+
	"""
	#""" Variante 1 (décommenter la ligne pour activer Variante 2)
	carateres = ["+","-","|"]
	ligne=""
	for i in taille_colonnes:
		ligne += carateres[0] + (i+1) * carateres[1]
	ligne += carateres[0]
	return ligne

	"""
	# Variante 2
	# Cette variante utilise deux boucles for imbriquées (peut-être plus formateur pour les élèves)
	# Elle est peut-être plus facilement transposable dans d'autres langages.
	texte = "+"
	for taille in taille_colonnes:
		for i in range(taille+1):	# Le +1 correspond à l'espace ajouté après l'entrée de table
			texte += "-"
		texte += "+"
	return texte
	# Fin variante 2"""


def convert_str(entree):
	"""
	Converti une entrée de la table en str.
	Cette fonction est nécessaire car le cast en str ne donne
	pas un résultat satisfaisant pour les type énumérés
	Auteurs: Gilles BECKER & Rachid CHOUCHI
	Arguments:
		entree : une entrée de la table
	Renvoi:
		une chaine de caractères pour afficher l'entrée
	"""
	texte = ""
	if isinstance(entree, Enum):
		texte = entree.name.replace("_", " ")
	elif entree == None:
		texte = "NULL"
	else:
		texte = str(entree)
	return texte


def format_entree(entree, taille):
	"""
	Génère le texte d'une entrée de la table en le formattant correctement
	Auteurs: Gilles BECKER & Rachid CHOUCHI
	Arguments:
		entree : une entrée de la table
		taille : taille de la colonne (plus grande chaine de caractères)
	Renvoi:
		une chaine de caractères plus assez d'espaces pour respecter la largeur de la colonne
	"""
	texte = convert_str(entree)
	if len(texte) < taille :	# Vérification théoriquement inutile
		texte += " "*(taille-len(texte))
	return texte


def trouve_taille_colonnes(table, debut, fin):
	"""
	Détermine la taille des colonnes pour la création du texte à afficher
	en cherchant pour chacune d'elle le nombre de caractère maximum à afficher
	Cette recherche ne s'effectue que sur les lignes que l'on cherche à afficher
	Auteurs: Gilles BECKER & Rachid CHOUCHI
	Arguments:
		table : la table
		debut : indice de début de la partie à afficher
		fin   : indice de fin
	Renvoi:
		une liste des tailles de chaque colonne
	"""
	# On initialise la liste des tailles à 0
	taille_colonnes = [0] * len(table[0])
	""" chercher la taille maximale des chaînes de caractères suivant chaque colonne
		on stocke dans un tableau une liste  """
	# Puis, pour chaque ligne entre debut et fin (la ligne fin étant comprise, il faut aller jusque fin + 1)
	for i in range(debut, fin + 1):
		# Puis, pour chaque colonne
		for j in range(len(taille_colonnes)):
			# On cherche la largeur de l'entrée scannée
			largeur_entree = len(convert_str(table[i][j]))
			if taille_colonnes[j] < largeur_entree:
				taille_colonnes[j] = largeur_entree
	return taille_colonnes # taille maximale de chaque champ de la table


def texte_table(table, debut = 0, fin = None):
	"""
	Crée le texte à afficher lors d'un affichage de la table.
	Auteurs: Gilles BECKER & Rachid CHOUCHI
	Arguments:
		table   : une liste de tuples
		debut   : indice de la première ligne que l'on veut afficher
		fin     : indice de la dernière ligne que l'on veut afficher
			si fin est à None, on affiche jusqu'à la dernière ligne
	Renvoi:
		la chaîne de caractères à afficher
	"""
	# On corrige si fin vaut None ou va au-delà de la taille de la table
	if fin == None or fin > (len(table) - 1):
		fin = len(table) - 1 # On considère que fin est le numéro de la dernière ligne à afficher
	# Par sécurité, on vérifie que fin n'est pas avant debut
	if debut > fin:
		# Si c'est le cas, on échange
		debut, fin = fin, debut
	# On cherche la taille des colonnes à afficher
	taille_colonnes = trouve_taille_colonnes(table, debut, fin)
	# On commence par une ligne de séparation
	ligne_separation = trace_ligne_separation(taille_colonnes)
	texte = ligne_separation + "\n"
	# Puis, pour chaque ligne dans l'intervalle voulu
	for i in range(debut, fin + 1):
		# On commence la ligne par un |
		ligne = "|"
		# et on ajoute chaque entree de la table en texte formaté, avec un " |" à la fin
		for j in range(len(taille_colonnes)):
			ligne += format_entree(table[i][j], taille_colonnes[j]) + " |"
		texte += ligne + "\n" + ligne_separation + "\n"
	return texte


def afficher_table(table, titre ="", debut = 0, fin = None):
	"""
	Affiche une table.
	Cette fonction était demandée dans le sujet.
	On peut avoir un affichage en console ou dans une fenêtre tkinter
	Auteurs: Gilles BECKER & Rachid CHOUCHI
	Arguments:
		table: une liste de tuples
		titre: str du titre à afficher avant la table
		debut: indice de la première ligne que l'on veut afficher
		fin: indice de la dernière ligne que l'on veut afficher
			si fin est à None, on affiche jusqu'à la dernière ligne
	Renvoi:
		rien
	"""
	if titre != "":
		titre += "\n\n"
	#print(titre + texte_table(table, debut, fin))
	affichage(titre + texte_table(table, debut, fin), titre)


def affichage(texte, titre = "Requêtes tables"):
	"""
	Affiche un texte (résultat d'une requête)
	dans une fenêtre tkinter
	Auteurs: Gilles BECKER & Rachid CHOUCHI
	Arguments:
		texte: str du texte à afficher
		titre: str du titre de la fenêtre
	Renvoi:
		rien
	"""
	root = tkinter.Tk()
	root.title(str(titre))
	RWidth=root.winfo_screenwidth() - 100
	RHeight=root.winfo_screenheight() - 100
	root.geometry("%dx%d+50+0"%(RWidth, RHeight))
	text=tkinter.Text(root, wrap = 'none')
	scroll_x=tkinter.Scrollbar(text.master, orient='horizontal', command = text.xview)
	scroll_x.config(command = text.xview)
	text.configure(xscrollcommand = scroll_x.set)
	scroll_x.pack(side = 'bottom', fill = 'x', anchor = 'w')
	scroll_y = tkinter.Scrollbar(text.master)
	scroll_y.config(command = text.yview)
	text.configure(yscrollcommand = scroll_y.set)
	scroll_y.pack(side = tkinter.RIGHT, fill = 'y')
	text.insert("1.0", texte)
	text.pack(side = tkinter.LEFT, expand = True, fill = tkinter.BOTH)
	root.mainloop()


########################################################################
#	Redirection vers main de main.py
########################################################################

if __name__ == '__main__':
	from main import main
	main()
