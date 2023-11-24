import time
import Contact
from project_contact import menu_de_recherche
""" 

"""
while True:
    print("""
          Choisissez l'option\n
        1- Enregistrer contact\n
        2- rechercher contact\n
        3- quitter""")
    option = input("L'option: ")
    if option.rstrip() == "1":
        Contact.Contact.ajouter()
    elif option.rstrip() == "2":
        value = input("Element search: ")
        menu_de_recherche.route(value)
    elif option.rstrip() == "3":
        break
    else:
        print("ERREUR: de frapper")
        print(f"boucler en 4sec...")
        time.sleep(5)
