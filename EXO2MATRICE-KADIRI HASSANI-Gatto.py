#KADIRI HASSANI Salim - GATTO Elisa
import numpy as np
import copy

#import EXO1MATRICE-KADIRI HASSANI-Gatto as exo1

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


#2 - Représentation d'un graphe par une matrice d'adjacence :


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
        
def supp(self, i, j):
    if i["id"] in self.sommets and j["id"] in self.sommets:
        i_index = self.sommets.index(i["id"])
        j_index = self.sommets.index(j["id"])
        self.matrice[i_index][j_index] = 0
        self.matrice[j_index][i_index] = 0
        
def est_voisin(self, i, j):
    if i["id"] in self.sommets and j["id"] in self.sommets:
        i_index = self.sommets.index(i["id"])
        j_index = self.sommets.index(j["id"])
        return self.matrice[i_index][j_index] == 1
    return False


def loadM(nom):
    G = Graphe()
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
            add_sommet(G, {"id": int(line[0]), "nom": line[1]})
        else:
            add(G,{"id": int(line[0])}, {"id": int(line[1])})
        i+=1
    f.close()
    return G

def saveM(self, nom):

    f = open(nom, "w")
    n = len(self.sommets)
    f.write(str(n) + "\n")
    cpt:int = 0
    for sommet in self.sommets:
        f.write(str(sommet) + " " + self.GraphenomM[cpt] +"\n")
        cpt+=1
    for i in range(n):
        for j in range(n):
            if self.matrice[i][j] == 1:
                f.write(str(self.sommets[i]) + " " + str(self.sommets[j]) + "\n")

       
    f.close()


# TESTS
#TEST LISTES

A ={"id" : 0,"nom" : "A", "aretes" : []}
B ={"id" : 1,"nom" : "B", "aretes" : []}
C ={"id" : 2,"nom" : "C", "aretes" : []}
D ={"id" : 3,"nom" : "D", "aretes" : []}

'''
grapheL = graphe_videL()

add_sommetL(grapheL, A)
add_sommetL(grapheL, B)
add_sommetL(grapheL, C)
#add_sommetL(grapheL, D) 

addL(grapheL, A, B)
addL(grapheL, C, A)
addL(grapheL, C, B)
addL(grapheL, B, D)
print(grapheL)

print(est_voisinL(grapheL, A, B))
print(est_voisinL(grapheL, A, C))
print(est_voisinL(grapheL, B, C))
print(est_voisinL(grapheL, A, D))

suppL(grapheL, A, B)
print(grapheL)

print(est_voisinL(grapheL, A, C))

saveL(grapheL, "graphes.txt")

grapheL2 = loadL("grapheL.txt")
print(grapheL2)
'''


#TESTS MATRICE
graphe1 = Graphe()
#print(Graphe.sommets)
add_sommet(graphe1, A)
add_sommet(graphe1, B)
add_sommet(graphe1, C)
add_sommet(graphe1, D)

#print(graphe1.sommets)
#print(graphe1.matrice)

add(graphe1, A, B)
add(graphe1, C, D)
add(graphe1, B, C)
add(graphe1, D, A)
add(graphe1, A, C)

#print(graphe1.matrice)
#print("A et B sont voisins ? ", est_voisin(graphe1, A, B))
#print(GraphenomM)

supp(graphe1, A, B)
#print(graphe1.matrice)

#print("A et B sont voisins ? ",est_voisin(graphe1, A, B))
#print("B et C sont voisins ? ",est_voisin(graphe1, B, C))

saveM(graphe1, "test.txt")

Graphe2 = loadM("test.txt")
#print(Graphe2.matrice)


