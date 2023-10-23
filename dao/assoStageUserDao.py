from dao.db_connection import DBConnection
from datetime import datetime


class AssoStageUserDao:

    def add(self, unStage, unUser) -> bool:
        """
        Rajouter un couple utilisateur stage dans la base de données
        """
        uneDate = datetime.now()
        caPasse = False
        if unStage is not None:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projetInfo.association_stage_user(url_stage, email, date_recherche)"
                        "VALUES       "                                              
                        "(%(url_stage)s, %(email)s, %(date_recherche)s) "
                        "RETURNING email;    ",
                        {
                            "url_stage": unStage.url_stage,
                            "email": unUser.email,
                            "date_recherche": uneDate
                        },
                    )
                    res = cursor.fetchone()
            if res:
                caPasse = True
        return caPasse
    
    def delete(self, unUser, url_stage):
        """
        supprime un couple
        """
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "delete from projetinfo.association_stage_user "
                    "where email = %(email)s and url_stage = %(url_stage)s"
                    "RETURNING email; ",
                    {
                        "email": unUser.email,
                        "url_stage": url_stage
                    },
                )
                res = cursor.fetchone()
        if res:
            caPasse = True
        return caPasse

    def existe_user_stage(self, unUser, unStage):
        """
        Vérifie si l'association user stage existe dans la bdd
        """
        trouve = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT email "
                    "FROM projetinfo.association_stage_user "
                    "where email = %(email)s and url_stage = %(url_stage)s;",
                    {
                        "email": unUser.email,
                        "url_stage": unStage.url_stage
                    },
                )
                res = cursor.fetchone()
        if res:
            trouve = True
        return trouve
    
    def exist_id(self, email, url_stage):
        """
        Vérifie si le couple existe dans la bdd
        """
        trouve = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT email "
                    "FROM projetinfo.association_stage_user "
                    "where email = %(email)s and url_stage = %(url_stage)s;",
                    {
                        "email": email,
                        "url_stage": url_stage
                    },
                )
                res = cursor.fetchone()
        if res:
            trouve = True
        return trouve

    def exist_url_stage(self, url_stage):
        """
        Vérifie si l'url du stage existe dans la bdd
        """
        trouve = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT email "
                    "FROM projetinfo.association_stage_user "
                    "where url_stage = %(url_stage)s;",
                    {
                        "url_stage": url_stage
                    },
                )
                res = cursor.fetchone()
        if res:
            trouve = True
        return trouve