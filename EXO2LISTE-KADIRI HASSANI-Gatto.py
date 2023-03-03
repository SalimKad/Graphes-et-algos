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

    for i in range(len(G2)):
        temp.append(G2[i]["nom"])
    for i in range(len(G)):
        if G[i]["nom"] not in temp :
            return False
    return True

def inclus_aretesL(G, G2):
#renvoie 1 si les arêtes du graphe G sont incluses (strictement) dans les arêtes du graphe G’, 0 sinon.
    cpt:int=0
    cpt2:int=0
    for i in range(len(G2)):
        for j in G2[i]["aretes"]:
            cpt+=1

    '''for i in range(len(G)):
        for j in G[i]["aretes"]:
            cpt2+=1
            if not est_voisinL(G2, {"id": i}, {"id": j}):
                return False'''

    for i in range(len (G)):
        nom = G[i]["nom"]
        for j in G[i]["aretes"]:
            cpt2+=1
            nom2 = G[j]["nom"]
            for k in range(len (G2)) :
                if G2[k]["nom"] == nom :
                    for l in G2[k]["aretes"]:
                        if G2[l]["nom"] == nom2 :
                            verif = True
                            break
                    break   
            if not verif :
                return False

    if cpt == cpt2:
        return False
    return True


def est_partiel(G, G2):
#renvoie 1 si G est un graphe partiel de G, 0 sinon.
    if len(G2) != len(G):
        return False
    
    temp = []
    for i in range(len(G2)):
        temp.append(G2[i]["nom"])
    for i in range(len(G)):
        if G[i]["nom"] not in temp :
            return False

    if inclus_aretesL(G, G2):
            return True
    return False


def est_sous_graphe(G, G2):  #à revoir
#renvoie 1 si G est un sous-graphe de G2, 0 sinon.
    if not inclus_sommetL(G, G2, 1):
        return False
    if len(G) >= len(G2):
        return False
    temp = []
    for i in range(len(G)):
        if G2[i]["nom"] in G[i]["nom"]:
            temp.append(G2[i]) #temp contient les noms des éléments en commun
            print("temp = ",temp)
    #là mon temp contient tous les sommets, mais contient trop d'arêtes, je dois retirer celles des sommets qui n'existent plus
    for i in range(len(temp)):
        for j in temp[i]["aretes"]:
            if j not in temp:
                temp[i]["aretes"].remove(j)
    print("temp = ",temp)
    if temp == G :
        return True
    
    return False
# TESTS
#TEST LISTES

A ={"id" : 0,"nom" : "A", "aretes" : []}
B ={"id" : 1,"nom" : "B", "aretes" : []}
C ={"id" : 2,"nom" : "C", "aretes" : []}
D ={"id" : 3,"nom" : "D", "aretes" : []}


grapheL = graphe_videL()

add_sommetL(grapheL, A)
add_sommetL(grapheL, B)
add_sommetL(grapheL, C)
add_sommetL(grapheL, D) 


grapheL2 = graphe_videL()
add_sommetL(grapheL2, A)
add_sommetL(grapheL2, B)
add_sommetL(grapheL2, C)
add_sommetL(grapheL2, D) 


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
addL(grapheL2, B, D)
addL(grapheL2, C, D)


print("graphe L :\n", grapheL)
print("graphe L2 :\n", grapheL2)

print("Aretes de L inclus dans L2 ? ", inclus_aretesL(grapheL, grapheL2))

print("L est un graphe partiel de L2 ? ", est_partiel(grapheL, grapheL2))


grapheL3 = graphe_videL()
add_sommetL(grapheL3, A)
add_sommetL(grapheL3, B)
add_sommetL(grapheL3, C)
addL(grapheL3,A,B)
addL(grapheL3,C,A)
addL(grapheL3,C,B)

print("graphe L3 :\n", grapheL3)

print("L3 est un sous-graphe de L2 ? ", est_sous_graphe(grapheL3, grapheL2))


