from metier.critere import Critere
# from scr.userDao import UserDao

class UserNonAuthentifie():
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
    
    def creer_compte(self, email, mdp):
        pass

    def __str__(self):
        return self.critere.__str__()
