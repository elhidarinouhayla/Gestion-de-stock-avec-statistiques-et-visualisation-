from data  import * 
import numpy as np

# Valeur totale du stock (somme(prix * quantité)).
def valeur_totale_stock():
    valeurs_total =[]
    for V in data:
        prix = V[2]
        quantite = V[1]
        valeur_total = prix * quantite
        valeurs_total.append(valeur_total)
    # print(valeurs_total)
    total_stock = sum(valeurs_total)
    print(f"Valeur totale du stock est {total_stock}")

# Prix moyen des produits.
def prix_moyen():
    for V in data:
        prix = V[2]
        moyen_prix = np.mean(prix)
    print(f"prix moyen des produits : {moyen_prix}")

# Prix minimum et maximum.


def prix_min_max():
    prix_produit = []
    for item in data:
        prix = item[2]
        prix_produit.append(prix)
        Max_prix = np.max(prix_produit)
        Min_prix = np.min(prix_produit)
    print(f"Prix minimum : {Min_prix}")
    print(f"Prix maximum : {Max_prix}")

# Produit le plus cher et le moins cher.
def produit_cher_moins_cher():
    prix_produit = []
    for item in data:
        prix = item[2]
        prix_produit.append(prix)
        # print(prix_produit)
        Max_prix = np.max(prix_produit)
        Min_prix = np.min(prix_produit)
    for element in data:
        if element[2] == Max_prix:
            print(f"le produit {element[0]} est le produit le plus cher ")
        elif element[2] == Min_prix:
            print(f"le produit {element[0]} est le produit le moins cher ")





