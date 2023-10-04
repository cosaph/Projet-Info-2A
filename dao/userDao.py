#from scr.eleveAuthentifie import EleveAuthentifie
#from scr.critere import Critere
from dao.critereDAO import CritereDAO
from dao.db_connection import DBConnection
from utils.singleton import Singleton


class UserDao(metaclass=Singleton):
    def add_user(self, unUser):
        """
        Rajouter un utilisateur dans la base de données
        """
        if self.exist_id(unUser):
            raise "L'utilisateur a déjà un compte"
        if not CritereDAO().exist_id(unUser.critere):
            CritereDAO().add(unUser.critere)
        
        caPasse = "Echec d'enregistrement"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO projetInfo.utilisateur(email, mdp, code_insee_residence, "
                    "souhaite_alertes, stage_trouve, profil, id_crit)"
                    "VALUES       "                                              
                    "(%(email)s, %(mdp)s, %(code_insee_residence)s, "
                    "%(souhaite_alertes)s, "
                    "%(stage_trouve)s,%(profil)s,%(id_crit)s)"
                    "RETURNING email;    ",
                    {
                        "email": unUser.email,
                        "mdp": unUser.mdp,
                        "code_insee_residence": unUser.code_insee_residence,
                        "souhaite_alertes": unUser.souhaite_alertes,
                        "stage_trouve": unUser.stage_trouve,
                        "profil": str(type(unUser)),
                        "id_crit": unUser.critere.id_crit
                    },
                )
                res = cursor.fetchone()
        if res:
            caPasse = unUser.email + " est enregistré dans la base de données"
        return caPasse
    
    def charger_user(self, email, mdp):
        # if not self.exist_id(unUser):
        #     raise "L'utilisateur a déjà un compte"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "from projetinfo.utilisateur "
                    "inner join  projetinfo.critere "
	                "on projetinfo.utilisateur.id_crit = projetinfo.critere.id_crit "
                    "where email = %(email)s and  mdp = %(mdp)s;",
                    {
                        "email": email,
                        "mdp": mdp
                    },
                )
                res = cursor.fetchone()
        if not res:
            return False
        return res

    def charger_all_user(self):
        # if not self.exist_id(unUser):
        #     raise "L'utilisateur a déjà un compte"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "from projetinfo.utilisateur "
                    "left join  projetinfo.critere "
	                "on projetinfo.utilisateur.id_crit = projetinfo.critere.id_crit;"
                )
                res = cursor.fetchall()
        if not res:
            return False
        return res
    

    def update_user(self, unUser):
        """
        Modifier un utilisateur dans la base de données
        """
        if not CritereDAO().exist_id(unUser.critere):
            CritereDAO().add(unUser.critere)
        
        caPasse = "Echec modification"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "update projetinfo.utilisateur "
                    "set "
                    "mdp = %(mdp)s, "
                    "code_insee_residence = %(code_insee_residence)s, "
                    "souhaite_alertes = %(souhaite_alertes)s, "
                    "stage_trouve =  %(stage_trouve)s, "
                    "id_crit = %(id_crit)s"
                    "where email = %(email)s "
                    "RETURNING email;",
                    {
                        "mdp": unUser.mdp,
                        "code_insee_residence": unUser.code_insee_residence,
                        "souhaite_alertes": unUser.souhaite_alertes,
                        "stage_trouve": unUser.stage_trouve,
                        "id_crit": unUser.critere.id_crit,
                        "email": unUser.email
                    },
                )
                res = cursor.fetchone()
        if res:
            caPasse = "Les infomations de {} ont bien été modifiées".format(unUser.email)

        return caPasse

    def delete_user(self, unUser):
        """
        Supprimer un utilisateur dans la base de données
        """
        caPasse = "Echec delete "
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "delete from projetinfo.utilisateur "
                    "where email = email "
                    "RETURNING email; ",
                    {
                        "email": unUser.email
                    },
                )
                res = cursor.fetchone()
        if res:
            caPasse = "L'utilisateur {} a été supprimé".format(unUser.email)
        return caPasse

    def exist_id(self, unUser) -> bool:
        """
        Vérifie si l'id existe dans la bdd
        """
        trouve = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT email "
                    "FROM projetinfo.utilisateur "
                    "where email = %(email)s;",
                    {
                        "email": unUser.email
                    },
                )
                res = cursor.fetchone()
        if res:
            trouve = True
        return trouve
