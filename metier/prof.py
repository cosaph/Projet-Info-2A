from metier.eleve import Eleve
from metier.stage import Stage
from dao.userDao import UserDao
from metier.listEnvie import ListEnvie
from dao.assoCritUserDAO import AssoCritUserDao
from dao.assoStageUserDao import AssoStageUserDao


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
        super().__init__(
            critere=critere,
            list_envie=list_envie,
            email=email,
            mdp=mdp,
            souhaite_alertes=souhaite_alertes
            )

    @classmethod
    def charger_user(self, email, mdp):
        res = UserDao().charger_user(email, mdp)
        if not res:
            raise "email ou mdp incorrect"
        if "Prof" not in res["profil"]:
            raise "L'utilisateur n'est pas un professeur"
        listStage = []
        listCritere = []
        if AssoCritUserDao().exist_email(email):
            listCritere = Prof.charger_all_critere_mail(email)
        #     print(len(listCritere))
        # print(AssoStageUserDao().exist_email(email))
        if AssoStageUserDao().exist_email(email):
            listStage = Prof.charger_all_stage_mail(email) 
        return Prof(
                    email=res["email"],
                    mdp=res["mdp"],
                    critere=listCritere,
                    list_envie=listStage,
                    souhaite_alertes=res["souhaite_alertes"]
                    )

    def envoyer_offre(self, mail: str, unStage: Stage):
        pass
   
    def stat_postule(self):
        pass

    def stat_trouve(self):
        pass
