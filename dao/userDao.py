# from metier.eleve import Eleve
# from metier.critere import Critere
from dao.critereDAO import CritereDAO
from dao.assoCritUserDAO import AssoCritUserDao
from dao.db_connection import DBConnection
from utils.singleton import Singleton
import hashlib


class UserDao(metaclass=Singleton):

    def chiffrer_mdp(self, mdp, email): 
        # comme sel nous allons prendre l'email de l'utilisateur.
        salt = email
        return hashlib.sha256(salt.encode() + mdp.encode('utf-8')).hexdigest()

    def add_user(self, unUser):
        # chiffrement du mot de passe 
        self.mdp_chiffre = self.chiffrer_mdp(unUser.mdp, unUser.email)
     
        if self.exist_id(unUser):
            raise "L'utilisateur a déjà un compte"
        if unUser.critere is not None:
            if not CritereDAO().exist_id(unUser.critere):
                CritereDAO().add(unUser.critere)
            if not AssoCritUserDao().existe_user_crit(unUser, unUser.critere):
                AssoCritUserDao().add(unUser.critere, unUser)       
        caPasse = "Echec d'enregistrement"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO "
                    "projetInfo.utilisateur(email, mdp, "
                    "souhaite_alertes, profil)"
                    "VALUES "                                              
                    "(%(email)s, %(mdp)s, " 
                    "%(souhaite_alertes)s, "
                    "%(profil)s)"
                    "RETURNING email;   ",
                    {
                        "email": unUser.email,
                        "mdp": self.mdp_chiffre,
                        "souhaite_alertes": unUser.souhaite_alertes,
                        "profil": str(type(unUser)),
                        
                    },
                )
                res = cursor.fetchone()
        if res:
            caPasse = unUser.email + " est enregistré dans la base de données"
        return caPasse
    
    def charger_user(self, email, mdp):
        # if not self.exist_id(unUser):
        #     raise "L'utilisateur a déjà un compte"

        mdp_chiffre = self.chiffrer_mdp(mdp, email)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "from projetinfo.utilisateur "
                    "where email = %(email)s and  mdp = %(mdp)s;", 
                    {
                        "email": email,
                        "mdp": mdp_chiffre
                    },
                )
                res = cursor.fetchone()
        if not res:
            return False
        return res

    def charger_user_email(self, email):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "from projetinfo.utilisateur "
                    "where email = %(email)s ;",
                    {
                        "email": email
                    },
                )
                res = cursor.fetchone()
        if not res:
            return False
        return res

    # a modifier 
    def charger_all_user(self):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "from projetinfo.utilisateur; "
                )
                res = cursor.fetchall()
        if not res:
            return False
        return res

    def update_user(self, unUser):
        """
        Modifier un utilisateur dans la base de données
        """
        nouvo_mdp = input("Nouveau mot de passe : ")
        self.mdp_chiffre = self.chiffrer_mdp(nouvo_mdp, unUser.email)

        #if unUser.critere is not None:
            #if not AssoCritUserDao().existe_user_crit(unUser, unUser.critere):
                #AssoCritUserDao().add(unUser.critere, unUser)
        
        caPasse = "Echec modification"
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "update projetinfo.utilisateur "
                    "set "
                    "mdp = %(mdp)s, "
                    "souhaite_alertes = %(souhaite_alertes)s, "
                    "stage_trouve =  %(stage_trouve)s "
                    "where email = %(email)s "
                    "RETURNING email;",
                    {
                        "mdp": self.mdp_chiffre,
                        "souhaite_alertes": unUser.souhaite_alertes,
                        "stage_trouve": None,
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
                    "where email = %(email)s "
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
        unUser peut etre un élève ou un prof
        """
        if isinstance(unUser, str):
            email = unUser
        else:
            email = unUser.email  # Assuming unUser is an instance of a user class with an 'email' attribute

        trouve = False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT email "
                    "FROM projetinfo.utilisateur "
                    "WHERE email = %(email)s;",
                    {
                        "email": email
                    },
                )
                res = cursor.fetchone()
        if res:
            trouve = True
        return trouve
    
    def tousLesEmails(self):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT email "
                    "FROM projetinfo.utilisateur;",
                )
                res = cursor.fetchall()
        return res
    
    def tous(self):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * "
                    "FROM projetInfo.utilisateur;",
                )
                res = cursor.fetchall()
        return res
    
    def insert_stage_trouve(self, unUser, alerte):
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "update projetinfo.utilisateur "
                    "set "
                    "stage_trouve =  %(stage_trouve)s "
                    "where email = %(email)s "
                    "RETURNING email;",
                    {
                        "stage_trouve": alerte,
                        "email": unUser.email
                    },
                )
                res = cursor.fetchone()
        return res
    
    def tout_mail_stage_touve():
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT email "
                    "FROM projetinfo.utilisateur "
                    "WHERE stage_trouve = True;",
                )
                res = cursor.fetchall()
        for k in res:
            print(k["email"])

    def tout_mail_stage_touve_bis():
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT email "
                    "FROM projetinfo.utilisateur "
                    "WHERE stage_trouve = True;",
                )
                res = cursor.fetchall()
        return res

    def creer_un_admin(self):
        
        mdp_chiffre = self.chiffrer_mdp("m","m")

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO "
                    "projetInfo.utilisateur(email, mdp, "
                    "souhaite_alertes, profil)"
                    "VALUES "                                              
                    "(%(email)s, %(mdp)s, " 
                    "%(souhaite_alertes)s, "
                    "%(profil)s)"
                    "RETURNING email;   ",
                    {
                        "email": "m",
                        "mdp": mdp_chiffre,
                        "souhaite_alertes": False,
                        "profil": "<class 'metier.admin.Admin'>",
                    }
                )
                res = cursor.fetchone()
            return res
        
    def creer_deux_exemeple(self):
        
        #premier utilisateur
        mdp_chiffre_1 = self.chiffrer_mdp("a","a")
        #deuxieme utilisateur
        mdp_chiffre_2 = self.chiffrer_mdp("b","b")


        #premier utilisateur
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO "
                    "projetInfo.utilisateur(email, mdp, "
                    "souhaite_alertes, profil)"
                    "VALUES "                                              
                    "(%(email)s, %(mdp)s, " 
                    "%(souhaite_alertes)s, "
                    "%(profil)s)"
                    "RETURNING email;   ",
                    {
                        "email": "a",
                        "mdp": mdp_chiffre_1,
                        "souhaite_alertes": False,
                        "profil": "<class 'metier.eleve.Eleve'>",
                    }
                )
                res1 = cursor.fetchone()
        
        #deuxieme utilisateur
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO "
                    "projetInfo.utilisateur(email, mdp, "
                    "souhaite_alertes, profil)"
                    "VALUES "                                              
                    "(%(email)s, %(mdp)s, " 
                    "%(souhaite_alertes)s, "
                    "%(profil)s)"
                    "RETURNING email;   ",
                    {
                        "email": "b",
                        "mdp": mdp_chiffre_2,
                        "souhaite_alertes": False,
                        "profil": "<class 'metier.eleve.Eleve'>",
                    }
                )
                res2 = cursor.fetchone()

            return res1, res2