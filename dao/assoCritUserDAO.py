from dao.db_connection import DBConnection
from utils.singleton import Singleton


class AssoCritUserDao:

    def add(self, unCrit, unUser, uneDate) -> bool:
        """
        Rajouter un utilisateur dans la base de données
        """
        caPasse = False
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
    
    def exist_id(self, unCrit, unUser) -> bool:
        """
        Vérifie si l'id existe dans la bdd
        """
        trouve = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT email "
                    "FROM projetinfo.utilisateur "
                    "where email = %(email)s and %(id_crit)s;",
                    {
                        "email": unUser.email,
                        "id_crit": unCrit.id_crit,
                    },
                )
                res = cursor.fetchone()
        if res:
            trouve = True
        return trouve