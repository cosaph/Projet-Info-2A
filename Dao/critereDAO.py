from scr.critere import Critere
from dao.db_connection import DBConnection

class CritereDAO:
    def add(self, unCritere: Critere) -> bool:
        """
        Rajouter un utilisateur dans la base de données
        """
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projetInfo.critere (id_crit, code_insee_cible, specialite, duree_min, duree_max)"
                    "Values"                                     
                    "(%(id_crit)s, %(code_insee_cible)s, %(specialite)s, %(duree_min)s,"
                    "%(duree_max)s)"
                    "RETURNING id_crit;",
                    {
                        "id_crit": unCritere.id,
                        "code_insee_cible": unCritere.code_insee_cible,
                        "specialite": unCritere.specialite,
                        "duree_min": unCritere.duree_min,
                        "duree_max": unCritere.duree_max
                    },
                )
                res = cursor.fetchone()
        if res:
            caPasse = True
        return caPasse

    # def update(self, unCritere: Critere) -> bool:
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

    # def delete(self, unCritere: Critere) -> bool:
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
