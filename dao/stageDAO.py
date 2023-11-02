from dao.db_connection import DBConnection


class StageDao():

    def add(self, unStage) -> bool:
        """
        Rajouter un stage dans la base de données
        """
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projetInfo.stage (url_stage, titre, specialite, ville) "
                    "VALUES (%(url_stage)s, %(titre)s, %(specialite)s, %(ville)s) "
                    "RETURNING url_stage;",
                    {
                        "url_stage": unStage.url_stage,
                        "titre": unStage.titre,
                        "specialite": unStage.specialite,
                        "ville": unStage.ville,
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
                    "where url_stage = %(url_stage)s "
                    "RETURNING url_stage;",
                    {
                        "url_stage": unStage.url_stage,
                        "titre": unStage.titre, 
                        "specialite": unStage.specialite,
                        "ville": unStage.ville,
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
