from metier.prof import Prof

class Admin(Prof):
    """ Un Admin hérite de la classe Prof 
    il a les même varactéristique qu'un Prof et dispose de fonctions
    supplémentaires
    """
    def __init__(self, critere, email, mdp, code_insee_residence, souhaite_alertes: bool):
        super().__init__(critere, email, mdp, code_insee_residence, souhaite_alertes)
    
    def supprime_user(self, idUser: str):
        pass
    def supprime_critere(self, idCrit: str):
        pass
    def supprimer_stage(self):
        pass