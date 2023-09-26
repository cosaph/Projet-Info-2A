class Stage:
    """
    Il faut revoir les attributs
    Un stage est caractérisé par un identifiant un titre, une spécialité un si...
    """
    def __init__(self, id, url_stage, specialite, site_recherche, code_commune, date_debut, contact_employeur):
        self.url_stage = url_stage
        self.specialite = specialite
        self.code_insee = code_commune
        self.date_debut = date_debut
        self.contact_employeur = contact_employeur
        
    def sauvegarder_dans_listeenvie(self, idUser):
        pass
