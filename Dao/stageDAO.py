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
                    "INSERT INTO projetInfo.stage (id_stage, lien, specialite, code_insee, date_debut, email_employeur)"
                    "VALUES       "                                              
                    "(%(id_stage)i, %(lien)s, %(specialite)s, %(code_insee)s, %(date_debut)s, %(email_employeur)s); "
                    ,
                    {
                        "id_stage": unStage.id,
                        "lien": unStage.lien,
                        "specialite": unStage.specialite,
                        "code_insee": unStage.code_insee,
                        "date_debut": unStage.date_debut,
                        "email_employeur": unStage.contact_employeur.email
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