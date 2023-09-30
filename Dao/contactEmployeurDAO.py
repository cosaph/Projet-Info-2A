
from dao.db_connection import DBConnection


class ContactEmployeurDAO:

    def add(self, unContact) -> bool:
        """
        Rajouter un utilisateur dans la base de données
        """
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projetInfo.Contact_employeur (email, nom, prenom,  tel)"
                    "VALUES       "                                           
                    "(%(email)s, %(nom)s, %(prenom)s, %(tel)s;    "
                    ,
                    {
                        "email": unContact.email,
                        "nom": unContact.nom,
                        "prenom": unContact.prenom,
                        "tel": unContact.tel
                    },
                )
                res = cursor.fetchone()
        if res:
            caPasse = True
        return caPasse

    def update(self, unContact) -> bool:
        """
        modifier un utilisateur dans la base de données
        """
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "update projetinfo.Contact_employeur "
                    "set "
                    "nom = %(nom)s, "
                    "prenom = %(prenom)s, "
                    "tel =  %(stage_trouve)s "
                    "where email = email = %(email)s "
                    "RETURNING email;",
                    {
                        "email": unContact.email,
                        "nom": unContact.nom,
                        "prenom": unContact.prenom,
                        "tel": unContact.tel
                    },
                )
                res = cursor.fetchone()
        if res:
            caPasse = True

        return caPasse

    def delete(self, unContact) -> bool:
        """
        Supprimer un utilisateur dans la base de données
        """
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "delete from projetinfo.Contact_employeur "
                    "where email = %(email)s "
                    "RETURNING email; ",
                    {
                        "email": unContact.email
                    },
                )
                res = cursor.fetchone()
        if res:
            caPasse = True

        return caPasse

    def exist_id(self, unContact) -> bool:
        """
        Vérifie si l'id existe dans la bdd
        """
        trouve = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT email "
                    "FROM projetinfo.Contact_employeur "
                    "where email = %(email)s;",
                    {
                        "email": unContact.email
                    },
                )
        return trouve
