class Stage:
    """
    Il faut revoir les attributs
    Un stage est caractérisé par un identifiant un titre, une spécialité un si...
    """
    def __init__(self, id, url, specialite, site_recherche, code_insee_residence, date_publication, contact_employeur):
        self.id, self.url = id, url
        self.specialite, self.site_recherche = specialite, site_recherche
        self.code_insee_residence = code_insee_residence
        self.date_publication = date_publication
        self.contact_employeur = contact_employeur
        
    def sauvegarder_dans_listeenvie(self, idUser):
        pass
