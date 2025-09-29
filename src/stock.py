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