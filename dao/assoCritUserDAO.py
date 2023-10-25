from dao.db_connection import DBConnection
from datetime import datetime


class AssoCritUserDao:

    def add(self, unCrit, unUser) -> bool:
        """
        Rajouter un couple utilisateur critere dans la base de données
        """
        
        uneDate = datetime.now()
        caPasse = False
        if unCrit is not None:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO projetInfo.association_critere_user(id_crit, email, date_recherche)"
                        "VALUES       "                                              
                        "(%(id_crit)s, %(email)s, %(date_recherche)s) "
                        "RETURNING email;    ",
                        {
                            "id_crit": unCrit.id_crit,
                            "email": unUser.email,
                            "date_recherche": uneDate
                        },
                    )
                    res = cursor.fetchone()
            if res:
                caPasse = True
        return caPasse

    def update(self, unCrit, unUser, uneDate):
        """
        Modifier une ligne de la table d'association dans la base de données
        """

        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "update projetinfo.association_critere_user "
                    "set "
                    "date_recherche =  %(date_recherche)s "
                    "where email = %(email)s and id_crit = %(id_crit)s "
                    "RETURNING email;",
                    {
                        "email": unUser.email,
                        "id_crit": unCrit.id_crit,
                        "date_recherche": uneDate
                    },
                )
                res = cursor.fetchone()
        if res:
            caPasse = True

        return caPasse
        
    def exist_email(self, email):
        """Vérifie si l'user existe dans la bdd"""
        trouve = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT email "
                    "FROM projetinfo.association_critere_user "
                    "where email = %(email)s;",
                    {
                        "email": email
                    },
                )
                res = cursor.fetchall()
        if res:
            trouve = True
        return trouve
    
    def unUser_all_id_crit(self, unUser):

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "FROM projetinfo.association_critere_user "
                    "where email = %(email)s;",
                    {
                        "email": unUser.email,
                    }
                )
                res = cursor.fetchall()
        return res
    
    def unUser_all_id_crit_mail(self, email):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "FROM projetinfo.association_critere_user "
                    "where email = %(email)s;",
                    {
                        "email": email,
                    }
                )
                res = cursor.fetchall()
        return res

    def existe_user_crit(self, unUser, unCrit):
        """
        Vérifie si l'association user critere existe dans la bdd
        """
        trouve = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT email "
                    "FROM projetinfo.association_critere_user "
                    "where email = %(email)s and id_crit = %(id_crit)s;",
                    {
                        "email": unUser.email,
                        "id_crit": unCrit.id_crit
                    },
                )
                res = cursor.fetchone()
        if res:
            trouve = True
        return trouve

    def exist_id(self, email, id_crit) -> bool:
        """
        Vérifie si l'id existe dans la bdd
        """
        trouve = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT email "
                    "FROM projetinfo.association_critere_user "
                    "where email = %(email)s and id_crit = %(id_crit)s;",
                    {
                        "email": email,
                        "id_crit": id_crit
                    },
                )
                res = cursor.fetchone()
        if res:
            trouve = True
        return trouve

    def exist_id_crit(self, id_crit) -> bool:
        """
        Vérifie si l'id existe dans la bdd
        """
        trouve = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT email "
                    "FROM projetinfo.association_critere_user "
                    "where id_crit = %(id_crit)s;",
                    {
                        "id_crit": id_crit
                    },
                )
                res = cursor.fetchone()
        if res:
            trouve = True
        return trouve
    
    def delete(self,  unUser, id_crit) -> bool:
        """
        supprime un couple
        """
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "delete from projetinfo.association_critere_user "
                    "where email = %(email)s and id_crit = %(id_crit)s"
                    "RETURNING email; ",
                    {
                        "email": unUser.email,
                        "id_crit": id_crit
                    },
                )
                res = cursor.fetchone()
        if res:
            caPasse = True
        return caPasse