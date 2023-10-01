from metier.eleve import Eleve
from metier.stage import Stage

class Prof(Eleve):
    """ Un Admin hérite de la classe EleveAuthentnifie
    il a les même varactéristique qu'un EleveAuthentifie et dispose de fonctions
    supplémentaires
    """
    def __init__(self, critere, email, mdp,  code_insee_residence, souhaite_alertes):
        super().__init__(critere, email, mdp, code_insee_residence, souhaite_alertes)

    def envoyer_offre(self, mail: str, unStage: Stage):
        pass
    
    def stat_postule(self):
        pass
    def stat_trouve(self):
        pass