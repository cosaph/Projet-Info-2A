from metier.eleve import Eleve
from metier.stage import Stage
from dao.userDao import UserDao


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
        code_insee_residence=None,
        souhaite_alertes=False
            ):
        super().__init__(critere=critere, email=email, mdp=mdp, code_insee_residence=code_insee_residence, souhaite_alertes=souhaite_alertes)

    @classmethod
    def charger_user(self, email, mdp):
        res = UserDao().charger_user(email, mdp)
        if not res:
            raise "email ou mdp incorrect"
        if "Prof" not in res["profil"]:
            raise "L'utilisateur n'est pas un professeur"
        listCritere = Prof.charger_all_critere_mail(email)
        return Prof(critere=listCritere, email=res["email"], mdp=res["mdp"], code_insee_residence=res["code_insee_residence"], souhaite_alertes=res["souhaite_alertes"])

    def envoyer_offre(self, mail: str, unStage: Stage):
        pass
   
    def stat_postule(self):
        pass

    def stat_trouve(self):
        pass
