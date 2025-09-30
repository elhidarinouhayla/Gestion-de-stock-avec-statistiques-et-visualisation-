from data import *

message = ("""1. Ajouter un produit. 
2. Supprimer un produit. 
3. Modifier la quantité d'un produit. 
4. Afficher le stock. 
5. Afficher les statistiques. 
6. Afficher un graphique. 
7. Quitter""")
print(message)

# ajouter un produit
choix = int(input("Entrer un choix: "))
if choix == 1:
    nauveau_produit = input("Entrer un produit: ")
    data.append(nauveau_produit)
    print(data)

# suprimer un produit
elif choix == 2:
    nom_produit = input("Enter un nom d'un produit: ")
    if nom_produit in data:
       data.remove(nom_produit)
    print(data)


    
