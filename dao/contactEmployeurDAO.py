from scr.contactEmployeur import ContactEmployeur
from dao.db_connection import DBConnection

class ContactemployeurDAO:

    def add(self, unContact: ContactEmployeur) -> bool:
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

    # def update(self, unContact: ContactEmployeur) -> bool:
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

    # def delete(self, unContact: ContactEmployeur) -> bool:
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

    def exist_id(email) -> bool:
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
