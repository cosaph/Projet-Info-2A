from metier.eleve import Eleve
from metier.stage import Stage
from dao.userDao import UserDao
from metier.listEnvie import ListEnvie
from dao.assoCritUserDAO import AssoCritUserDao
from dao.assoStageUserDao import AssoStageUserDao
from metier.stage import Stage


class Prof(Eleve):
    """ Un Admin hérite de la classe EleveAuthentnifie
    il a les même varactéristique qu'un EleveAuthentifie et dispose de fonctions
    supplémentaires
    """
    def __init__(
        self,
        email,
        mdp,
        critere=None,
        list_envie=[],
        code_insee_residence=None,
        souhaite_alertes=False
       ):
    
        # super().__init__(unCritere=critere)
        self.critere = critere
        self.mdp = mdp
        self.email = email
        self.list_envie = ListEnvie(list_envie)
        self.code_insee_residence = code_insee_residence
        self.souhaite_alertes = souhaite_alertes

    @classmethod
    def charger_user(self, email, mdp):
        res = UserDao().charger_user(email, mdp)
        #print(res)
        if res == False:
            print("Mauvais identifiants veuillez recommencer")
        #if "élève.e" not in res["profil"]:
            #raise ValueError("The user is not a student")
        else :
            return Prof(
                email=res["email"],
                mdp=res["mdp"],
            )
        return(res)

    def envoyer_offre(self, mail: str, unStage: Stage):
        pass
   
    def stat_postule(self):
        pass

    def stat_trouve(self):
        pass
