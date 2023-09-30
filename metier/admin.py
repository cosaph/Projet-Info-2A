from metier.prof import Prof
from metier.eleve import Eleve
from metier.critere import Critere
from metier.stage import Stage


class Admin(Prof):
    """ Un Admin hérite de la classe Prof 
    il a les même varactéristique qu'un Prof et dispose de fonctions
    supplémentaires
    """
    def __init__(self, critere, email, mdp, code_insee_residence, souhaite_alertes: bool):
        super().__init__(critere, email, mdp, code_insee_residence, souhaite_alertes)
    
    def supprime_user(self, unUser: Eleve):
        unUser.supprimer_compte()

    def supprime_critere(self, unCritere: Critere):
        unCritere.supprimer_critere()

    def supprimer_stage(self, unStage: Stage):
        unStage.supprimer_stage()