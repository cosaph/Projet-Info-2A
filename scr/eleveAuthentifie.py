from scr.eleveNonAuthentifie import EleveNonAuthentifie
from scr.stage import Stage
#from scr.userDao import UserDao

class EleveAuthentifie(EleveNonAuthentifie):
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


    # ok pour les alertes ou pas
    def set_souhaite_alertes(self, reponse):
        self.souhaite_alertes = reponse
        
    # l'éleve informe qu'il a trouvé un stage
    def set_stage_trouve(self, reponse):
        self.stage_trouve = reponse

    def postule(self, unStage: Stage):
        pass

    def exporter_list_envie(self):
        pass

    def supprimer_compte(self):
        pass
    def __str__(self):
        res = "email: {}\nListe de stages : {}\nCommune de résidence: {}\nSouhaite alerte: {}\nA trouvé un stage: {}".format(self.email, self.list_envie, self.code_insee_residence, self.souhaite_alertes, self.stage_trouve)
        return self.critere.__str__() + "\n" + res

