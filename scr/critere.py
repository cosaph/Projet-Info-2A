class Critere:
    """
    Une Critere est caractérisé par une commune cible, une spécialité, 
    une duree min et max de stage et des tailles d'entreprises dans lesquelles l'utilisateur
    est disposé à faire un stage.
    """
    def __init__(self, id, code_insee_cible: str, specialite: str, duree_min: int, duree_max, taille_entreprise):
        ''' Constructeur d'un objet Critere'''
        # prevoir autoincrement
        self.id = id
        self.code_insee_cible = code_insee_cible
        # convertion en majuscule
        self.specialite = specialite.upper()
        self.duree_min = duree_min
        self.duree_max = duree_max
        # convertion en majuscule
        self.taille_entreprise = taille_entreprise.upper()
    # selection des communes à moins de ...
    def calcul_communes_selection(self, km):
        pass

    def __str__(self):
        res = "Commune de résidence: {} \nTheme du stage: {} \nDurée minimum du stage: {} \nDurée maximum du stage: {}  \nTaille entreprise: {}".format(self.code_insee_cible, self.theme, self.duree_min, self.duree_max, self.taille_entreprise)
        return res