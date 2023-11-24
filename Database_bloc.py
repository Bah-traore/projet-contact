import sqlite3
import os
from project_contact import Contact


class Databasebloc:

    def __init__(self, database_nom: str):
        self.nom = None
        self.date = None
        self.numero = None
        self.conn = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\\{Contact.Contact.database_nom}")
        self.conn.row_factory = sqlite3.Row

    def create_contact(self, list_personne=None):  # , nom: str = None, numero: int = 0, date=None
        # self.nom = nom
        # self.numero = numero
        # self.date = date
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Contact(
        id_contact INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nom VARCHAR,
        numero INTEGER)
        """)
        # artiste_id INTEGER REFERENCES artiste
        cursor.execute(f"INSERT INTO Contact (nom, numero) VALUES ('{list_personne[0]}', {list_personne[1]})")
        self.conn.commit()
        cursor.close()

    def create_historique(self, h_list=None):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS"historique" (
        "id_historique"	INTEGER NOT NULL,
        "id_contact"	,
        "numero"	INTEGER NOT NULL,
        "date_recent"	INTEGER NOT NULL,
        PRIMARY KEY("id_historique" AUTOINCREMENT),
        FOREIGN KEY("id_contact") REFERENCES "contact")
                """)
        cursor.execute(
            f"INSERT INTO historique (id_contact, numero, date_recent) VALUES ('{h_list[0]}', '{h_list[1]}', '{h_list[2]}')")
        self.conn.commit()
        cursor.close()

    @staticmethod
    def existe_contact():
        conn2 = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\\{Contact.Contact.database_nom}")
        # conn2 = sqlite3.connect(
        #     "E:\\Mes Dossiers\\Mes-Algorithme\\Crois\\python formation\\project_3D\\database_compte.db")
        cursor = conn2.cursor()
        try:
            cursor.execute("""
                        SELECT * FROM Contact
                            """)
        except sqlite3.OperationalError:
            # print("ERREUR: PAS DE BASE DE DONNEE EN PLACE. REESSAYER CETTE FOIS-CI")
            return None
        else:
            v = cursor.fetchall()
            conn2.commit()
            cursor.close()
            return v

    @staticmethod
    def existe_historique():
        conn3 = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}\\{Contact.Contact.database_nom}")
        # conn3 = sqlite3.connect(
        #     "E:\\Mes Dossiers\\Mes-Algorithme\\Crois\\python formation\\project_3D\\database_compte.db")
        cursor = conn3.cursor()
        cursor.execute("""
                        SELECT * FROM historique
                            """)
        v = cursor.fetchall()
        conn3.commit()
        cursor.close()
        return v
        pass
