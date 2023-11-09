from metier.prof import Prof
from metier.eleve import Eleve
from metier.critere import Critere
from metier.stage import Stage
from dao.userDao import UserDao
from metier.listEnvie import ListEnvie
from dao.assoCritUserDAO import AssoCritUserDao
from dao.assoStageUserDao import AssoStageUserDao


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
        list_envie=[],
        souhaite_alertes=False
            ):
        super().__init__(
            critere=critere,
            list_envie=list_envie,
            email=email,
            mdp=mdp,
            code_insee_residence=code_insee_residence,
            souhaite_alertes=souhaite_alertes
            )
    
    @classmethod
    def charger_user(self, email, mdp):
        res = UserDao().charger_user(email, mdp)
        if not res:
            raise "email ou mdp incorrect"
        if "Admin" not in res["profil"]:
            raise "L'utilisateur n'est pas un administrateur"
        #listStage = []
        #listCritere = []
        #if AssoCritUserDao().exist_email(email):
            listCritere = Admin.charger_all_critere_mail(email)
        #     print(len(listCritere))
        # print(AssoStageUserDao().exist_email(email))
        #if AssoStageUserDao().exist_email(email):
            listStage = Admin.charger_all_stage_mail(email)
   
        return Admin(
                    email=res["email"],
                    mdp=res["mdp"],
                    critere=None,
                    list_envie=None,
                    code_insee_residence=res["code_insee_residence"],
                    souhaite_alertes=res["souhaite_alertes"]
                    )

    def chargerUnAutreUser(self, email):
        res = UserDao().charger_user_email(email)
        if not res:
            raise "email ou mdp incorrect"
        listStage = []
        listCritere = []
        if AssoCritUserDao().exist_email(email):
            listCritere = Admin.charger_all_critere_mail(email)
        if AssoStageUserDao().exist_email(email):
            listStage = Admin.charger_all_stage_mail(email)
        if "Admin" in res["profil"]:
            unUser = Admin(
                        email=res["email"],
                        mdp=res["mdp"],
                        critere=listCritere,
                        list_envie=listStage,
                        code_insee_residence=res["code_insee_residence"],
                        souhaite_alertes=res["souhaite_alertes"]
                    )
        elif "Prof" in res["profil"]:
            unUser = Prof(
                        email=res["email"],
                        mdp=res["mdp"],
                        critere=listCritere,
                        list_envie=listStage,
                        code_insee_residence=res["code_insee_residence"],
                        souhaite_alertes=res["souhaite_alertes"]
                    )
        elif "Eleve" in res["profil"]:
            unUser = Eleve(
                        email=res["email"],
                        mdp=res["mdp"],
                        critere=listCritere,
                        list_envie=listStage,
                        code_insee_residence=res["code_insee_residence"],
                        souhaite_alertes=res["souhaite_alertes"]
                    )
        return unUser

    def chargerToutLemonde(self):
        listDic = UserDao().tousLesEmails()
        if len(listDic) == 0:
            return None
        listRes = []
        for res in listDic:
            listRes.append(res["email"])
        return(listRes)
    
    def chargerTout(self):
        listDic = UserDao().tous()
        print(listDic)

        if len(listDic) == 0:
            return None
    
        listRes = []
        for res in listDic:
            email = res["email"]
            #url_stage = res["url_stage"]
            listRes.append({"email": email})
    
        return (listRes)
    

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

    def ajouter_user(self, unUser):
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
            AssoStageUserDao().delete(unUser) 
            UserDao().delete_user(unUser)
                
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