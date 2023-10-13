from metier.userNonAuthentifie import UserNonAuthentifie
from metier.stage import Stage
from metier.critere import Critere
from dao.userDao import UserDao
from dao.critereDAO import CritereDAO
from dao.assoCritStageDao import AssoCritStageDao
from dao.assoCritUserDAO import AssoCritUserDao
from datetime import datetime


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
        critere,
        email,
        mdp,
        code_insee_residence,
        souhaite_alertes
       ):

        super().__init__(critere)
        self.mdp = mdp
        self.email = email
        self.list_envie = list()
        self.code_insee_residence = code_insee_residence
        self.souhaite_alertes = souhaite_alertes
        self.stage_trouve = False

    # modifier
    @classmethod
    def charger_user(self, email, mdp):
        res = UserDao().charger_user(email, mdp)
        if not res:
            raise "email ou mdp incorrect"

        listCritere = Eleve.charger_all_critere_mail(email)
        return Eleve(listCritere, res["email"], res["mdp"], res["code_insee_residence"], res["souhaite_alertes"])

    def possede_critere(self, unCritere):
        return AssoCritUserDao().existe_user_crit(self, unCritere)

    def ajouter_critereAuser(self, unCritere):
        if self.possede_critere(unCritere):
            raise "L' utilisateur a déjà ce critere"
        if not unCritere.existe():
            unCritere.enregistrer_critere()
        self.critere.append(unCritere)
        return AssoCritUserDao().add(unCritere, self, datetime.now())
    
    def supprimer_critereAuser(self, id_crit):
        if AssoCritUserDao().exist_id(self.email, id_crit):
            AssoCritUserDao().delete(self, id_crit)
        if not AssoCritUserDao().exist_id_crit(id_crit):
            CritereDAO().delete_id(id_crit)

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
        for k in self.critere:
            res3 = res3 + k.__str__() +"\n"
        return "Les critères de l'utilisateur sont:\n{}Les caractéristiques de l'utilisateurs sont:\n{} ".format(res3, res)

    # ok pour les alertes ou pas
    def set_souhaite_alertes(self, reponse: bool):
        self.souhaite_alertes = reponse
        
    # l'éleve informe qu'il a trouvé un stage
    def set_stage_trouve(self, reponse: bool):
        self.stage_trouve = reponse

    def postule(self, unStage: Stage):
        pass

    def exporter_list_envie(self):
        pass

    def charger_all_critere(self):
        res = AssoCritUserDao().unUser_all_id_crit(self)
        listCritere = []
        for k in res:
            listCritere.append(Critere.charger_critere(k["id_crit"]))
        return listCritere
    
    @classmethod
    def charger_all_critere_mail(self, email):
        res = AssoCritUserDao().unUser_all_id_crit_mail(email)
        listCritere = []
        for k in res:
            listCritere.append(Critere.charger_critere(k["id_crit"]))
        return listCritere


