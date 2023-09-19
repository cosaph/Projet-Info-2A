from scr.eleveAuthentifie import EleveAuthentifie


class UserDao():
    def add_user(self, unUser: EleveAuthentifie) -> bool:
        """
        Rajouter un utilisateur dans la base de données
        """
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projetInfo.user (id, mdp, email, code_insee_residence, souhaite_alertes)"
                    "VALUES       "                                              
                    "(%(id)s, %(mdp)s, %(email)s, %(code_insee_residence)s, %(souhaite_alertes)b, %(stage_trouve)b;    "
                    ,
                    {
                        # je ne sais pas encore associer la liste de stage
                        "id": unUser.id,
                        "mdp": unUser.mdp,
                        "email": unUser.email,
                        "code_insee_residence": unUser.code_insee_residence,
                        "souhaite_alertes": unUser.souhaite_alertes,
                        "stage_trouve": unUser.stage_trouve
                    },
                )
                res = cursor.fetchone()
        if res:
            caPasse = True
        return caPasse

    def update_user(self, unUser: EleveAuthentifie) -> bool:
        """
        modifier un utilisateur dans la base de données
        """
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                #faire
                )
                res = cursor.fetchone()
        if res:
            caPasse = True

        return caPasse

    def delete_user(self, unUser: EleveAuthentifie) -> bool:
        """
        Supprimer un utilisateur dans la base de données
        """
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                #faire
                )
                res = cursor.fetchone()
        if res:
            caPasse = True

        return caPasse

    def exist_id(id)-> bool:
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