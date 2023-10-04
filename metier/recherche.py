from metier.critere import Critere
from metier.userNonauthentifie import UserNonAuthentifie


class Recherche:
    """
    Une recherche est caractérisé par un identifiant, un utilisateur, 
    un critère, une liste de stage et une date.
    """
    def __init__(self, unUser, unCritere, unSite):
       # self.id_recherche= autoincrement
        self.user = unUser
        self.critere = unCritere
        #self.site = unSite.url
        #self.list_stage = unCritere.recherche_stage(unSite)
        #self.date_recherche = today
    
    #La recherche est sauvegardée dans  l'historique
    
    def sauvegarder(self):
        pass
