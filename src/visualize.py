import matplotlib.pyplot as plt
from data import List
#1. Graphique en barres : quantité par produit.

def graphique_barres():
 for p in List :
    produit = p[0]
    quantity = p[1]
    plt.bar(produit,quantity,color="green")
 plt.show()
graphique_barres()