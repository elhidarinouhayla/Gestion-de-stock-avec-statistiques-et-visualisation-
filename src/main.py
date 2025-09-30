from menu import *
from stock import *
from stats import *
from visualize import *
# from data import *
def main():
    while True:
        menu()
        choice = int(input("Entrer un choix: "))
        if choice == 1:
            add_product()
        elif choice == 2:
           supprimer_product()
        elif choice == 3:
            update_produit()
        elif choice == 4:
            produits_dispo()
        elif choice == 5:
            valeur_totale_stock()
            prix_moyen()
            prix_min_max()
            produit_cher_moins_cher()
        elif choice == 6:
            graphique_barres()
            Camembert_diagramme()
        elif choice == 7:
            print("Exiting...")
            break
        else:
            print("Invalid choice. choisir une option.")

if __name__ == "__main__":
 main()

