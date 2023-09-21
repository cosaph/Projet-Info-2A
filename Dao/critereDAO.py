from scr.critere import Critere

class CritereDAO:
    def add(self, unCritere: Critere) -> bool:
        """
        Rajouter un utilisateur dans la base de données
        """
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projetInfo.critere (id, code_insee_cible, specialite, duree_min, duree_max, taille_entreprise)"
                    "VALUES       "                                           
                    "(%(id)s, %(code_insee_cible)s, %(specialite)s, %(duree_min)i, %(duree_max)i, %(taille_entreprise)s;    "
                    ,
                    {
                        "id": unCritere.id,
                        "code_insee_cible": unCritere.code_insee_cible,
                        "specialite": unCritere.specialite,
                        "duree_min": unCritere.duree_min,
                        "duree_max": unCritere.duree_max,
                        "taille_entreprise": unCritere.taille_entreprise
                    },
                )
                res = cursor.fetchone()
        if res:
            caPasse = True
        return caPasse

    def update(self, unCritere: Critere) -> bool:
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

    def delete(self, unCritere: Critere) -> bool:
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