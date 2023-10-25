from dao.db_connection import DBConnection


class StageDao():
    def add(self, unStage) -> bool:
        """
        Rajouter un utilisateur dans la base de données
        """
        mailEmployeur = None
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projetInfo.stage (url_stage, titre, "
                    "specialite, "
                    "ville, date_debut, date_fin, email_employeur) "
                    "VALUES       "                                              
                    "(%(url_stage)s, %(titre)s, %(specialite)s, %(ville)s, "
                    "%(date_debut)s, %(date_fin)s, %(email_employeur)s)"
                    "RETURNING url_stage;    ",
                    {
                        "url_stage": unStage.url_stage,
                        "titre": unStage.titre,
                        "specialite": unStage.specialite,
                        "ville": unStage.ville,
                        "date_debut": unStage.date_debut,
                        "date_fin": unStage.date_fin,
                        "email_employeur": mailEmployeur
                        # "email_employeur": unStage.contact_employeur.email
                    },
                )
                res = cursor.fetchone()
        if res:
            caPasse = True
        return caPasse

    def update(self, unStage) -> bool:
        """
        Modifier un stage dans la base de données
        """
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "update projetinfo.stage "
                    "set "
                    "titre = %(titre)s,  "
                    "specialite = %(specialite)s,  "
                    "ville = %(ville)s, "
                    "date_debut =   %(date_debut)s,  "
                    "date_fin =   %(date_fin)s,  "
                    "email_employeur = %(email_employeur)s "
                    "where url_stage = %(url_stage)s "
                    "RETURNING url_stage;",
                    {
                        "url_stage": unStage.url_stage,
                        "titre": unStage.titre, 
                        "specialite": unStage.specialite,
                        "ville": unStage.ville,
                        "date_debut": unStage.date_debut,
                        "email_employeur": unStage.email_employeur
                    },
                )
                res = cursor.fetchone()
        if res:
            caPasse = True

        return caPasse

    def delete(self, unStage) -> bool:
        """
        Supprimer un stage dans la base de données
        """
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "delete from projetinfo.stage "
                    "where url_stage = %(url_stage)s "
                    "RETURNING url_stage; ",
                    {
                        "url_stage": unStage.url_stage
                    },
                )
                res = cursor.fetchone()
        if res:
            caPasse = True

        return caPasse

    def delete_id(self, url_stage):
        """
        Supprimer un stage dans la base de données
        """
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "delete from projetinfo.stage "
                    "where url_stage = %(url_stage)s "
                    "RETURNING url_stage; ",
                    {
                        "url_stage": url_stage
                    },
                )
                res = cursor.fetchone()
        if res:
            caPasse = True
        return caPasse

    def exist_id(self, unStage) -> bool:
        """
        Vérifie si l'id existe dans la bdd
        """
        trouve = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT url_stage "
                    "FROM projetinfo.stage "
                    "where url_stage = %(url_stage)s;",
                    {
                        "url_stage": unStage.url_stage
                    },
                )
                res = cursor.fetchone()
        if res:
            trouve = True     
        return trouve
    
    def charger_stage(self, url_stage):
        """ Importe un stage de la bdd """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "from projetinfo.stage "
                    "where url_stage = %(url_stage)s ;",
                    {
                        "url_stage": url_stage
                    },
                )
                res = cursor.fetchone()
        if not res:
            return False
        return res
