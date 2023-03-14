# FONCTIONS DE L'EXERCICE 1 DONT ON A BESOIN

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

A ={"id" : 0,"nom" : "A", "aretes" : []}
B ={"id" : 1,"nom" : "B", "aretes" : []}
C ={"id" : 2,"nom" : "C", "aretes" : []}
D ={"id" : 3,"nom" : "D", "aretes" : []}


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
    #if inclus_sommetM(self,self2,False):
    for i in range(len(self.sommets)):
        #print(self.GraphenomM[i])
        if self.GraphenomM[i] in self2.GraphenomM:
            for j in range(len(self.sommets)):
                #print(self.GraphenomM[self.sommets[i]])
                #print(self.GraphenomM[i])
                #print(self2.GraphenomM[j])
                #print("\n")
                if self.matrice[i][j] == 1:
                    if self2.matrice[i][j] != 1:
                        return False
        else:
            for j in range(len(self.sommets)):
                #print(self.matrice[i][j])
                if self.matrice[i][j] == 1:
                    return False
    return True


def est_partiel(self, self2):
    return inclus_sommetM(self, self2, True) and inclus_areteM(self, self2)

def est_sous_graphe2(self, self2):
    if est_partiel(self, self2):
        for i in range(len(self.sommets)):
            for j in range(len(self.sommets)):
                #if(self.GraphenomM[i] is self2.GraphenomM[j]):
                    #for k in range(len(self.sommets)):
                if(self2.matrice[i][j] == 1):
                    if(self.matrice[i][j] != 1):
                        return False
    else: return False
    return True

def est_sous_graphe(self, self2):
    if not inclus_sommetM(self, self2, True):
        return False

    if not inclus_areteM(self, self2):
        return False

    temp = []
    for i in range(len(self2.GraphenomM)):
        temp.append(self2.GraphenomM[i])
    #print(temp)
    #print(self.GraphenomM)
    
    for i in range(len(self.GraphenomM)):
        if self.GraphenomM[i] not in temp:
            return False

    bool = True
    for i in range(len(self.sommets)):
        for j in range(len(self.sommets)):
            if bool == False :
                return False
            x = self.GraphenomM[i]
            y = self.GraphenomM[j]
            for k in range (len(self2.sommets)):
                if self2.GraphenomM[k] == x:
                    for l in range (len(self2.sommets)):
                        if self2.GraphenomM[l] == y:
                            if self2.matrice[k][l] == 1:
                                if self.matrice[i][j] == 1:
                                    bool = True
                                    break
                                bool = False
                    break
    return True



def est_sous_graphe_partiel(self, self2):
    return est_partiel(self, self2) and est_sous_graphe(self, self2)

'''
def est_clique(self, self2):
    A
'''

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
add(graphe3, A, C)

E ={"id" : 4,"nom" : "E", "aretes" : []}
graphe4 = Graphe()
add_sommet(graphe4, A)
add_sommet(graphe4, B)
add_sommet(graphe4, E)
add(graphe4, A, B)
add(graphe4, B, E)

graphe5 = Graphe()
add_sommet(graphe5, A)
add_sommet(graphe5, B)
add_sommet(graphe5, C)
add(graphe5, A, B)
add(graphe5, B, C)

'''
print(graphe.sommets)
print(graphe2.sommets)
print(graphe3.sommets)
print(graphe4.sommets)

print(graphe4.matrice)


print(inclus_sommetM(graphe2, graphe, 0))
print(inclus_sommetM(graphe2, graphe, 1))
print(inclus_sommetM(graphe3, graphe, 0))
print(inclus_sommetM(graphe4, graphe, 1))

print(graphe4.GraphenomM)
print(graphe4.sommets)
print(inclus_areteM(graphe3,graphe))
print(inclus_areteM(graphe4,graphe))
print(inclus_areteM(graphe4,graphe2))

print(est_partiel(graphe3, graphe))
print(est_partiel(graphe4, graphe))

print(est_sous_graphe(graphe3, graphe))
print(est_sous_graphe(graphe4, graphe))
print(est_sous_graphe(graphe5, graphe))

print(est_sous_graphe_partiel(graphe3, graphe))
print(est_sous_graphe_partiel(graphe4, graphe))
print(est_sous_graphe_partiel(graphe5, graphe))
'''