def recherche(tableau, valeur):
    position = -1
    i = 0

    while i < len(tableau) and position == -1:
        if tableau[i] == valeur:
            position = i
        else:
            i += 1
    else:
        return position
    
print(recherche(([2, 4 ,5 ,2 ,6, 5]), 2))
print(recherche(([2, 4 ,5 ,2 ,6, 5]), 5))
print(recherche(([2, 4 ,5 ,2 ,6, 5]), 7))
print(recherche(([2, 4 ,5 ,2 ,6, 5]), 4))
print(recherche(([2, 4 ,5 ,2 ,6, 5]), 6))
print(recherche(([2, 4 ,5 ,2 ,6, 5]), 1))


