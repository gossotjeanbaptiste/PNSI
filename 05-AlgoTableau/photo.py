from itertools import combinations

def gain(photos):
    resultat = 0
    '''for i in range(len(photos)):
        resultat += photos[i][1]
    print(resultat)'''
    for e in photos:
        resultat += e[1]
    return resultat

def poids(data):
    resultat = 0
    for e in data:
        resultat += e[0]
    return resultat

photos = [(4.5, 8, 'chat'), (7.5, 6, 'paysage'), (2.5, 7, 'sport'),
          (10, 5, 'manif'), (8, 12, 'ville'), (12, 10, 'astronomie'), 
          (1.5, 5, 'chien')]

def brute_force(data):
    resultat=[]
    for i in range(1,len(data)+1):
        combinaisons = combinations(data,i)
        for c in combinaisons :
            if poids(c)<=15:
                resultat.append(c)
    maxi = 0
    solution = None
    for s in resultat:
        if maxi < gain(s):
            maxi = gain(s)
            solution = s
    return solution

def glouton(data):
    resultat = []
    reste = 15
    encore = True
    while encore:
        maxi = 0
        meilleur = None
        for e in data:
            if e[0] <= reste and e not in resultat and e[1] > maxi:
                meilleur = e 
                maxi = e[1]
        if meilleur != None:
            reste -= meilleur[0]
            meilleur.append(resultat)
        else:
            encore = False
    return resultat

if __name__ == '__glouton__':
    glouton(photos)
    
'''if __name__ == '__gain__':
    gain(photos)

if __name__ == '__poids__':
    poids(photos)'''
