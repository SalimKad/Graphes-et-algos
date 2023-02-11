'''class Graphe:
    def __init__(self):
        self.sommets = {}
        self.n = 0
        self.m = 0

    def graphe_vide(self):
        self.sommets = {}
        self.n = 0
        self.m = 0

    def add_sommet(self, i, nom):
        if i not in self.sommets:
            self.sommets[i] = (nom, [])
            self.n += 1

    def add(self, i, j):
        if j not in self.sommets[i][1]:
            self.sommets[i][1].append(j)
            self.m += 1

    def supp(self, i, j):
        if j in self.sommets[i][1]:
            self.sommets[i][1].remove(j)
            self.m -= 1

    def est_voisin(self, i, j):
        return j in self.sommets[i][1]

    def load(self, nom):
        with open(nom, "r") as f:
            n = int(f.readline().strip())
            self.n = n
            for i in range(n):
                ligne = f.readline().strip().split(" ")
                self.sommets[int(ligne[0])] = (ligne[1], [])
            m = int(f.readline().strip())
            self.m = m
            for i in range(m):
                ligne = f.readline().strip().split(" ")
                self.add(int(ligne[0]), int(ligne[1]))

    def save(self, nom):
        with open(nom, "w") as f:
            f.write(str(self.n) + "\n")
            for i in self.sommets:
                f.write(str(i) + " " + self.sommets[i][0] + "\n")
            f.write(str(self.m) + "\n")
            for i in self.sommets:
                for j in self.sommets[i][1]:
                    f.write(str(i) + " " + str(j) + "\n")
'''
import numpy as np

class Graphe:
    def __init__(self):
        self.sommets = []
        self.matrice = np.array([])

def graphe_vide(self):
    self.sommets = []
    self.matrice = np.array([])
    
def add_sommet(self, i):
    if i not in self.sommets:
        self.sommets.append(i)
        n = len(self.sommets)
        self.matrice = np.zeros((n, n))
        
def add(self, i, j):
    if i in self.sommets and j in self.sommets:
        i_index = self.sommets.index(i)
        j_index = self.sommets.index(j)
        self.matrice[i_index][j_index] = 1
        self.matrice[j_index][i_index] = 1
        
def supp(self, i, j):
    if i in self.sommets and j in self.sommets:
        i_index = self.sommets.index(i)
        j_index = self.sommets.index(j)
        self.matrice[i_index][j_index] = 0
        self.matrice[j_index][i_index] = 0
        
def est_voisin(self, i, j):
    if i in self.sommets and j in self.sommets:
        i_index = self.sommets.index(i)
        j_index = self.sommets.index(j)
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

def save(self, nom):
    with open(nom, "w") as file:
        n = len(self.sommets)
        file.write(str(n) + "\n")
        for sommet in self.sommets:
            file.write(str(sommet) + "\n")
        for i in range(n):
            for j in range(i+1, n):
                if self.matrice[i][j] == 1:
                    file.write(str(self.sommets[i]) + " " + str(self.sommets[j]) + "\n")


graphe_vide(Graphe)
print(Graphe.sommets)
add_sommet(Graphe, 1)
add_sommet(Graphe, 2)
add_sommet(Graphe, 3)
add_sommet(Graphe, 4)


add(Graphe, 1, 2)
add(Graphe, 2, 3)
add(Graphe, 3, 4)
add(Graphe, 4, 1)
add(Graphe, 1, 3)

print(Graphe.matrice)
print(est_voisin(Graphe, 1, 2))

supp(Graphe, 1, 2)
print(Graphe.matrice)

print(est_voisin(Graphe, 1, 2))
print(est_voisin(Graphe, 2, 3))

save(Graphe, "test.txt")
