from scr.eleveAuthentifie import EleveAuthentifie
from scr.critere import Critere
from dao.db_connection import DBConnection
from utils.singleton import Singleton

class UserDao(metaclass=Singleton):
    # def __init__(self):
    #     self.zz = "zz"
    def add_user(self, unUser: EleveAuthentifie) -> bool:
        """
        Rajouter un utilisateur dans la base de données
        """
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projetInfo.user(email, mdp, code_insee_residence, souhaite_alertes, stage_trouve, id_crit)"
                    "VALUES       "                                              
                    "(%(email)s, %(mdp)s, %(code_insee_residence)s, %(souhaite_alertes)s, %(stage_trouve)s,%(id_crit)s);    "
                    ,
                    {
                        "email": unUser.email,
                        "mdp": unUser.mdp,
                        "code_insee_residence": unUser.code_insee_residence,
                        "souhaite_alertes": unUser.souhaite_alertes,
                        "stage_trouve": unUser.stage_trouve,
                        "id_crit": unUser.critere.id
                    },
                )
                res = cursor.fetchone()
        if res:
            caPasse = True
        return caPasse

    # def update_user(self, unUser: EleveAuthentifie) -> bool:
    #     """
    #     modifier un utilisateur dans la base de données
    #     """
    #     caPasse = False
    #     with DBConnection().connection as connection:
    #         with connection.cursor() as cursor:
    #             cursor.execute(
    #             #faire
    #             )
    #             res = cursor.fetchone()
    #     if res:
    #         caPasse = True

    #     return caPasse

    # def delete_user(self, unUser: EleveAuthentifie) -> bool:
    #     """
    #     Supprimer un utilisateur dans la base de données
    #     """
    #     caPasse = False
    #     with DBConnection().connection as connection:
    #         with connection.cursor() as cursor:
    #             cursor.execute(
    #             #faire
    #             )
    #             res = cursor.fetchone()
    #     if res:
    #         caPasse = True

    #     return caPasse

    def exist_id(id) -> bool:
        """
        Vérifie si l'id existe dans la bdd
        """
        trouve = False
        # with DBConnection().connection as connection:
        #     with connection.cursor() as cursor:
        #         cursor.execute(
        #         #faire
        #         )
        return trouve


if __name__ == "__main__":
    # Pour charger les variables d'environnement contenues dans le fichier .env
    import dotenv
    dotenv.load_dotenv(override=True)

    # Création d'une attaque et ajout en BDD
    unCritere = Critere("idd", "47001", "dataS", 3, 6, "pme")
    deuxEleve = EleveAuthentifie(unCritere, "mail", "mdp", "47001", True)
   
    succes = UserDao().add_user(deuxEleve)
    print(succes)


    
