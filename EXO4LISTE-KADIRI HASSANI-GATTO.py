#KADIRI HASSANI Salim - GATTO Elisa
import numpy as np
import copy

################ FONCTIONS DE L'EXERCICE 1 DONT ON A BESOIN ################

#On crée une structure contenant les informations d'un graphe

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


################ Génération d'un graphe aléatoire ################

def G(n, p) : 
    '''créer un graphe aléatoire de n sommets et de probabilité p'''
    GrapheL = graphe_videL()
    nom = 65 #on commence les noms à A

    for i in range(n) :
        add_sommetL(GrapheL, {"id":i, "nom":chr(nom+i) ,"aretes":[]})
    for i in range(n) :
        for j in range(i+1, n) :
            if np.random.rand() < p :
                addL(GrapheL, {"id":i, "aretes":[]}, {"id":j, "aretes":[]})

    return GrapheL


################ MAIN ################

GrapheL = G(5,0)
print("Graphevide5 :\n", GrapheL)
saveL(GrapheL, "graphevide5.txt")


GrapheL2 = G(10,0.5)
print("\n\nGrapheundemi10 :\n", GrapheL2)
saveL(GrapheL2, "grapheundemi10.txt")


GrapheL3 = G(20,0.25)
print("\n\nGrapheunquart20 :\n", GrapheL3)
saveL(GrapheL3, "grapheunquart20.txt")


GrapheL4 = G(5,1)
print("\n\nGraphecomplet5 :\n", GrapheL4)
saveL(GrapheL4, "graphecomplet5.txt")

