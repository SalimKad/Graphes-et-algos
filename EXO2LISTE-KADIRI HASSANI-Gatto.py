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

def loadL(nom):
    G = graphe_videL()
    f = open(nom, "r")
    #on lit le nombre de sommets
    n = int(f.readline())
    #print("n = ", n)
    i:int = 0

    for line in f:
        #print("line = ", line)
        #line = f.readline()
        line = line.strip().split() #on enlève les espaces
        if i<n:
            add_sommetL(G, {"id": int(line[0]), "nom": line[1], "aretes" : [] })
        else:
            addL(G, {"id": int(line[0])}, {"id": int(line[1])})
        i+=1
    f.close()
    return G    

def saveL(G, nom):
    try:
        f = open(nom, "w")
        n = len(G)
        f.write(str(n) + "\n")
        
        for i in range(n):
            f.write(str(G[i]["id"]) + " " + G[i]["nom"] + "\n")
            #f.write(i[0]["id"] + " " + i["nom"] + "\n")

        for i in range(n):
            for j in G[i]["aretes"]:
                f.write(str(i) + " " + str(j) + "\n")
        f.close()
    except Exception as e:
        print("Erreur d'ecriture : ", e)

def inclus_sommetL(G, G2, strict):
    #si strict = 1 -> G < G2
    #si strict = 0 -> G <= G2
    if strict == 1:
        if len(G) >= len(G2):
            return False
    else:
        if len(G) > len(G2):
            return False

    temp = []

    for i in range(len(G)):
        temp.append(G[i]["nom"])
        if G[i]["nom"] not in temp :
            return False
    return True

def inclus_aretesL(G, G2):
#renvoie 1 si les arêtes du graphe G sont incluses (strictement) dans les arêtes du graphe G’, 0 sinon.
    for i in range(len(G)):
        for j in G[i]["aretes"]:
            if not est_voisinL(G2, {"id": i}, {"id": j}):
                return False
    return True




# TESTS
#TEST LISTES

A ={"id" : 0,"nom" : "A", "aretes" : []}
B ={"id" : 1,"nom" : "B", "aretes" : []}
C ={"id" : 2,"nom" : "C", "aretes" : []}
D ={"id" : 3,"nom" : "D", "aretes" : []}


grapheL = graphe_videL()



add_sommetL(grapheL, A)
add_sommetL(grapheL, B)
#add_sommetL(grapheL, C)
#add_sommetL(grapheL, D) 


#print(A)

grapheL2 = graphe_videL()
add_sommetL(grapheL2, A)
add_sommetL(grapheL2, B)
add_sommetL(grapheL2, C)
#add_sommetL(grapheL2, D) 



print("graphe L :\n", grapheL)

print("graphe L2 :\n", grapheL2)


print("Sommets de L inclus dans L2 ? ", inclus_sommetL(grapheL, grapheL2, 1))

addL(grapheL, A, B)
addL(grapheL, C, A)
#addL(grapheL, C, B)
#addL(grapheL, B, D)


addL(grapheL2, A, B)
addL(grapheL2, C, A)
addL(grapheL2, C, B)


print("graphe L :\n", grapheL)
print("graphe L2 :\n", grapheL2)

print("Aretes de L inclus dans L2 ? ", inclus_aretesL(grapheL, grapheL2))

'''
print(est_voisinL(grapheL, A, B))
print(est_voisinL(grapheL, A, C))
print(est_voisinL(grapheL, B, C))
print(est_voisinL(grapheL, A, D))

suppL(grapheL, A, B)
print(grapheL)

print(est_voisinL(grapheL, A, C))

saveL(grapheL, "graphes.txt")

grapheL2 = loadL("graphes.txt")
print(grapheL2)

'''
