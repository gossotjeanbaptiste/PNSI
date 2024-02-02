def inputEntier(question1 = "Combien d'essai ? ", question2 = "Saisie invalide veuillez recommencez : Combien d'essai ? "):
    nombre = input(question1) #demande un numéro
    while not nombre.isnumeric():
        nombre = input(question2) #si saisie non valide alors répeté la question et récuperer le numéro 
    return print(int(nombre)+ 'essais.')

#code dans l'espace global
print('OutilsConsole v0.0.2')