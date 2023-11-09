from dao.db_connection import DBConnection
from utils.singleton import Singleton
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
                        "INSERT INTO projetInfo.association_stage_user(titre, url_stage, email, critere, ville) "
                        "VALUES       "                                              
                        "(%(titre)s, %(url_stage)s, %(email)s, %(critere)s, %(ville)s) "
                        "RETURNING email;    ",
                        {
                            "titre": unStage.titre,
                            "url_stage": unStage.url_stage,
                            "email": unUser.email,
                            "critere" : unStage.specialite,
                            "ville" : unStage.ville
                        },
                    )
                    res = cursor.fetchone()
            if res:
                caPasse = True
        return caPasse
    
    def delete(self, unUser):
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
    
    def existe_stage(self, unStage):
        """
        Vérifie si l'association user stage existe dans la bdd
        """
        trouve = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT email "
                    "FROM projetinfo.association_stage_user "
                    "where url_stage = %(url_stage)s;",
                    {
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
                # print(email)
                # print(url_stage)
                cursor.execute(
                    "SELECT * "
                    "FROM projetinfo.association_stage_user "
                    "where email = %(email)s "
                    "and url_stage = %(url_stage)s ;  ",
                    {
                        "email": email,
                        "url_stage": url_stage
                    },
                )
                res = cursor.fetchone()
        # print(res)
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
    
    def exist_email(self, email):
        """Vérifie si l'user existe dans la bdd"""
        trouve = False
        print(trouve)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT email "
                    "FROM projetinfo.association_stage_user "
                    "where email = %(email)s;",
                    {
                        "email": email
                    },
                )
                res = cursor.fetchall()
        if res:
            trouve = True
        return trouve

    def unUser_all_url_stage(self, unUser):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "FROM projetinfo.association_stage_user "
                    "where email = %(email)s;",
                    {
                        "email": unUser.email,
                    }
                )
                res = cursor.fetchall()
        return res
    
    def unUser_all_url_stage_mail(self, email):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "FROM projetinfo.association_stage_user "
                    "where email = %(email)s;",
                    {
                        "email": email,
                    }
                )
                res = cursor.fetchall()
        return res

    def unUser_all_url_stage_mail_critere(self, email, critere):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "FROM projetinfo.association_stage_user "
                    "where email = %(email)s AND critere = %(critere)s ;",
                    {
                        "email": email,
                        "critere": critere
                    }
                )
                res = cursor.fetchall()
        return res