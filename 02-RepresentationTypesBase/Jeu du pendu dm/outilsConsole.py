def inputEntier(question1 = "", question2 = ""):
    nombre = input(question1) #demande un numéro
    while not nombre.isnumeric():
        nombre = input(question2) #si saisie non valide alors répeté la question et récuperer le numéro 
    return int(nombre)
inputEntier("Quel nombre ? ", "On a dit un nombre : quel nombre ?? ") #appelle de la fonction

#code dans l'espace global
print('OutilsConsole v0.0.1')