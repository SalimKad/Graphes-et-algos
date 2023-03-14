#KADIRI HASSANI Salim - GATTO Elisa
import numpy as np

import EXO1_KADIRIHASSANI_Gatto as exo1

################ Génération d'un graphe aléatoire ################

def G(n, p) : 
    '''créer un graphe aléatoire de n sommets et de probabilité p'''
    GrapheL = exo1.graphe_videL()
    nom = 65 #on commence les noms à A

    for i in range(n) :
        exo1.add_sommetL(GrapheL, {"id":i, "nom":chr(nom+i) ,"aretes":[]})
    for i in range(n) :
        for j in range(i+1, n) :
            if np.random.rand() < p :
                exo1.addL(GrapheL, {"id":i, "aretes":[]}, {"id":j, "aretes":[]})

    return GrapheL


################ MAIN ################

GrapheL = G(5,0)
print("Graphevide5 :\n", GrapheL)
exo1.saveL(GrapheL, "graphevide5.txt")


GrapheL2 = G(10,0.5)
print("\n\nGrapheundemi10 :\n", GrapheL2)
exo1.saveL(GrapheL2, "grapheundemi10.txt")


GrapheL3 = G(20,0.25)
print("\n\nGrapheunquart20 :\n", GrapheL3)
exo1.saveL(GrapheL3, "grapheunquart20.txt")


GrapheL4 = G(5,1)
print("\n\nGraphecomplet5 :\n", GrapheL4)
exo1.saveL(GrapheL4, "graphecomplet5.txt")

