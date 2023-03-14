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


#4 - Graphes aléatoires

import random

def G(n,p):
    '''probabilité p
    n sommets
    chaque paire (x, y) de sommets est connectée de façon indépendante selon la probabilité p'''
    graphe = Graphe()
    
    for i in range(n):
        
        add_sommet(graphe,{"id" : i,"nom" : "sommet "+str(i), "aretes" : []})
    
    n = len(graphe.sommets)
    
    for i in range(n):
        for j in range(n):
            x = random.random()
            #print(x)
            if(x < p):
                graphe.matrice[i][j] = 1
                graphe.matrice[j][i] = 1
        
    return graphe

graphe6 = G(5,0.7)
print(graphe6.sommets)
print(graphe6.matrice)