def inputEntier(question1 = "Quelle est votre proposition ? ", question2 = "Quelle est votre proposition ? "):
    question2 = question1
    nombre = input(question1) #demande un numéro
    while not nombre.isnumeric():
        nombre = input(question2) #si saisie non valide alors répeté la question et récuperer le numéro 
    return int(nombre)

#code dans l'espace global
print('OutilsConsole v0.0.1')