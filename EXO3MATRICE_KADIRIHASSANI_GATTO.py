#KADIRI HASSANI Salim - GATTO Elisa
import numpy as np
import copy

# FONCTIONS DE L'EXERCICE 1 DONT ON A BESOIN

class Graphe: 
    def __init__(self):
        self.sommets = []
        self.matrice = np.array([])
        self.GraphenomM = []

def graphe_vide(self):
    self.sommets = []
    self.matrice = np.array([])
    
def add_sommet(self, i):
    if i["id"] not in self.sommets:
        self.GraphenomM.append(i["nom"])
        self.sommets.append(i["id"])
        n = len(self.sommets)
        self.matrice = np.zeros((n, n))


def add(self, i, j):
    if i["id"] in self.sommets and j["id"] in self.sommets:
        i_index = self.sommets.index(i["id"])
        j_index = self.sommets.index(j["id"])
        self.matrice[i_index][j_index] = 1
        self.matrice[j_index][i_index] = 1


A ={"id" : 0,"nom" : "A", "aretes" : []}
B ={"id" : 1,"nom" : "B", "aretes" : []}
C ={"id" : 2,"nom" : "C", "aretes" : []}
D ={"id" : 3,"nom" : "D", "aretes" : []}


graphe = Graphe()
add_sommet(graphe, A)
add_sommet(graphe, B)
add_sommet(graphe, C)
add_sommet(graphe, D)

add(graphe, A, B)
add(graphe, C, D)
add(graphe, B, C)
add(graphe, D, A)
add(graphe, A, C)
#print(graphe.sommets)
#print(graphe.matrice)

graphe2 = Graphe()
add_sommet(graphe2, A)
add_sommet(graphe2, B)
add_sommet(graphe2, C)
add_sommet(graphe2, D)

add(graphe2, A, B)
add(graphe2, C, D)
add(graphe2, B, C)
add(graphe2, D, A)
add(graphe2, A, C)

graphe3 = Graphe()
add_sommet(graphe3, A)
add_sommet(graphe3, B)
add_sommet(graphe3, C)
add(graphe3, A, B)
add(graphe3, B, C)
add(graphe3, A, C)

E ={"id" : 4,"nom" : "E", "aretes" : []}
graphe4 = Graphe()
add_sommet(graphe4, A)
add_sommet(graphe4, B)
add_sommet(graphe4, E)
add(graphe4, A, B)
add(graphe4, B, E)

graphe5 = Graphe()
add_sommet(graphe5, A)
add_sommet(graphe5, B)
add_sommet(graphe5, C)
add(graphe5, A, B)
add(graphe5, B, C)



#3 - Rayon, diamètre et centre :

def calcul_distances(G):
    #calcule les plus courtes distances (en nombre d’arêtes) entre tout couple de sommets du graphe G.
    n = len(G.sommets)
    dist = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if G.matrice[i][j] != 0:
                dist[i][j] = 1
            else:
                dist[i][j] = 1000000
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j:
                    dist[i][j] = 0
                else:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

'''
print("distances de graphe : ")
print(calcul_distances(graphe))
print("distances de graphe5 : ")
print(calcul_distances(graphe5))
'''

def donne_diametre(G):
    #distance maximale entre deux sommets
    dist = calcul_distances(G)
    n = len(G.sommets)
    diametre = 0
    for i in range(n):
        for j in range(n):
            diametre = max(diametre, dist[i][j])
    return diametre

#print("\ndiametre graphe :")
#print(donne_diametre(graphe))

def excentricite(G, s):
    #distance maximale entre un sommet s et les autres sommets du graphe
    dist = calcul_distances(G)
    n = len(G.sommets)
    excent = 0
    for i in range(n):
        excent = max(excent, dist[s][i])
    return excent

#print("\nexcentricites de graphe :")
excentricites = np.zeros(len(graphe.sommets))
for i in range(len(graphe.sommets)):
    excentricites[i] = excentricite(graphe,i)
#print(excentricites)

def donne_centres(G):
    dist = calcul_distances(G)
    n = len(G.sommets)
    centre = []
    excentricites = np.zeros(n)
    dmin = 1000000
    
    for i in range(n):
        excentricites[i] = excentricite(G, i)
        
    for i in range(n):
        if excentricites[i] < dmin:
            dmin = excentricites[i]
            
    for i in range(n):
        if excentricites[i] == dmin:
            centre.append(G.sommets[i])
    rayon = excentricite(G,centre[0])
    
    return (len(centre),centre,rayon)

#print("\ndonne_centre de graphe :")
#print(donne_centres(graphe))

def calcul_degres(G):
    n = len(G.sommets)
    degres = np.zeros(n, dtype=int)
    
    for i in range(n):
        for j in range(n):
            if G.matrice[i][j] == 1:
                degres[i] += 1
    
    return degres

#print("\ndegrés de graphe :")
#print(calcul_degres(graphe))

def donne_centres_degre(G):
    n = len(G.sommets)
    degres = calcul_degres(G)
    degre_max = 0
    centre = []
            
    for i in range(len(degres)):
        if degres[i] > degre_max : 
            degre_max = degres[i]
    
    for i in range(n):
        if degres[i] == degre_max:
            centre.append(G.sommets[i])
    print(centre)
                
    return (len(centre),centre,degre_max)

#print("\ncentres en fonction du degré max : ")
#print(donne_centres_degre(graphe))

