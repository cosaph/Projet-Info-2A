from metier.userNonAuthentifie import UserNonAuthentifie
from metier.stage import Stage
from metier.critere import Critere
from dao.userDao import UserDao


class Eleve(UserNonAuthentifie):
    """
    Un EleveAuthentifie hérite de la classe Eleve NonAuthentifie.
    Il est caractérisé par un identifiant, un mot de passe, un email, 
    une liste de stage pour lesquels il est enthousiaste, 
    un code commune de résidence, le fait de vouloir être alerté et d'avoir 
    trouvé un stage ou pas
    """

    def __init__(self, critere, email, mdp,  code_insee_residence, souhaite_alertes):
        # if UserDao().exist_id(id):
        #     raise ("il faut choisir un autre identifiant") 
       # if not UserDao().exist_id(id):
        super().__init__(critere)
        self.mdp = mdp
        self.email = email
        self.list_envie = list()
        self.code_insee_residence = code_insee_residence
        self.souhaite_alertes = souhaite_alertes
        self.stage_trouve = False

    @classmethod
    def charger_user(self, email, mdp):
        res = UserDao().charger_user(email, mdp)
        if not res:
            raise "email ou mdp incorrect"
        unCritere = Critere(res["code_insee_cible"], res["rayon_km"], res["specialite"], res["duree_min"], res["duree_max"])
        return Eleve(unCritere, res["email"], res["mdp"],res["code_insee_residence"], res["souhaite_alertes"])

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
        res2 = "\nLes critères par défaut de l'utilisateur sont : \n{} \n\nLes caractéristiques de l'utilisateurs sont : \n{}".format(self.critere.__str__(),res)
        self.critere.__str__() + "\n" + res
        return res2

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


