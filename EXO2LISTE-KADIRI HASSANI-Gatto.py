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
    #print("temp de est_partiel = ", temp)
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
        for j in range(len(G2)):
            if G2[j]["nom"] in G[i]["nom"]:
                temp.append(G2[i]) #temp contient les noms des éléments en commun
                #print("temp = ",temp)
    #là mon temp contient tous les sommets, mais contient trop d'arêtes, je dois retirer celles des sommets qui n'existent plus
    cpt:int = 0
    for i in range(len(temp)): #i parcours temp
        for j in temp[i]["aretes"]: #j parcours aretes de la case i
            cpt = 0
            for k in range (len(temp)): #k parcours temp
                if temp[k]["id"] != j:
                    cpt = cpt + 1
            if cpt == len(temp):
                temp[i]["aretes"].remove(j)
    #print("temp = ",temp)

    for i in range(len(temp)):
        for j in range(len (G)):
            if temp[i]["nom"] == G[j]["nom"]:
                if temp[i]["aretes"] != G[j]["aretes"]:
                    return False
    
    return True

def est_sous_graphe_partiel(G,G2): #à l'aire de fonctionner, à revoir
#renvoie 1 si G est un sous-graphe partiel de G2, 0 sinon.

    #On va définir tous les sous graphes de G2, et on test si c'est un graphe partiel :
    #On va donc parcourir tous les sommets de G2, et on va les retirer un par un, et on va tester si le graphe obtenu est un graphe partiel de G2
    #Si c'est le cas, on renvoie 1, sinon on renvoie 0
    sousgraphe = False

    if len(G) >= len(G2):
        return False
    
    for i in range(len(G2)): #i = case de G2
        temp = [] #sous-graphe de G2
        for j in range(len(G2)): #j = case de G2
            if j != i:
                temp.append(G2[j]) #crée len(G2)-1 cases
                if i >= len(G2) :
                    for l in temp[j]["aretes"]:
                        if l == i:
                            temp[j]["aretes"].remove(i)
        for k in range(len(temp)):
            temp[k]["id"]= k
        print("temp = ",temp)
        if est_partiel(G, temp):
            sousgraphe = True

    return sousgraphe

    if not est_partiel(G, G2):
        return False
    if not est_sous_graphe(G, G2):
        return False
    return True


# TESTS
#TEST LISTES

S1 ={"id" : 0,"nom" : "A", "aretes" : []}
S2 ={"id" : 1,"nom" : "B", "aretes" : []}
S3 ={"id" : 2,"nom" : "C", "aretes" : []}
S4 ={"id" : 3,"nom" : "D", "aretes" : []}


grapheL = graphe_videL()

add_sommetL(grapheL, S1)
add_sommetL(grapheL, S2)
add_sommetL(grapheL, S3)
add_sommetL(grapheL, S4) 


grapheL2 = graphe_videL()
add_sommetL(grapheL2, S1)
add_sommetL(grapheL2, S2)
add_sommetL(grapheL2, S3)
add_sommetL(grapheL2, S4) 


print("graphe L :\n", grapheL)

print("graphe L2 :\n", grapheL2)


print("Sommets de L inclus dans L2 ? ", inclus_sommetL(grapheL, grapheL2, 1))

addL(grapheL, S1, S2)
addL(grapheL, S3, S1)
#addL(grapheL, C, B)
#addL(grapheL, B, D)


addL(grapheL2, S1, S2)
#addL(grapheL2, S3, S2)
addL(grapheL2, S3, S1)
addL(grapheL2, S1, S4)
addL(grapheL2, S3, S4)


print("graphe L :\n", grapheL)
print("graphe L2 :\n", grapheL2)
'''
print("Aretes de L inclus dans L2 ? ", inclus_aretesL(grapheL, grapheL2))

print("L est un graphe partiel de L2 ? ", est_partiel(grapheL, grapheL2))


grapheL3 = graphe_videL()
S5 ={"id" : 1,"nom" : "C", "aretes" : []}
S6 ={"id" : 2,"nom" : "B", "aretes" : []}
add_sommetL(grapheL3, S1)
add_sommetL(grapheL3, S5)
add_sommetL(grapheL3, S6)
addL(grapheL3,S1,S5)
addL(grapheL3,S6,S1)
#addL(grapheL3,S5,S6)

print("graphe L3 :\n", grapheL3)

print("L3 est un sous-graphe de L2 ? ", est_sous_graphe(grapheL3, grapheL2))
'''


grapheL4 = graphe_videL()
S7 ={"id" : 2,"nom" : "D", "aretes" : []}

add_sommetL(grapheL4, S1)
add_sommetL(grapheL4, S2)
add_sommetL(grapheL4, S7)

addL(grapheL4,S1,S2)
#addL(grapheL4,S1,S7)

print("graphe L4 :\n", grapheL4)

grapheL5 = graphe_videL()
add_sommetL(grapheL5, S1)
add_sommetL(grapheL5, S2)
add_sommetL(grapheL5, S3)
add_sommetL(grapheL5, S4)

addL(grapheL5,S1,S2)
addL(grapheL5,S1,S4)
addL(grapheL5,S2,S3)
addL(grapheL5,S3,S4)
addL(grapheL5,S2,S4)

print("graphe L5 :\n", grapheL5)

print("L4 est un sous-graphe partiel de L5 ? ", est_sous_graphe_partiel(grapheL4, grapheL5))

