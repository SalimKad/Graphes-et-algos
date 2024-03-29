import numpy as np
# 1- Représentation d'un graphe par une liste de listes : 

#On crée une structure contenant les informations d'un graphe

def graphe_videL() : #créer une liste vide
    return []

def add_sommetL(G, i) :
    #print(i)
    if i >= len(G) : #si le sommet n'existe pas, on l'ajoute à la liste de listes
        G.append([])
        

def addL(G, i, j) :
    if i >= len(G) : #si le sommet n'existe pas, on l'ajoute à la liste de listes
        add_sommetL(G, i)
    if j >= len(G) :
        add_sommetL(G, j)
    if j not in G[i] :
        G[i].append(j)
    if i not in G[j] :
        G[j].append(i)


def suppL(G, i, j) :
    a:int = i
    b:int = j
    #if a in G and b in G :
    if b in G[a] :
        G[a].remove(b)
    if a in G[b] :
        G[b].remove(a)


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
        line = line.strip().split()
        i = int(line[0])
        j = int(line[1])
        addL(G, {"id": i}, {"id": j})
    f.close()
    return G


def saveL(G, nom):
    f = open(nom, "w")
    n = len(G)
    f.write(str(n) + "\n")
    for i in range(len(G)):
        for j in G[i]:
            f.write(str(i) + " " + str(j) + "\n")

    for i in range(len(G)):
        for j in G[i]:
            f.write(str(i) + " " + str(j) + "\n")
    f.close()



#2 - Représentation d'un graphe par une matrice d'adjacence :

def graphe_videM(): #créer une matrice vide
    return np.zeros((0,0))  

def add_sommetM(G, i) :
    a:int = i
    if a > len(G) :
        G = np.zeros((len(G)+1, len(G)+1))
            

def addM(G, i, j) :
    a:int = i
    b:int = j
    if a > len(G) :
        G = np.zeros((len(G)+1, len(G)+1))
    if b > len(G) :
        G = np.zeros((len(G)+1, len(G)+1))
    G[a][b] = 1
    G[a][b] = 1
 
def suppM(G, i, j) :
    a:int = i
    b:int = j
    if a < len(G) and b < len(G) :
        G[a][b] = 0
        G[a][b] = 0

def est_voisinM(G, i, j):
    a:int = i
    b:int = j
    if i < len(G) and j < len(G) :
        if G[a][b] == 1 and G[a][b] == 1 :
            return True
        else :
            return False
    else :
        return False

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
A ={"id" : 0,"nom" : 0}
B ={"id" : 1,"nom" : 3}
C ={"id" : 2,"nom" : 5}

'''#tableau qui contient les sommets
sommets = [A, B, C]'''


add_sommetL(grapheL, A)
add_sommetL(grapheL, B)
add_sommetL(grapheL, C) 

addL(grapheL, A, B)
addL(grapheL, C, A)
addL(grapheL, C, B)
print(grapheL)

print(est_voisinL(grapheL, 0, 2))
print(est_voisinL(grapheL, 1, 0))
print(est_voisinL(grapheL, 2, 1))
print(est_voisinL(grapheL, 1, 1))

suppL(grapheL, A, C)
print(grapheL)

print(est_voisinL(grapheL, 0, 2))
saveL(grapheL, "grapheL.txt")

grapheL2 = loadL("grapheL.txt")
print(grapheL2)

grapheLM = liste_to_matrice(grapheL)
print(grapheLM)


grapheM = graphe_videM()