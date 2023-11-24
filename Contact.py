import time
import Database_bloc


class Contact:
    database_nom = "database_compte.db"

    def __init__(self, ) -> None:
        pass

    @staticmethod
    def ajouter():
        database = Database_bloc.Databasebloc(Contact.database_nom)
        enregistre_nom = input("Entrez: (nom complet et fasse deux tapes espaces et ensuite le numero): ")
        enregistre_nom_split = enregistre_nom.split('  ')
        if enregistre_nom_split[0].rsplit() == enregistre_nom_split[-1].rsplit():
            return
        else:
            enregistre_nom_split = enregistre_nom.split('  ')
            temps = time.gmtime()  # Zone UTC horloge
            t_variable = (f"{temps.tm_mday}/{temps.tm_mon}/{temps.tm_year} |"
                          f" {temps.tm_hour}:{temps.tm_min}:{temps.tm_sec}")

            variable_tuple = (enregistre_nom_split[0].rstrip(), enregistre_nom_split[-1].rstrip(), t_variable)
            if variable_tuple is None:  # None est retourne lors de (input vide, saisi non conforme du msg input, )
                print("[!] ATTENTION: verifier votre saisi (nom deux tapes espaces ensuite numero). Merci!!!")
                return None
            else:
                valeur = Database_bloc.Databasebloc.existe_contact()
                if valeur is None:
                    print((variable_tuple[0]), (variable_tuple[1]))
                    database.create_contact((variable_tuple[0], variable_tuple[1]))
                else:
                    try:
                        for i in valeur:
                            for p in i:
                                if p == int(variable_tuple[1]):
                                    database.create_historique((i[0], variable_tuple[1], variable_tuple[2]))
                                    return
                    except IndexError:
                        database.create_contact((variable_tuple[0], variable_tuple[1]))
                        return
                    database.create_contact((variable_tuple[0], variable_tuple[1]))
