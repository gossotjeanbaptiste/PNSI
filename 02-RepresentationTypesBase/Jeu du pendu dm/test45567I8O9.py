motATrouver= input('Mot ? ')
for i in range(len(motATrouver)):
    caractere = motATrouver[i]
    valeur = ord(caractere)
while (valeur >= ord("A")) and  (valeur =< ord('Z')) and (valeur >= ord("a")) and (valeur <= ord("z")):
    print('bon')
else:
    mot_a_trouver = input(' Saisie non valide veuilez recommencer. ')
    caractere = mot_a_trouver[i]
print('sortie de boucle')