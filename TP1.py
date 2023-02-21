#KADIRI HASSANI Salim - GATTO Elisa
import numpy as np
# 1- Représentation d'un graphe par une liste de listes : 

#On crée une structure contenant les informations d'un graphe

def graphe_videL() : #créer une liste vide
    return []

def add_sommetL(G, i) : #ajoute un sommet à la liste de listes
    temp = []
    for j in range(len(G)) :
        temp.append(G[j][0]["id"])
        #print("Temp = ",temp)
    #print(i["id"])
    #si G est vide, on ajoute le sommet à la liste de listes
    if len(G) == 0 :
        G.append([i])
    #sinon, on vérifie que le sommet n'existe pas déjà
    elif i["id"] not in temp : #si le sommet n'existe pas, on l'ajoute à la liste de listes
        G.append([i])
        

def addL(G, i, j) : #ajoute une arête entre i et j
    temp = []
    for k in range(len(G)) :
        temp.append(G[k][0]["id"])

    if i["id"] not in temp : #si le sommet n'existe pas, on l'ajoute à la liste de listes
        add_sommetL(G, i)
    if j["id"] not in temp :
        add_sommetL(G, j)
    if j["id"] not in G[i["id"]][0]["aretes"] :
        '''print(G[i["id"]])
        print(G[0][0]["aretes"])
        print(i)
        print(G[i["id"]][0]["aretes"])'''
        G[i["id"]][0]["aretes"].append(j["id"])
    #print("i id = ", i["id"])
    #print(G[j["id"]][0])
    #problem : j["id"] = 7 et  G[7] n'existe pas
    if i["id"] not in G[j["id"]][0]["aretes"] :
        G[j["id"]][0]["aretes"].append(i["id"])


def suppL(G, i, j) : #supprime l'arête entre i et j
    a:int = i["id"]
    b:int = j["id"]
    #if a in G and b in G :
    if b in G[a][0]["aretes"] :
        G[a][0]["aretes"].remove(b)
    if a in G[b][0]["aretes"] :
        G[b][0]["aretes"].remove(a)

def est_voisinL(G, i, j): #vérifie si i et j sont reliés par une arête
    a:int = i["id"]
    b:int = j["id"]
    if a<len(G) and b <len(G) :
        if b in  G[a][0]["aretes"] and a in G[b][0]["aretes"] :
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
            f.write(str(G[i][0]["id"]) + " " + G[i][0]["nom"] + "\n")
            #f.write(i[0]["id"] + " " + i[0]["nom"] + "\n")

        for i in range(n):
            for j in G[i][0]["aretes"]:
                f.write(str(i) + " " + str(j) + "\n")
        f.close()
    except Exception as e:
        print("Erreur d'ecriture : ", e)


#2 - Représentation d'un graphe par une matrice d'adjacence :
GraphenomM = []

class Graphe: 
    def __init__(self):
        self.sommets = []
        self.matrice = np.array([])

def graphe_vide(self):
    self.sommets = []
    self.matrice = np.array([])
    
def add_sommet(self, i):
    GraphenomM.append(i["nom"])

    if i["id"] not in self.sommets:
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

def load(self, nom):
    with open(nom, "r") as file:
        n = int(file.readline().strip())
        self.sommets = []
        for i in range(n):
            line = file.readline().strip()
            self.sommets.append(line)
        self.matrice = np.zeros((n, n))
        for line in file:
            sommets = line.strip().split(" ")
            i = self.sommets.index(sommets[0])
            j = self.sommets.index(sommets[1])
            self.matrice[i][j] = 1
            self.matrice[j][i] = 1

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
        f.write(str(sommet) + " " + GraphenomM[cpt] +"\n")
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
graphe_vide(Graphe)
print(Graphe.sommets)
add_sommet(Graphe, A)
add_sommet(Graphe, B)
add_sommet(Graphe, C)
add_sommet(Graphe, D)

print(Graphe.matrice)


add(Graphe, A, B)
add(Graphe, C, D)
add(Graphe, B, C)
add(Graphe, D, A)
add(Graphe, A, C)

print(Graphe.matrice)
print("A et B sont voisins ? ", est_voisin(Graphe, A, B))
print(GraphenomM)

supp(Graphe, A, B)
print(Graphe.matrice)

print("A et B sont voisins ? ",est_voisin(Graphe, A, B))
print("B et C sont voisins ? ",est_voisin(Graphe, B, C))

saveM(Graphe, "test.txt")

Graphe2 = loadM("test.txt")
print(Graphe2.matrice)
