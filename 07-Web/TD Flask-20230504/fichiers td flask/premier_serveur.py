from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder="static", template_folder="templates")

autorisation = None


@app.route("/")
def logpage(erreur=False):
    return render_template("login.html", erreur=erreur)


@app.post("/auth")
def login():
    global autorisation
    log = request.form["chp_login"]
    password = request.form["chp_mdp"]
    if log == "olympe" and password == "1234":
        autorisation = log
        return redirect(url_for('page_eleve', eleve=autorisation))
    else:
        return render_template("login.html", erreur=True)


@app.route("/eleves/<eleve>")
def page_eleve(eleve):
    if autorisation == eleve:
        return render_template(f"eleves/{eleve}.html")
    else:
        return f"T'es pas {eleve} !"
