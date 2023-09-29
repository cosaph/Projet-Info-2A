from dao.critereDAO import CritereDAO


class Critere:
    """
    Une Critere est caractérisé par une commune cible, une spécialité, 
    une duree min et max de stage et des tailles d'entreprises dans lesquelles l'utilisateur
    est disposé à faire un stage.
    """
    def __init__(self, 
                code_insee_cible: str,
                rayon_km : float,
                specialite: str,
                duree_min: int, 
                duree_max: int):
        ''' Constructeur d'un objet Critere'''
        self.code_insee_cible = code_insee_cible
        # convertion en majuscule
        self.specialite = specialite.upper()
        self.duree_min = duree_min
        self.duree_max = duree_max
        self.rayon_km = rayon_km
        self.id = CritereDAO().calcul_id(self)
    
    def __str__(self):
        res = "id: {} \nCommune cible: {} \nSpecialite du stage: {} \nDurée minimum du stage: {} \nDurée maximum du stage: {}".format(self.id, self.code_insee_cible, self.specialite, self.duree_min, self.duree_max)
        return res
        
    def recherche_stage(self):
        pass

    def enregistrer_critere(self):
        pass
    
    def supprimer_critere(self):
        pass

    def recherche_stage(self, url_site):
        pass