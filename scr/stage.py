from scr.contactEmployeur import ContactEmployeur

class Stage:
    """
    Il faut revoir les attributs
    Un stage est caractérisé par un identifiant un titre, une spécialité un si...
    """
    def __init__(self, url_stage, titre, specialite, code_commune, date_debut, contact_employeur: ContactEmployeur):
        self.url_stage = url_stage
        self.titre = titre,
        self.specialite = specialite
        self.code_insee = code_commune
        self.date_debut = date_debut
        self.contact_employeur = contact_employeur
        
    def sauvegarder_dans_listeenvie(self, idUser):
        pass

    def enregistrer_stage(self):
        pass

    def supprimer_stage(self):
        pass

    def modifier_stage(self):
        pass
    
    def existe(self):
        pass

