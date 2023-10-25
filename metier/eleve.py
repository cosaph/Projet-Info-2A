from metier.userNonAuthentifie import UserNonAuthentifie
from metier.stage import Stage
from metier.critere import Critere
from metier.listEnvie import ListEnvie
from dao.userDao import UserDao
from dao.critereDAO import CritereDAO
from dao.stageDAO import StageDao
# from dao.assoCritStageDao import AssoCritStageDao
from dao.assoCritUserDAO import AssoCritUserDao
from dao.assoStageUserDao import AssoStageUserDao
# from datetime import datetime


class Eleve(UserNonAuthentifie):
    """
    Un EleveAuthentifie hérite de la classe Eleve NonAuthentifie.
    Il est caractérisé par un identifiant, un mot de passe, un email, 
    une liste de stage pour lesquels il est enthousiaste, 
    un code commune de résidence, le fait de vouloir être alerté et d'avoir 
    trouvé un stage ou pas
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
        self.stage_trouve = False

    # modifier
    @classmethod
    def charger_user(self, email, mdp):
        res = UserDao().charger_user(email, mdp)
        if not res:
            raise "email ou mdp incorrect"
        if "Eleve" not in res["profil"]:
            raise "L'utilisateur n'est pas un eleve"
        listStage = []
        listCritere = []
        if AssoCritUserDao().exist_email(email):
            listCritere = Eleve.charger_all_critere_mail(email)
        #     print(len(listCritere))
        # print(AssoStageUserDao().exist_email(email))
        if AssoStageUserDao().exist_email(email):
            listStage = Eleve.charger_all_stage_mail(email)
            # listEnvie = ListEnvie(Eleve.charger_all_stage_mail(email))
            # print(len(listEnvie))
            
        return Eleve(
                    email=res["email"],
                    mdp=res["mdp"],
                    critere=listCritere,
                    list_envie=listStage,
                    code_insee_residence=res["code_insee_residence"],
                    souhaite_alertes=res["souhaite_alertes"]
                    )

    # Gestion des criteres

    def possede_critere(self, unCritere):
        return AssoCritUserDao().existe_user_crit(self, unCritere)

    def ajouter_critereAuser(self, unCritere):
        # print(self)
        if self.possede_critere(unCritere):
            raise "L' utilisateur a déjà ce critere"
        if not unCritere.existe():
            unCritere.enregistrer_critere()
        if isinstance(self.critere, list):
            self.critere.append(unCritere)
        else:
            lcrit = []
            
            if Critere is not None:
                lcrit.append(self.critere)
            lcrit.append(unCritere)
            self.critere = lcrit
        return AssoCritUserDao().add(unCritere, self)
 
    def supprimer_critereAuser(self, id_crit):
        if AssoCritUserDao().exist_id(self.email, id_crit):
            AssoCritUserDao().delete(self, id_crit)
        if not AssoCritUserDao().exist_id_crit(id_crit):
            CritereDAO().delete_id(id_crit)
        
    def charger_all_critere(self, verbose=False):
        res = AssoCritUserDao().unUser_all_id_crit(self)
        listCritere = []
        for k in res:
            listCritere.append(Critere.charger_critere(k["id_crit"], verbose))
        return listCritere
    
    @classmethod
    def charger_all_critere_mail(self, email):
        res = AssoCritUserDao().unUser_all_id_crit_mail(email)
        listCritere = []
        for k in res:
            listCritere.append(Critere.charger_critere(k["id_crit"]))
        return listCritere

    # Gestion des stages

    def charger_all_stageAuser(self, verbose=False):
        res = AssoStageUserDao().unUser_all_url_stage(self)
        listStage = []
        for k in res:
            listStage.append(Stage.charger_stage(k["url_stage"], verbose))
        return listStage

    @classmethod
    def charger_all_stage_mail(self, email):
        res = AssoStageUserDao().unUser_all_url_stage_mail(email)
        listStage = []
        for k in res:
            listStage.append(Stage.charger_stage(k["url_stage"]))
        return listStage

    def possede_stage(self, unStage):
        return AssoStageUserDao().existe_user_stage(self, unStage)

    def ajouter_stageAuser(self, unStage):
        if self.possede_stage(unStage):
            raise "L' utilisateur a déjà ce stage dans la liste envie"
        if not unStage.existe():
            unStage.enregistrer_stage()
        self.list_envie.ajouter_stage(unStage)
        return AssoStageUserDao().add(unStage, self)

    def supprimer_stageAuser(self, unStage):
        if self.possede_stage(unStage):
            AssoStageUserDao().delete(self, unStage.url_stage)
        if not AssoStageUserDao().existe_stage(unStage):
            StageDao().delete(unStage)
        self.list_envie.supprimer_stage(unStage)

    def existe(self):
        return UserDao().exist_id(self)

    def modifier(self):
        if self.existe():
            UserDao().update_user(self)
            
    def enregistrer(self):
        if not self.existe():
            UserDao().add_user(self)
        else:
            self.modifier()
    
    def supprimer_compte(self):
        if self.existe():
            UserDao().delete_user(self)

    def __str__(self):
        res = "email: {}\nListe de stages : {}\nCommune de résidence: {}\nSouhaite alerte: {}\nA trouvé un stage: {}".format(self.email, self.list_envie, self.code_insee_residence, self.souhaite_alertes, self.stage_trouve)
        res3 = ""
        if self.critere is not None:
            if isinstance(self.critere, list):
                for k in self.critere:
                    res3 = res3 + k.__str__() + "\n"
            else:
                res3 = self.critere.__str__()
        return "Les critères de l'utilisateur sont:\n{}Les caractéristiques de l'utilisateurs sont:\n{} ".format(res3, res)

    # ok pour les alertes ou pas
    def set_souhaite_alertes(self, reponse: bool):
        self.souhaite_alertes = reponse
        
    # l'éleve informe qu'il a trouvé un stage
    def set_stage_trouve(self, reponse: bool):
        self.stage_trouve = reponse
    
    def rechercher_stage(self, critereChoix=None, verbose=False):
        """ 
        Recherche un stage par rapport à un critère
        Input
        -------
        critereChoix est None par défaut
            S'il est renseigné alors on effectue la recherche de stage
            sur ce critère
            Sinon sur le dernier critère
            renseigné
            Si le critere n'est pas un critere de l'Eleve,
            on le rajoute à la liste
        """  
        if self.critere is None:
            raise "Pas de critères pas de recherches"
        if critereChoix is None:
            if isinstance(self.critere, list):
                return self.critere[len(self.critere)-1].recherche_stage(verbose)
            else:
                return self.critere.recherche_stage(verbose) 
        if not isinstance(critereChoix, Critere):
            raise "Les paramètre saisi n'est pas un critère"
        if not self.possede_critere(critereChoix):
            self.ajouter_critereAuser(critereChoix)
        return critereChoix.recherche_stage(verbose)

    def postule(self, unStage: Stage):
        pass

    def exporter_list_envie(self):
        pass