def matrice_to_liste(self):
    liste = graphe_videL()
    for i in range(len(self.sommets)):
        #liste.append({"id": self.sommets[i], "nom": GraphenomM[i], "aretes": []})
        add_sommetL(liste, {"id": self.sommets[i], "nom": GraphenomM[i], "aretes": []})
    for i in range(len(self.sommets)):
        for j in range(len(self.sommets)):
            if self.matrice[i][j] == 1:
                #liste[i]["aretes"].append(liste[j])
                addL(liste, {"id": self.sommets[i], "nom": GraphenomM[i], "aretes": []}, {"id": self.sommets[j], "nom": GraphenomM[j], "aretes": []})
    return liste

def liste_to_matrice(liste):
    matrice = graphe_vide(Graphe())
    #transfere de sommets du graphe en liste au graphe en matrice
    for i in range (len(liste)):
        #G i "id"
        a = liste[i]
        print("a=",a)
        add_sommet(matrice, a)
    print("Matrice = ",matrice)
    #transfere des aretes du graphe en liste au graphe en matrice
    for i in range (len(liste)):
        for j in range(len(liste[i]["aretes"])):
            add(matrice, liste[i]["aretes"][j], liste[j]["id"])
    return matrice

'''
graphe_liste = matrice_to_liste(Graphe)
print(Graphe.matrice)
print(graphe_liste)


graphe_matrice = liste_to_matrice(graphe_liste)
print(graphe_liste)
print(graphe_matrice.matrice)
'''



# EXERCICE 2 : GRAPHE PARTIEL ET SOUS-GRAPHE

def inclus_sommetM(self, self2, strict):
    if len(self.sommets) > len(self2.sommets):
        return False
    if strict:
        if len(self.sommets) == len(self2.sommets):
            return False
    else:
        for i in range(len(self.sommets)):
            if self.sommets[i] not in self2.sommets:
                return False
    return True


def inclus_areteM(self, self2):
    for i in range(len(self.sommets)):
        for j in range(len(self2.sommets)):
            if self.GrapheNomM[self.sommets[i]] == self2.GrapheNomM[self2.sommets[j]]:
                continue
            else: break
            if self.matrice[i][j] == 1:
                if self2.matrice[i][j] != 1:
                    return False
    return True


def est_partiel(self, self2):
    return inclus_sommetM(self, self2, True) and inclus_areteM(self, self2)

def est_sous_graphe(self, self2):
    if est_partiel(self, self2):
        for i in range(len(self2.sommets)):
            if(self2.GrapheNomM[self2.sommets[i]] in self.GrapheNomM):
                for j in range(len(self.sommets)):
                    if(self.GrapheNomM[self.sommets[j]] == self2.GrapheNomM[self2.sommets[i]]):
                        for k in range(len(self.sommets)):
                            if(self.matrice[j][k] == 1):
                                if(self2.matrice[i][k] != 1):
                                    return False
    return True



def est_sous_graphe_partiel(self, self2):
    return est_partiel(self, self2) and est_sous_graphe(self, self2)

def est_clique(self, self2):
    A

def est_stable(self, self2):
    if inclus_sommetM(self, self2, False):
        for i in range(len(self2.sommets)):
            for j in range(len(self2.sommets)):
                if self2.matrice[i][j] != 0:
                    return False
    return True


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

E ={"id" : 4,"nom" : "E", "aretes" : []}
graphe4 = Graphe()
add_sommet(graphe4, A)
add_sommet(graphe4, B)
add_sommet(graphe4, E)
add(graphe4, A, B)
add(graphe4, B, E)

print(graphe.sommets)
print(graphe2.sommets)
print(graphe3.sommets)
print(graphe4.sommets)

print(graphe4.matrice)

'''
print(inclus_sommetM(graphe2, graphe, 0))
print(inclus_sommetM(graphe2, graphe, 1))
print(inclus_sommetM(graphe3, graphe, 0))
print(inclus_sommetM(graphe4, graphe, 1))
'''

#print(inclus_areteM(graphe2, graphe))
#print(inclus_areteM(graphe3, graphe))
print(inclus_areteM(graphe4, graphe))