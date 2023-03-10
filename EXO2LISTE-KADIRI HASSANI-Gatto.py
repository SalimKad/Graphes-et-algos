#KADIRI HASSANI Salim - GATTO Elisa
import numpy as np
import copy

################ FONCTIONS DE L'EXERCICE 1 DONT ON A BESOIN ################

# On crée une structure contenant les informations d'un graphe

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
 
################ FONCTIONS DE L'EXERCICE 2 ################

def inclus_sommetL(G, G2, strict):
    '''si strict = 1 -> G < G2
    si strict = 0 -> G <= G2'''
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
    '''renvoie 1 si les arêtes du graphe G sont incluses (strictement) dans les arêtes du graphe G2, 0 sinon.'''
    cpt:int=0
    cpt2:int=0
    verif = False
    for i in range(len(G2)):
        for j in G2[i]["aretes"]:
            cpt+=1

    for i in range(len (G)):
        nom = G[i]["nom"]
        for j in G[i]["aretes"]:
            cpt2+=1
            nom2 = G[j]["nom"]
            for k in range(len (G2)) :
                if G2[k]["nom"] == nom :
                    for l in G2[k]["aretes"]:
                        #print("l =",l)
                        #print("G2 = ",G2)
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
    '''renvoie 1 si G est un graphe partiel de G, 0 sinon'''
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


def est_sous_graphe(G, G2):
    '''renvoie 1 si G est un sous-graphe de G2, 0 sinon'''
    if not inclus_sommetL(G, G2, 1):
        return False
    if not inclus_aretesL(G, G2): 
        return False

    temp = []

    for i in range(len(G2)):
        temp.append(G2[i]["nom"])
    for i in range(len(G)):
        if G[i]["nom"] not in temp :
            return False 
        #On vérifie que les sommets de G sont bien dans G2
    #print("temp de est_partiel = ", temp)

    #On doit vérifier que les arêtes de G sont bien dans G2 :
    verif = True
    for i in range(len(G)):
        for j in G[i]["aretes"]:
            if verif == False:
                return False
            a = G[i]["nom"]
            b = G[j]["nom"]
            for k in range(len(G2)):
                if G2[k]["nom"] == a :
                    for l in G2[k]["aretes"]:
                        if G2[l]["nom"] == b :
                            verif = True
                            break
                        verif = False
                    break

    return True


    #tentaive de faire est_sous_graphe en testant toutes les combinaisons de sommets, mauvaise idée
    '''temp = []
    for i in range(len(G)):
        for j in range(len(G2)):
            if G2[j]["nom"] == G[i]["nom"]:
                #print("le nom est : ", G2[j]["nom"])
                temp.append(G2[j]) #temp contient les noms des éléments en commun
                #print("temp = ",temp)
    #là mon temp contient tous les sommets, mais contient trop d'arêtes, je dois retirer celles des sommets qui n'existent plus
    cpt:int = 0
    for i in range(len(temp)): #i parcours temp
        for j in temp[i]["aretes"]: #j parcours aretes de la case i
            cpt = 0
            for k in range (len(temp)): #k parcours temp
                if temp[k]["id"] != j:
                    cpt = cpt + 1 #cpt compte le nombre de fois où l'id de la case k est différent de j
            if cpt == len(temp): 
                print("suppresion de",j, " de ",temp[i]["aretes"])
                temp[i]["aretes"].remove(j)
    print("temp = ",temp)
    for i in range(len(temp)):
        for j in range(len (G)):
            if temp[i]["nom"] == G[j]["nom"]:
                if temp[i]["aretes"] != G[j]["aretes"]:
                    return False
    
    return True'''
    '''for i in range(len(G2)): #i = case de G2
        temp = [] #sous-graphe de G2
        noms = []
        for j in range(len(G2)): #j = case de G2
            if j != i:
                temp.append(G2[j]) #crée len(G2)-1 cases
                noms.append(G2[j]["nom"])
                if i >= len(G2) :
                    for l in temp[j]["aretes"]:
                        if l == i:
                            print("suppresion de",i, " de ",temp[j]["aretes"])
                            temp[j]["aretes"].remove(i)
        print("ici temp = ",temp)
        for k in range(len(temp)):
            temp[k]["id"]= k
        #for k in range (len(temp)):
            #print("aretes =", len(temp[k]["aretes"]), "len noms =", len(noms))
            #for l in range (len(temp[k]["aretes"]) - len(noms)):
                #print("l =", l)
                #noms.append("")
        for k in range(len(temp)):
            trouver = False
            for l in range (len (temp[k]["aretes"])):
                #if l >= len(temp):
                #print("noms[l]= ", noms)
                #print("temp = ", temp)
                #print("l = ", l)
                #if l>len(temp):
                if G2[l]["nom"] not in noms and temp[k]["aretes"][G2[l]["id"]] not in temp[k]["aretes"] :
                    #print("suppresion de",l, " de ",temp[k]["aretes"])
                    temp[k]["aretes"].remove(G2[l]["id"])

                else :
                    for m in range (len(noms)):
                        if noms[m] == temp[k]["nom"] : 
                            trouver = True
                            case = m
                            break
                    if trouver : 
                        temp[k]["aretes"][G2][l]["id"]] = case
                            #temp
                    else : 
                        print("suppresion de",l, " de ",temp[k]["aretes"])
                        temp[k]["aretes"].remove(l)
                        #temp[k]["aretes"][l] = temp[k]["aretes"][l] - 1
            for l in noms:
                if noms[l] not in temp[k]:'''

