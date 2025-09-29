from data import *
import numpy as np



quantite = ([])
prix_unitaire = ([])
for item in data:
    Q = item[1]
    quantite.append(Q)

    PU = item[2]
    prix_unitaire.append(PU)
print(quantite)
print(prix_unitaire)

tab1 = np.array(quantite)
tab2 = np.array(prix_unitaire)
print(tab1)
print(tab2)
stock_tableau = np.concatenate((tab1,tab2))
print(stock_tableau)
valeur_totale = np.sum(stock_tableau)
print(valeur_totale)

# prix moyen des produit
moyen_prix = np.mean(tab2)
print(moyen_prix)

# prix minimum et prix maximum 
min_prix = min(prix_unitaire)
print(min_prix)
max_prix = max(prix_unitaire)
print(max_prix)

# Produit le plus cher et le moins cher. 
for item in data:
    if item[2] == max_prix:
       print(f"le produit {item[0]} est le produit le plus cher ")
    elif item[2] == min_prix:
        print(f"le produit {item[0]} est le produit le moins cher")

        

