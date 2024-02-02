def inversionElement(tableau):
    '''
    Argument : 
            Un tableau qui est supposé trié dans l'ordre croissant
    Renvoie : 
            le tableau trié dans l'ordre décroissant
    '''
    tableauFinal = []
    
    for i in range(0, len(tableau), -1):
        tableauFinal.append(tableau[i])
    return tableauFinal
tab = [1, 2, 3] 
inversionElement(tab)

