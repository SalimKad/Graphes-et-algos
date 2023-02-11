import numpy as np
# 1- Représentation d'un graphe par une liste de listes : 

#On crée une structure contenant les informations d'un graphe

def graphe_videL() : #créer une liste de listes vide
    return []

def add_sommetL(G, i) :
    b = False
    for s in range (len(sommet)):
        if(sommet[s][0]== i):
            b = True
    if(b == False):
        sommet[len(sommet)-1][0] = i #nom
        sommet[len(sommet)-1][1] = len(sommet)-1 #id
        G.append([])
        

def addL(G, i, j) :
    '''if i not in G :
        add_sommetL(G, i)
    if j not in G :
        add_sommetL(G, j)
    if j not in G[i] :
        G[i].append(j)
    if i not in G[j] :
        G[j].append(i)'''
    if i not in sommet[:,0] :
        add_sommetL(G, i)
    if j not in sommet[:,0] :
        add_sommetL(G, j)

    if j not in G[i] :
        G[i].append(j)
    if i not in G[j] :
        G[j].append(i)
    '''
    if j not in G[sommet[i][1]] :
        G[sommet[i][1]].append(j)
    if i not in G[sommet[j][1]] :
        G[sommet[j][1]].append(sommet[i][1])'''



def suppL(G, i, j) :
    if i in G and j in G :
        if j in G[i] :
            G[i].remove(j)
        if i in G[j] :
            G[j].remove(i)


def est_voisinL(G, i, j):
    if i<len(G) and j <len(G) :
        if j in G[i] and i in G[j] :
            return True
        else :
            return False
    else :
        return False

def loadL(nom):
    G = graphe_videL()
    f = open(nom, "r")
    for line in f :
        line = line.split()
        addL(G, int(line[0]), int(line[1]))
    f.close()
    return G

def saveL(G, nom):
    f = open(nom, "w")
    for i in range(len(G)) :
        f.write(i + " " + str(i) +"\n")
    for i in range(len(G)) :
        for j in G[i] :
            f.write(str(i) + " " + str(j)+"\n")
    f.close()
    

#2 - Représentation d'un graphe par une matrice d'adjacence :

def graphe_videM(): #créer une matrice vide
    return np.zeros((0,0))  

def add_sommetM(G, i) :
    if i > len(G) :
        G = np.zeros((len(G)+1, len(G)+1))
            

def addM(G, i, j) :
    if i > len(G) :
        G = np.zeros((len(G)+1, len(G)+1))
    if j > len(G) :
        G = np.zeros((len(G)+1, len(G)+1))
    G[i][j] = 1
    G[j][i] = 1
 
def suppM(G, i, j) :
    if i < len(G) and j < len(G) :
        G[i][j] = 0
        G[j][i] = 0

def est_voisinM(G, i, j):
    #if i < len(G) and j < len(G) :
        if G[i][j] == 1 and G[j][i] == 1 :
            return True
        else :
            return False
    #else :
     #   return False

def loadM(nom):
    G = graphe_videM()
    f = open(nom, "r")
    for line in f :
        line = line.split()
        addM(G, int(line[0]), int(line[1]))
    f.close()
    return G

def saveM(G, nom):
    f = open(nom, "w")
    for i in range(len(G)) :
        f.write(i + " " + str(i) +"\n")
    for i in range(len(G)) :
        for j in range(len(G)) :
            if G[i][j] == 1 :
                f.write(str(i) + " " + str(j)+"\n")
    f.close()
 
   
def matrice_to_liste(G):
    L = graphe_videL()
    for i in range(len(G)) :
        for j in range(len(G)) :
            if G[i][j] == 1 :
                addL(L, i, j)
    return L

def liste_to_matrice(G):
    M = graphe_videM()
    for i in range(len(G)) :
        for j in G[i] :
            M[i][j] = 1
    return M


# TESTS
grapheL = graphe_videL()
i ={"id" : 0,"nom" : 0}

sommet = np.zeros((1,2))  # tableau de sommets
add_sommetL(grapheL, 0)
add_sommetL(grapheL, 1)
add_sommetL(grapheL, 5) 

#addL(grapheL, 1, 2)
addL(grapheL, 1, 5)
addL(grapheL, 0, 1)
print(grapheL)

print(est_voisinL(grapheL, 0, 2))
print(est_voisinL(grapheL, 1, 0))
print(est_voisinL(grapheL, 2, 1))
print(est_voisinL(grapheL, 1, 1))
'''
suppL(grapheL, 1, 2)
print(grapheL)
print(est_voisinL(grapheL, 1, 2))
saveL(grapheL, "grapheL.txt")

grapheL2 = loadL("grapheL.txt")
print(grapheL2)

grapheLM = liste_to_matrice(grapheL)
print(grapheLM)

'''
grapheM = graphe_videM()