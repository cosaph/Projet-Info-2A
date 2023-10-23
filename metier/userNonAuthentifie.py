from metier.critere import Critere
# from scr.userDao import UserDao


class UserNonAuthentifie():
    '''
    Un eleve  non authentifie est composé d'un critere de recherchce de stage
    '''
    def __init__(self, unCritere):
        self.critere = unCritere
        #self.critere = self.critere.append(unCritere)

    # def creer_compte(self, id, mdp, email, code_insee_residence, souhaite_alertes):
    #     unEleveAuthentifie = EleveAuthentifie(id, mdp, email, code_insee_residence, souhaite_alertes)
    #     return UserDao().add_user(unEleveAuthentifie)
    
    def supprimer_critereAuser(self, id_crit):
        pass

    def rechercher_stage(self, critereChoix=None):
        """ 
        Recherche un stage par rapport à un critère
        Input
        -------
        critereChoix est None par défaut
            S'il est renseigné alors on effectue la recherche de stage sur ce critère
            Sinon sur le dernier critère renseigné
            Si le critere n'est pas un critere de l'Eleve, on le rajoute à la liste
        """
        
        if self.critere is None:
            raise "Pas de critères pas de recherches"
        if critereChoix is None:
            if isinstance(self.critere, list):
                return self.critere[len(self.critere)-1].recherche_stage()
            else:
                return self.critere.recherche_stage() 
        if not isinstance(critereChoix, Critere):
            raise "Les paramètre saisi n'est pas un critère"
        return critereChoix.recherche_stage()

    def creer_compte(self, email, mdp):
        pass

    def __str__(self):
        return self.critere.__str__()
