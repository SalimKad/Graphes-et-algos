#KADIRI HASSANI Salim - GATTO Elisa
import numpy as np
import copy

################ FONCTIONS DE L'EXERCICE 1 DONT ON A BESOIN ################

def graphe_videL() : 
    '''créer une liste vide'''
    return []

def add_sommetL(G, i) :
    '''ajoute un sommet à la liste de listes'''
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
        G.append(j)
        
        

def addL(G, i, j) :
    '''ajoute une arête entre i et j'''
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
    if i["id"] not in G[j["id"]]["aretes"] :
        G[j["id"]]["aretes"].append(i["id"])


def suppL(G, i, j) : 
    '''supprime l'arête entre i et j'''
    a:int = i["id"]
    b:int = j["id"]

    if b in G[a]["aretes"] :
        G[a]["aretes"].remove(b)
    if a in G[b]["aretes"] :
        G[b]["aretes"].remove(a)

def est_voisinL(G, i, j): 
    '''vérifie si i et j sont reliés par une arête'''
    a:int = i["id"]
    b:int = j["id"]

    if a<len(G) and b <len(G) :
        if b in  G[a]["aretes"] and a in G[b]["aretes"] :
            return True
    return False

################ FONCTIONS DE L'EXERCICE 3 ################

#Graphe connexe : tout sommet peut être relié à tout autre sommet par une arête ou une suite d'arêtes

def calcul_distances(G) :
    '''calcule les plus courtes distances (en nombre d’arêtes) entre tout couple de sommets du graphe G
    On utilise l'algorithme de Floyd-Warshall
    On crée une matrice de distances'''

    #on crée une matrice de distances
    n = len(G)
    D = np.zeros((n,n), dtype=int)
    for i in range(n) :

        for j in range(n) :
            if i != j :
                if est_voisinL(G, G[i], G[j]) :
                    D[i][j] = 1
                else :
                    D[i][j] = n #on met n pour représenter l'infini car on ne peut pas avoir de distance supérieure à n-1 dans un graphe connexe
            else :
                D[i][j] = 0
                
    #on calcule les plus courtes distances
    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                if D[i][k] + D[k][j] < D[i][j] : #si la distance entre i et j par k est plus courte que la distance directe entre i et j
                    D[i][j] = D[i][k] + D[k][j]
    return D


def donne_diametre(G, D):
    '''Renvoie le diamètre du graphe G à partir de la structure de données 
    D (au choix) contenant les plus courtes distances entre tout couple de sommets de G'''
    n = len(G)
    diametre = 0
    for i in range(n) :
        for j in range(n) :
            if D[i][j] > diametre :
                diametre = D[i][j]
    return diametre


def donne_centres(G, D):
    '''retourne le nombre de centres du graphe G, la liste des centres, et le rayon de G'''
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

def calcul_degres(G) : 
    '''calcul le degré de chaque sommet du graphe G'''
    n = len(G)
    degres = np.zeros(n, dtype=int)
    for i in range(n) :
        degres[i] = len(G[i]["aretes"])
    return degres

def donne_centres_degre(G, D) :
    '''retourne le nombre de centres du graphe G, la liste des centres, et le rayon de G'''
    n = len(G)
    centres = []
    degmax = D[0]

    for i in range(n)  : #on cherche le degré maximum
        if D[i] > degmax :
            degmax = D[i]    
    #print(degmax)

    for i in range(n) : #on cherche les sommets de degré maximum
        if D[i] == degmax :
            centres.append(G[i])

    return len(centres), centres, degmax

################ MAIN ################


S1 ={"id" : 0,"nom" : "A", "aretes" : []}
S2 ={"id" : 1,"nom" : "B", "aretes" : []}
S3 ={"id" : 2,"nom" : "C", "aretes" : []}
S4 ={"id" : 3,"nom" : "D", "aretes" : []}


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

######## 1er TEST ########

## RAYON, DIAMETRE, CENTRES :

print("\nMéthode de mesure RAYON, DIAMETRE, CENTRES : ")

D = calcul_distances(grapheL)
print("matrice de distances :\n", D)

print("diametre : ", donne_diametre(grapheL, D))

nbcentres, centres, rayon = donne_centres(grapheL, D)
print("\nnombre de centres : ", nbcentres)
print("centres : ", centres)
print("rayon : ", rayon)

## DEGRES :

D2 = calcul_degres(grapheL)

print("\nMéthode de mesure DEGRES : ", D2)

nbcentres2, centres2, degmax2 = donne_centres_degre(grapheL, D2)
print("\nnombre de centres : ", nbcentres2)
print("centres : ", centres2)
print("Degre maximal d'un sommet de G : ", degmax2)

######## 2ème TEST ########

S1 ={"id" : 0,"nom" : "A", "aretes" : []}
S2 ={"id" : 1,"nom" : "B", "aretes" : []}
S3 ={"id" : 2,"nom" : "C", "aretes" : []}
S4 ={"id" : 3,"nom" : "D", "aretes" : []}
S5 ={"id" : 4,"nom" : "E", "aretes" : []}

print("\n2ème TEST : ")

grapheL2 = graphe_videL()

add_sommetL(grapheL2, S1)
add_sommetL(grapheL2, S2)
add_sommetL(grapheL2, S3)
add_sommetL(grapheL2, S4)
add_sommetL(grapheL2, S5)

addL(grapheL2, S1, S2) # A B
#addL(grapheL2, S1, S3) # A C
addL(grapheL2, S1, S4) #A D
#addL(grapheL2, S1, S5) # A E
addL(grapheL2, S2, S3) # B C
#addL(grapheL2, S3, S4) # D C
addL(grapheL2, S4, S5) # E D

print("graphe L :\n", grapheL2)

## RAYON, DIAMETRE, CENTRES :
print("\n Méthode de mesure RAYON, DIAMETRE, CENTRES : ")

D = calcul_distances(grapheL2)
print("matrice de distances :\n", D)

print("diametre : ", donne_diametre(grapheL2, D))

nbcentres, centres, rayon = donne_centres(grapheL2, D)
print("\nnombre de centres : ", nbcentres)
print("centres : ", centres)
print("rayon : ", rayon)

## DEGRES :

D2 = calcul_degres(grapheL2)

print("\n Méthode de mesure DEGRES : ", D2)

nbcentres2, centres2, degmax2 = donne_centres_degre(grapheL2, D2)
print("\nnombre de centres : ", nbcentres2)
print("centres : ", centres2)
print("Degre maximal d'un sommet de G : ", degmax2)



