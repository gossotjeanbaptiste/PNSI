# ©JustWirelessInc. 2021-2024
# -*- coding: utf-8 -*-
# Co-created by Jean-Baptiste GOSSOT and Léa GUERIN under the Copyright of JustWirelessInc.

# Importation des frameworks
from flask import Flask, render_template, request, url_for, redirect, session
import os
import csv
import secrets

# Définition du répertoire de travail
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Création de l'application Flask
app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = secrets.token_hex(16)  # Clé secrète pour la session

# Variable de verrouillage initialisée à False
verrou = False

# Lecture des inscrits à partir d'un fichier CSV
with open('inscrits.csv', 'r', encoding='UTF-8') as inscrits_file:
    reader = csv.DictReader(inscrits_file, delimiter=';')
    inscrits = [row for row in reader]

# Page de connexion
@app.route("/")
def logpage():
    return render_template("login.html")

# Authentification de l'utilisateur
@app.post("/auth")
def login():
    global verrou
    global vote
    global indice
    log = request.form["chp_login"]
    password = request.form["chp_mdp"]
    vote = ""
    indice = 0
    for i in range(len(inscrits)):
        if log == inscrits[i]["nom"] and password == inscrits[i]["mdp"]:
            if inscrits[i]["choix"] != "":
                return redirect(url_for('verif'))
            # Si les informations d'identification sont valides, le verrou est défini sur True
            verrou = True
            vote = inscrits[i]["choix"]
            indice = i
            return redirect(url_for('verif'))
    # Si les informations d'identification sont incorrectes, le verrou est défini sur False
    verrou = False
    return redirect(url_for('logpage'))

@app.route("/verif")
def verif():
    global verrou
    global vote
    global indice

    if verrou:
        if vote != "oui" and vote != "non":
            return render_template("vote.html")
        else:
            return redirect(url_for('confirmation'))
    else:
        return redirect(url_for('logpage'))


# Soumission du vote
@app.route("/a_vote", methods=["POST"])
def a_vote():
    global vote
    global indice
    choice = request.form["choix"]
    vote = choice
    inscrits[indice]["choix"] = choice
    with open('inscrits.csv', 'w', newline='', encoding='utf-8') as inscrits_file:
        fieldnames = ['nom', 'mdp', 'choix']
        writer = csv.DictWriter(
            inscrits_file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerows(inscrits)

    # Ajoutez la clé 'voted' à la session pour indiquer que l'utilisateur a voté
    session['voted'] = True

    return redirect(url_for('confirmation'))

# Page de confirmation
@app.route("/confirmation")
def confirmation():
    # Vérifiez si la clé 'voted' est présente dans la session
    if not session.get('voted'):
        return redirect(url_for('logpage'))

    # Supprimez la clé 'voted' de la session pour empêcher l'utilisateur de revenir en arrière et de modifier son vote
    session.pop('voted', None)

    return render_template("confirmation.html", choix=vote)

# Page introuvable
@app.errorhandler(404)
def page_not_found(e):
    # Supprimez la clé 'voted' de la session si elle est présente
    session.pop('voted', None)
    return redirect(url_for('logpage'))

# Désactiver la mise en cache de la page de vérification
@app.after_request
def add_no_cache_header(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response
