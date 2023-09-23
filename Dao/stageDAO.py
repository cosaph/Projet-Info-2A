from scr.stage import Stage
from dao.db_connection import DBConnection

class StageDao():
    def add(self, unStage: Stage) -> bool:
        """
        Rajouter un utilisateur dans la base de données
        """
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projetInfo.stage (id_stage, lien, specialite, "
                    "code_insee, date_debut, email_employeur) "
                    "VALUES       "                                              
                    "(%(id_stage)i, %(lien)s, %(specialite)s, %(code_insee)s, "
                    "%(date_debut)s, %(email_employeur)s); ",
                    {
                        "id_stage": unStage.id,
                        "lien": unStage.lien,
                        "specialite": unStage.specialite,
                        "code_insee": unStage.code_insee,
                        "date_debut": unStage.date_debut,
                        "email_employeur": unStage.contact_employeur.email
                    },
                )
                res = cursor.fetchone()
        if res:
            caPasse = True
        return caPasse

    def update(self, unStage: Stage) -> bool:
        """
        Modifier un stage dans la base de données
        """
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "update projetinfo.utilisateur "
                    "set "
                    "lien = %(lien)s,  "
                    "specialite = %(specialite)s,  "
                    "code_insee = %(code_insee)s, "
                    "date_debut =   %(date_debut)s,  "
                    "email_employeur = %(email_employeur)s "
                    "where id_stage = id_stage "
                    "RETURNING id_stage;",
                    {
                        "lien": unStage.lien, 
                        "specialite": unStage.specialite,
                        "code_insee": unStage.code_insee,
                        "date_debut":unStage.date_debut,
                        "email_employeur": unStage.email_employeur,
                        "id_stage": unStage.id_stage
                    },
                )
                res = cursor.fetchone()
        if res:
            caPasse = True

        return caPasse

    def delete(self, unStage: Stage) -> bool:
        """
        Supprimer un stage dans la base de données
        """
        caPasse = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "delete from projetinfo.stage "
                    "where id_stage = id_stage "
                    "RETURNING id_stage; ",
                    {
                        "id_stage": unStage.id_stage
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
                    "SELECT id_stage "
                    "FROM projetinfo.stage "
                    "where id_stage = id_stage;",
                    {
                        "id_stage": unStage.id_stage
                    },
                )
                res = cursor.fetchone()
        if res:
            trouve = True     
        return trouve