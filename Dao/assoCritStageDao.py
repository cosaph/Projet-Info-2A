
from scr.critere import Critere
from scr.stage import Stage
from dao.db_connection import DBConnection
from utils.singleton import Singleton


class AssoCritStageDao:
    # def __init__(self):
    #     self.zz = "zz"
    def add(self, unCrit: Critere, unStage: Stage) -> bool:
        """
        Rajouter un utilisateur dans la base de données
        """
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projetInfo.association_critere_stage(id_crit, id_stage)"
                    "VALUES       "                                              
                    "(%(id_crit)i, %(id_stage)i);",
                    {
                        "id_crit": unCrit.id,
                        "id_stage": unStage.id_stage
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

