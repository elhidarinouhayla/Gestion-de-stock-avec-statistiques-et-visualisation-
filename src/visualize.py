import matplotlib.pyplot as plt
from data import *
#1. Graphique en barres : quantité par produit.

def graphique_barres():
 for p in data :
    produit = p[0]
    quantity = p[1]
    plt.bar(produit,quantity,color="green")
 plt.show()
# graphique_barres()

def Camembert_diagramme():
 produits = []
 valeurs_totales = []
 for p in data :
        produit = p[0]
        quantity = p[1]
        prix = p[2]
        valeur_totale = quantity * prix
        produits.append(produit)
        valeurs_totales.append(valeur_totale)
 plt.pie(valeurs_totales, labels=produits,autopct='%1.1f%%', startangle=90,colors=['gold', 'lightblue', 'lightgreen', 'salmon','cyan'])
 plt.title('Valeur totale par produit')
 plt.axis('equal') 
 plt.show()
# Camembert_diagramme()
  
