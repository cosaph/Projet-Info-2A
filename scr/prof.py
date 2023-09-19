from scr.eleveAuthentifie import EleveAuthentifie 

class Prof(EleveAuthentifie):
    """ Un Admin hérite de la classe EleveAuthentnifie
    il a les même varactéristique qu'un EleveAuthentifie et dispose de fonctions
    supplémentaires
    """
    def __init__(self):
        pass
    def envoyer_offre(self, mail:str, unStage : Stage):
        pass
    
    def stat_postule(self):
        pass
    def stat_trouve(self):
        pass