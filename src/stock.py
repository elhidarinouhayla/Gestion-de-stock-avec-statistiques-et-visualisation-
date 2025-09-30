from data import List
#ajouter produit a la list data
def add_product():
    name = input("Entrez le nom du produit: ")
    quantity = int(input("Entrez la quantité du produit: "))
    price = float(input("Entrez le prix du produit: "))
    List.append([name, quantity, price])
    print(f"Produit '{name}' ajouté avec succès.")
    print(List)
# add_product()

# Supprimer un produit.
def supprimer_product():
    name = input("Entrez le nom du produit à supprimer: ")
    for product in List:
        if product[0] == name:
            List.remove(product)
            print(f"Produit '{name}' supprimé avec succès.")
            print(List)
            return
    print(f"Produit '{name}' non trouvé.")
# supprimer_product()

# Mettre à jour un produit.
def update_produit():
   nom_produit = input("entre le nom de produit a modifier: ")
   for p in List:
      if p[0] == nom_produit:
          N_name = input("entre le nouveau nom produit: ")
          N_quantity = int(input("entre la nouvelle quantite produit: "))
          N_price = float(input("entre le nouveau prix produit: "))
          if N_name :
              p[0]=N_name
          if N_quantity :
              p[1]=N_quantity
          if N_price :
              p[2]=N_price
          print(f"Produit '{nom_produit}' mis à jour avec succès.")
          print(List)
          return
   print(f"Produit '{nom_produit}' non trouvé.")

# update_produit()

#afficher la liste des produits disponibles. 
def produits_dispo() :
    print("Liste des produits disponibles:")
    for p in List : 
        print(f"produit: {p[0]}, quantite: {p[1]}, prix: {p[2]}")
# produits_dispo()