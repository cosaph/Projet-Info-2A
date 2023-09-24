#from scr.critere import Critere
from dao.db_connection import DBConnection

class CritereDAO:
    def add(self, unCritere) -> bool:
        """
        Rajouter un utilisateur dans la base de données
        """
        if self.exist_id(unCritere):
            raise "Le critere est déjà enregistré dans la base de données"
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projetInfo.critere (id_crit, code_insee_cible, "
                    "specialite, duree_min, duree_max)"
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

    # def update(self, unCritere):
    #     """
    #     modifier un utilisateur dans la base de données
    #     """
    #     caPasse = False
    #     with DBConnection().connection as connection:
    #         with connection.cursor() as cursor:
    #             cursor.execute(
    #                 "update projetinfo.utilisateur "
    #                 "set "
    #                 "code_insee_cible = %(code_insee_cible)s, "
    #                 "specialite = %(specialite)s, "
    #                 "duree_min = %(duree_min)s, "
    #                 "duree_max = %(duree_max)s, "
    #                 "where id_crit = %(id_crit)s "
    #                 "RETURNING id_crit;",
    #                 {
    #                     "id_crit": unCritere.id,
    #                     "code_insee_cible": unCritere.code_insee_cible,
    #                     "specialite": unCritere.specialite,
    #                     "duree_min": unCritere.duree_min,
    #                     "duree_max": unCritere.duree_max
    #                 },
    #             )
    #             res = cursor.fetchone()
    #     if res:
    #         caPasse = True

    #     return caPasse

    def delete(self, unCritere) -> bool:
        """
        Supprimer un utilisateur dans la base de données
        """
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "delete from projetinfo.critere "
                    "where id_crit = %(id_crit)s "
                    "RETURNING id_crit; ",
                    {
                        "id_crit": unCritere.id
                    },
                )
                res = cursor.fetchone()
        if res:
            caPasse = True
        return caPasse

    def exist_id(self, unCrit) -> bool:
        """
        Vérifie si l'id existe dans la bdd
        """
        trouve = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_crit "
                    "FROM projetinfo.critere "
                    "where id_crit = %(id_crit)s;",
                    {
                        "id_crit": unCrit.id
                    },
                )
                res = cursor.fetchone()
        if res:
            #print(str(res))
            trouve = True
        return trouve
        
    def calcul_id(self, unCritere):
        """
        Attribut l'identifiant à un critere.
        Si le critere existe déjà dans id la bdd, on lui attribut l'id de ce critere
        Sinon l'identifiant n+1
        ------
        Parameter: Critere
        --------
        return: Integer
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_crit "
                    "FROM projetinfo.critere "
                    "where code_insee_cible = %(code_insee_cible)s and "
                    "specialite = %(specialite)s and "
                    "duree_min = %(duree_min)s and "
                    "duree_max = %(duree_max)s;",
                    {
                        "code_insee_cible": unCritere.code_insee_cible,
                        "specialite": unCritere.specialite,
                        "duree_min": unCritere.duree_min,
                        "duree_max": unCritere.duree_max
                    },
                )
                res = cursor.fetchone()
        if res:
            return res["id_crit"]
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT max(id_crit) "
                    "FROM projetinfo.critere; "
                )
                res = cursor.fetchone()
        if res:
            return res["max"] + 1
        return 1