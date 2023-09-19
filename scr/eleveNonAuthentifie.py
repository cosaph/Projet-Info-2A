from scr.critere import Critere
# from scr.eleveAuthentifie import EleveAuthentifie
# from scr.userDao import UserDao

class EleveNonAuthentifie:
    '''
    Un eleve  non authentifie est composé d'un critere de recherchce de stage
    '''
    def __init__(self, unCritere: Critere):
        self.critere = unCritere

    # def creer_compte(self, id, mdp, email, code_insee_residence, souhaite_alertes):
    #     unEleveAuthentifie = EleveAuthentifie(id, mdp, email, code_insee_residence, souhaite_alertes)
    #     return UserDao().add_user(unEleveAuthentifie)
    
    def rechercher_stage(self):
        pass
    
    def authentifier(self):
        pass

    def __str__(self):
        return self.critere.__str__()
