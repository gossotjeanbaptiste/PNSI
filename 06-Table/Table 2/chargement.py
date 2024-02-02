#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from collections import namedtuple
from affichage import *


def chargePays(cheminFichier):
	"""
	Fonction pour charger la table "pays.csv".
	
	Argument:
		- cheminFichier: str du chemin du fichier à charger
		
	Renvoi:
		Les données chargées sous forme d'une list de namedtuple.

	Le choix du namedtuple permet un accès aux données d'une ligne
	de la table à partir du numéro de colonne ou du nom du champ
	correspondant à cette colonne.
	
	Le fichier doit être cohérent avec la table attendue
	"""
	# Ouverture du fichier en lecture:
	fichier = open(cheminFichier, "r", encoding = "UTF-8")	# L'argument encoding permet d'utiliser le bon charset lors du chargement du fichier. Les versions récentes de python devraient utiliser UTF-8 par défaut, mais cette précaution assure le compatibilité lors de l'ouverture.
	# Création du namedtuple Pays:
	Pays = namedtuple("Pays", [	"Code", "Nom", "Continent", "Region",  "Aire", "AnneeIndependance", 
	"Population", "EsperanceVie", "PIB", "PIBAncien", "NomLocal", "FormeGouvernement", "ChefEtat", "Capitale", "Code2"])
	# List pour accueillir les données de la table
	table = []
	
	
	for ligne in fichier:
		# Il faut penser à enlever le retour à la ligne en fin de ligne
		ligne = ligne.rstrip("\n")
		# On crée la liste des éléments en coupant au séparateur ";"
		cellules = ligne.split(";")
		# Il faut convertir les cellules dans le type voulu
		# Pour le faire de manière automatique, on utilise un tuple des types attendus.
		types = (str, str, str, str, float, int, int, float, float, float, str, str, str, int, str)
		for i in range(len(cellules)):
			if cellules[i] == "NULL":	# Précaution pour gérer les NULL
				cellules[i] = None
			else:
				cellules[i] = types[i](cellules[i])  # Equivalent à str(cellules[i]), int(cellules[i]), float(cellules[i]),... selon le type rencontré dans types
		# Ajout d'un nouveau namedtuple dans la table:
		table.append(Pays(*cellules))	# Le * unpack la list en ses composants.
	
	fichier.close()
	return table



def main(args):
	pays = chargePays("pays.csv")
	# affichage de la table complète
	afficher_table(pays, "Table complète")
	
	# affichage des pays d'Europe (version compatible avec l'utilisation d'un tuple ou d'une list pour chaque ligne de la table)
	europe = []
	mini = (pays[1].PIB - pays[1].PIBAncien) / pays[1].PIBAncien * 100
	nom = pays[1].Nom
	for p in pays:
		if p.PIB and p.PIBAncien and (p.PIB - p.PIBAncien) / p.PIB * 100 < mini:
			mini = (p.PIB - p.PIBAncien) / p.PIB * 100
			nom = p.Nom
		# ~ if p[2] == "Europe":
			# ~ europe.append(p)
	# ~ afficher_table(europe, "Les pays d'Europe")
	print(mini)
	print(nom)
	afficher_table(pays, "Table complète")
	
	# Autre version: construction à l'aide d'un tableau par compréhension et en utilisant les noms de champs du namedtuple
	europeV2 = [ p for p in pays if p.FormeGouvernement == "Republic" and p.AnneeIndependance and p.AnneeIndependance > 1945 ] # if p.Continent == "Europe" ]
	afficher_table(europeV2, "Les pays d'Europe (2ème version)")
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
