import Database_bloc


class Recherche:
    def __init__(self, Barinput: (str, int)):
        self.Barinput = Barinput

    def MenuDeRecherce(self):
        resultat = Database_bloc.Databasebloc.existe_contact()
        valeur = Database_bloc.Databasebloc.existe_historique()
        condition = self.Barinput.isnumeric()
        long_data = len(resultat)
        if not condition:
            for element in resultat:  # 1er boucle aux tuples dans la liste
                afficher = f"""Nom: {element[1]}\n Numero: {element[2]}"""
                long_data -= 1
                for el in element[1:2]:  # boucle elements des tuples
                    e_spl = el.split(" ")
                    if len(e_spl) >= 2:
                        dar_split = self.Barinput.split(" ")
                        if e_spl[0] == dar_split[0] and e_spl[-1] == dar_split[-1]:
                            print(afficher)
                            for i in range(len(valeur)):
                                if element[2] == valeur[i][2]:
                                    print("recent: " + valeur[i][3])
                                    break
                        elif e_spl[0] == dar_split[0] or e_spl[-1] == dar_split[-1]:
                            print(afficher)
                            for i in range(len(valeur)):
                                if element[2] == valeur[i][2]:
                                    print("recent: " + valeur[i][3])
                    else:
                        if element[1] == self.Barinput:
                            print(afficher)
                            for i in range(len(valeur)):
                                if element[2] == valeur[i][2]:
                                    print("recent: " + valeur[i][3])
        else:
            for element in resultat:
                long_data -= 1
                if element[2] == int(self.Barinput):
                    print(f"""Nom: {element[1]}\n Numero: {element[2]}""")
                    for i in range(len(valeur)):
                        if element[2] == valeur[i][2]:
                            print("recent: " + valeur[i][3])
                elif long_data == 0:
                    print(f"Numero {self.Barinput} non trouve")


def route(mots):
    mot = Recherche(mots)
    mot.MenuDeRecherce()

