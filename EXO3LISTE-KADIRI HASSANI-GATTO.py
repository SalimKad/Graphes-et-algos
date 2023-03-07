#KADIRI HASSANI Salim - GATTO Elisa
import numpy as np
import copy

# 1- Représentation d'un graphe par une liste de listes : 

#On crée une structure contenant les informations d'un graphe

def graphe_videL() : #créer une liste vide
    return []

def add_sommetL(G, i) : #ajoute un sommet à la liste de listes
    temp = [] 
    # temp va contenir les id déjà présentes dans G
    for j in range(len(G)) :
      temp.append(G[j]["id"])

    #si G est vide, on ajoute le sommet à la liste de listes
    if len(G) == 0 :
        j = copy.deepcopy(i)
        G.append(j)
    #sinon, on vérifie que le sommet n'existe pas déjà
    elif i["id"] not in temp : #si le sommet n'existe pas, on l'ajoute à la liste de listes
        j = copy.deepcopy(i)
        #j["id"] = len(G) 
        G.append(j)
        
        

def addL(G, i, j) : #ajoute une arête entre i et j
    temp = []
    for k in range(len(G)) :
        temp.append(G[k]["id"])

    if i["id"] not in temp : #si le sommet n'existe pas, on l'ajoute à la liste de listes
        add_sommetL(G, i)
    if j["id"] not in temp :
        add_sommetL(G, j)
    if j["id"] not in G[i["id"]]["aretes"] :
        '''print(G[i["id"]])
        print(G[0][0]["aretes"])
        print(i)
        print(G[i["id"]]["aretes"])'''
        G[i["id"]]["aretes"].append(j["id"])
    #print("i id = ", i["id"])
    #print(G[j["id"]])
    #problem : j["id"] = 7 et  G[7] n'existe pas
    if i["id"] not in G[j["id"]]["aretes"] :
        G[j["id"]]["aretes"].append(i["id"])


def suppL(G, i, j) : #supprime l'arête entre i et j
    a:int = i["id"]
    b:int = j["id"]
    #if a in G and b in G :
    if b in G[a]["aretes"] :
        G[a]["aretes"].remove(b)
    if a in G[b]["aretes"] :
        G[b]["aretes"].remove(a)

def est_voisinL(G, i, j): #vérifie si i et j sont reliés par une arête
    a:int = i["id"]
    b:int = j["id"]
    if a<len(G) and b <len(G) :
        if b in  G[a]["aretes"] and a in G[b]["aretes"] :
            return True
    return False


#Graphe connexe : tout sommet peut être relié à tout autre sommet par une arête ou une suite d'arêtes

def calcul_distances(G) :
    #calcule les plus courtes distances (en nombre d’arêtes) entre tout couple de sommets du graphe G
    #on utilise l'algorithme de Floyd-Warshall
    #on crée une matrice de distances

    #on crée une matrice de distances
    n = len(G)
    D = np.zeros((n,n), dtype=int)
    for i in range(n) :

        for j in range(n) :
            if i != j :
                if est_voisinL(G, G[i], G[j]) :
                    D[i][j] = 1
                else :
                    D[i][j] = 999999
            else :
                D[i][j] = 0
                
    #on calcule les plus courtes distances
    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                if D[i][k] + D[k][j] < D[i][j] :
                    D[i][j] = D[i][k] + D[k][j]
    return D


def donne_diametre(G, D):
    #qui renvoie le diamètre du graphe G à partir de la structure de données 
    #D (au choix) contenant les plus courtes distances entre tout couple de sommets de G
    n = len(G)
    diametre = 0
    for i in range(n) :
        for j in range(n) :
            if D[i][j] > diametre :
                diametre = D[i][j]
    return diametre


def donne_centres(G, D):
    #retourne le nombre de centres du graphe G, la liste des centres (structure de données au choix), et le rayon de G.
    n = len(G)
    centres = []
    temp = D[0][0]
    for i in range(n)  :
        if D[0][i] > temp :
            temp = D[0][i]
    rayon = temp
    #print(rayon)
    for i in range(n) :
        for j in range(n) :
            #print("max = ",max(D[i]))
            if max(D[i]) < rayon :
                rayon = max(D[i])           
    for i in range(n) :
        if max(D[i]) == rayon :
            centres.append(G[i])
    return len(centres), centres, rayon


# TESTS
#TEST LISTES

S1 ={"id" : 0,"nom" : "A", "aretes" : []}
S2 ={"id" : 1,"nom" : "B", "aretes" : []}
S3 ={"id" : 2,"nom" : "C", "aretes" : []}
S4 ={"id" : 3,"nom" : "D", "aretes" : []}

S5 = {"id" : 2,"nom" : "D", "aretes" : []}


grapheL = graphe_videL()

add_sommetL(grapheL, S1)
add_sommetL(grapheL, S2)
add_sommetL(grapheL, S3)
add_sommetL(grapheL, S4) 

addL(grapheL, S1, S2) # A B
addL(grapheL, S1, S3) # A C
addL(grapheL, S1, S4) #A D 
addL(grapheL, S2, S3) # B C
addL(grapheL, S3, S4) # D C
#addL(grapheL, S2, S4) # D B


print("graphe L :\n", grapheL)

D = calcul_distances(grapheL)
print("matrice de distances :\n", D)

print("diametre : ", donne_diametre(grapheL, D))

print("\nnombre de centres : ", donne_centres(grapheL, D)[0])
print("centres : ", donne_centres(grapheL, D)[1])
print("rayon : ", donne_centres(grapheL, D)[2])

