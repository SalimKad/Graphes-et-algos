#KADIRI HASSANI Salim - GATTO Elisa
import numpy as np
import copy

# 1- Représentation d'un graphe par une liste de listes : 

#On crée une structure contenant les informations d'un graphe

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

def loadL(nom):
    '''charge un graphe depuis un fichier'''
    G = graphe_videL()
    f = open(nom, "r")
    #on lit le nombre de sommets
    n = int(f.readline())
    #print("n = ", n)
    i:int = 0

    for line in f:
        line = line.strip().split() #on enlève les espaces
        if i<n:
            add_sommetL(G, {"id": int(line[0]), "nom": line[1], "aretes" : [] })
        else:
            addL(G, {"id": int(line[0])}, {"id": int(line[1])})
        i+=1
    f.close()
    return G    

def saveL(G, nom):
    '''sauvegarde un graphe dans un fichier'''
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
GraphenomM = []

class Graphe: 
    def __init__(self):
        self.sommets = []
        self.matrice = np.array([])

def graphe_vide(self):
    self.sommets = []
    self.matrice = np.array([])
    
def add_sommet(self, i):
    if i["id"] not in self.sommets:
        GraphenomM.append(i["nom"])
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

grapheL2 = loadL("graphes.txt")
print(grapheL2)



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


def matrice_to_liste(mat):
    liste = graphe_videL()
    for i in range(len(mat.sommets)):
        #liste.append({"id": mat.sommets[i], "nom": GraphenomM[i], "aretes": []})
        add_sommetL(liste, {"id": mat.sommets[i], "nom": GraphenomM[i], "aretes": []})
    for i in range(len(mat.sommets)):
        for j in range(len(mat.sommets)):
            if mat.matrice[i][j] == 1:
                #liste[i]["aretes"].append(liste[j])
                addL(liste, {"id": mat.sommets[i], "nom": GraphenomM[i], "aretes": []}, {"id": mat.sommets[j], "nom": GraphenomM[j], "aretes": []})
    return liste

def liste_to_matrice(liste):
    matrice = Graphe()
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
            add(matrice, liste[liste[i]["aretes"][j]], liste[i])
    return matrice


graphe_liste = matrice_to_liste(graphe1)
print(graphe1.matrice)
print(graphe_liste)


graphe_matrice = liste_to_matrice(graphe_liste)
print(graphe_liste)
print(graphe_matrice.matrice)
