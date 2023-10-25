from metier.prof import Prof
from metier.eleve import Eleve
from metier.critere import Critere
from metier.stage import Stage
from dao.userDao import UserDao


class Admin(Prof):
    """ Un Admin hérite de la classe Prof 
    il a les même varactéristique qu'un Prof et dispose de fonctions
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
        if "Admin" not in res["profil"]:
            raise "L'utilisateur n'est pas un administrateur"
        listCritere = Eleve.charger_all_critere_mail(email)
        return Admin(critere=listCritere, email=res["email"], mdp=res["mdp"], code_insee_residence=res["code_insee_residence"], souhaite_alertes=res["souhaite_alertes"])

    def modifier_user(self, unUser: Eleve):
        if unUser.existe():
            unUser.modifier()
        else:
            print("L' utilisateur {} n'est pas enregistré".format(unUser.email))

    def modifier_stage(self, unStage: Stage):
        if unStage.existe():
            unStage.modifier_stage()
        else:
            print("Le stage {} n'est pas enregistré".format(unStage.url_stage))

    def ajouter_user(self, unUser: Eleve):
        if not unUser.existe():
            unUser.enregistrer()
        else:
            print("L' utilisateur {} est déjà enregistré.".format(unUser.email))

    def ajouter_critere(self, unCritere: Critere):
        if not unCritere.existe():
            unCritere.enregistrer_critere()
        else:
            print("Le critère {} est déjà enregistré".format(unCritere.id_crit))

    def ajouter_stage(self, unStage: Stage):
        if not unStage.existe():
            unStage.enregistrer_stage()
        else:
            print("Le stage {} est déjà enregistré".format(unStage.url_stage))

    def supprime_user(self, unUser: Eleve):
        if unUser.existe():
            unUser.supprimer_compte()
        else:
            print("L' utilisateur {} n'est pas enregistré".format(unUser.email))

    def supprime_critere(self, unCritere: Critere):
        if unCritere.existe():
            unCritere.supprimer_critere()
        else:
            print("Le critère {} n'est pas enregistré".format(unCritere.id_crit))

    def supprimer_stage(self, unStage: Stage):
        if unStage.existe():
            unStage.supprimer_stage()
        else:
            print("Le stage {} n'est pas enregistré".format(unStage.url_stage))