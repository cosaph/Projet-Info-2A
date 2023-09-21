from scr.stage import Stage
from dao.db_connection import DBConnection

class StageDao():
    def add(self, unStage: Stage) -> bool:
        """
        Rajouter un utilisateur dans la base de données
        """
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projetInfo.stage (id_stage, url, specialite, code_insee_residence, site_recherche, date_publication)"
                    "VALUES       "                                              
                    "(%(id_stage)s, %(url)s, %(specialite)s, %(code_insee_residence)s, %(site_recherche)b, %(date_publication)s;    "
                    ,
                    {
                        "id_stage": unStage.id,
                        "url": unStage.url,
                        "specialite": unStage.specialite,
                        "code_insee_residence": unStage.code_insee_residence,
                        "site_recherche": unStage.site_recherche,
                        "date_publication": unStage.date_publication
                    },
                )
                res = cursor.fetchone()
        if res:
            caPasse = True
        return caPasse

    # def update(self, unStage: Stage) -> bool:
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

    # def delete(self, unStage: Stage) -> bool:
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