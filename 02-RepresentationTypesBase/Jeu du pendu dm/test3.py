resultat="pizza"
caché="*****"
solution=""
lettre_propose=input('Quel lettre ? ')
for i in range(len(resultat)):
        a_trouver=caché[i]
        if (ord(a_trouver) == ord("*")) and (ord(resultat[i]) == ord(lettre_propose)):
            solution += lettre_propose
            print(solution)
        else:
            solution += "*"
            lettre_propose=input('Invalide. Quel lettre ?')