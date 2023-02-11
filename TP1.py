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

'''def loadL(nom):
    G = graphe_videL()
    f = open(nom, "r")
    #on lit le nombre de sommets
    n = int(f.readline())
    print("n = ", n)
    m = len(f.readlines())
    print("m = ", m)
    for i in range(1, n+1):
        line = f.readline()
        line = line.strip().split() #on enlève les espaces
        add_sommetL(G, {"id": int(line[0]), "nom": line[1]})
    
    print("line = ", line)
    m = len(f.readlines())
    print("m = ", m)
    line = f.readline()
    print("line 2 = ", line)
    for k in range(0,m):
        line = f.readline()
        line = line.strip().split()
        print("line =", line)
        #i = int(line[0])
        #j = int(line[1])
        addL(G, i, {"id": j})
    f.close()
    return G
'''

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
            add_sommetL(G, {"id": int(line[0]), "nom": line[1], "aretes" : [] }, )
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


'''
#2 - Représentation d'un graphe par une matrice d'adjacence :

def graphe_videM(): #créer une matrice vide
    return np.zeros((0,0))  

def add_sommetM(G, i) :
    a:int = i["id"]
    if a > len(G) :
        G = np.zeros((len(G)+1, len(G)+1))
            

def addM(G, i, j) :
    a:int = i["id"]
    b:int = j["id"]
    if a > len(G) :
        G = np.zeros((len(G)+1, len(G)+1))
    if b > len(G) :
        G = np.zeros((len(G)+1, len(G)+1))
    G[a][b] = 1
    G[a][b] = 1
 
def suppM(G, i, j) :
    a:int = i["id"]
    b:int = j["id"]
    if a < len(G) and b < len(G) :
        G[a][b] = 0
        G[a][b] = 0

def est_voisinM(G, i, j):
    a:int = i["id"]
    b:int = j["id"]
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
'''

# TESTS
grapheL = graphe_videL()
A ={"id" : 0,"nom" : "A", "aretes" : []}
B ={"id" : 1,"nom" : "B", "aretes" : []}
C ={"id" : 2,"nom" : "C", "aretes" : []}
D ={"id" : 3,"nom" : "D", "aretes" : []}

'''#tableau qui contient les sommets
sommets = [A, B, C]'''


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

G = loadL("graphes.txt")
print(G)

'''
grapheL2 = loadL("grapheL.txt")
print(grapheL2)

grapheLM = liste_to_matrice(grapheL)
print(grapheLM)


grapheM = graphe_videM()'''