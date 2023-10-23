from dao.db_connection import DBConnection
from utils.singleton import Singleton


class AssoCritStageDao:
    # def __init__(self)
    #     self.zz = "zz"
    def add(self, unCrit, unStage) -> bool:
        """
        Rajouter un utilisateur dans la base de données
        """
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projetInfo.association_critere_stage(id_crit, url_stage)"
                    "VALUES       "                                              
                    "(%(id_crit)s, %(url_stage)s);",
                    {
                        "id_crit": unCrit.id_crit,
                        "url_stage": unStage.url_stage
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

    # def delete_user(self, unUser: Eleve) -> bool:
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