def est_sous_graphe_partiel(G,G2):
    '''renvoie 1 si G est un sous-graphe partiel de G2, 0 sinon.
    On défini tous les sous graphes de G2, et on test si c'est un graphe partiel :
    On va donc parcourir tous les sommets de G2, et on va les retirer un par un, et on va tester si le graphe obtenu est un graphe partiel de G2.
    Si c'est le cas, on renvoie 1, sinon on renvoie 0'''
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
        for k in range(len(temp)):
            for l in temp[k]["aretes"]:
                if l >= len(temp):
                    temp[k]["aretes"].remove(l)
                    #temp[k]["aretes"][l] = temp[k]["aretes"][l] - 1
        #print("temp = ",temp)
        if est_partiel(G, temp):
            sousgraphe = True

    return sousgraphe

def est_clique(G, G2):
    '''renvoie 1 si G est une clique de G2, 0 sinon'''
    if not est_sous_graphe(G, G2):
        #print("ce n'est pas un sous graphe")
        return False
    
    for i in range(len(G)):
        for j in range(len(G)):
            if i != j:
                if not est_voisinL(G, G[i], G[j]):
                    return False
                
    return True


def est_stable(G, G2):
    '''renvoie 1 si G est stable dans G2, 0 sinon'''
    if not est_sous_graphe(G, G2):
        return False
    
    for i in range(len(G)):
        if G[i]["aretes"] != []:
            return False
                    
    return True

##################### MAIN #####################

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
addL(grapheL, S2, S4) # D B

S6 ={"id" : 2,"nom" : "D", "aretes" : []}
S7 ={"id" : 3,"nom" : "C", "aretes" : []}

grapheL4 = graphe_videL()
add_sommetL(grapheL4, S1)
add_sommetL(grapheL4, S2)
add_sommetL(grapheL4, S6)
add_sommetL(grapheL4, S7)

'''addL(grapheL4, S1, S2)
addL(grapheL4, S1, S6)
addL(grapheL4, S1, S7)'''
addL(grapheL4, S2, S6)

print("graphe L4 :\n", grapheL4)

print("Sommets de L4 inclus dans L ?", inclus_sommetL(grapheL4, grapheL, 1))
print("Aretes de L4 inclus dans L ?", inclus_aretesL(grapheL4, grapheL))

print("L4 partiel de L ?", est_partiel(grapheL4, grapheL))

S8 ={"id" : 2,"nom" : "B", "aretes" : []}
S9 ={"id" : 1,"nom" : "C", "aretes" : []}

grapheL5 = graphe_videL()
add_sommetL(grapheL5, S1)
add_sommetL(grapheL5, S9)
add_sommetL(grapheL5, S8)

addL(grapheL5, S1, S8)
addL(grapheL5, S1, S9)
addL(grapheL5, S8, S9)

print("graphe L5 :\n", grapheL5)

print("L5 est un sous graphe de L ?", est_sous_graphe(grapheL5, grapheL))


print("L5 est une clique de L ?", est_clique(grapheL5, grapheL))

grapheL2 = graphe_videL()

add_sommetL(grapheL2, S1)
add_sommetL(grapheL2, S2)
add_sommetL(grapheL2, S3)
add_sommetL(grapheL2, S4) 

addL(grapheL, S1, S2) # A B
addL(grapheL, S1, S3) # A C
addL(grapheL, S1, S4) #A D 
addL(grapheL, S3, S4) # D C
addL(grapheL, S2, S4) # D B

print("graphe L2 :\n", grapheL2)
print("graphe L5 :\n", grapheL5)

print("L5 est un sous-graphe de L2 ?", est_clique(grapheL5, grapheL2))


grapheL6 = graphe_videL()
add_sommetL(grapheL6, S1)
add_sommetL(grapheL6, S9)
add_sommetL(grapheL6, S8)

addL(grapheL6, S1, S9)

print("graphe L6 :\n", grapheL6)

print("L6 est un sous graphe partiel de L ?", est_sous_graphe_partiel(grapheL6, grapheL))

print("L6 est stable de L ?", est_stable(grapheL6, grapheL))

grapheL7 = graphe_videL()

add_sommetL(grapheL7, S1)
add_sommetL(grapheL7, S9)
add_sommetL(grapheL7, S8)

print("graphe L7 :\n", grapheL7)
print("L7 est stable de L ?", est_stable(grapheL7, grapheL))