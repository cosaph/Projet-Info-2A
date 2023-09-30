from metier.contactEmployeur import ContactEmployeur
from dao.stageDAO import StageDao


class Stage:
    """
    Il faut revoir les attributs
    Un stage est caractérisé par un identifiant un titre, 
    une spécialité un si...
    """
    def __init__(
        self,
        url_stage,
        titre,
        specialite,
        code_commune,
        date_debut=None,
        date_fin=None,
        contact_employeur=None
            ):

        self.url_stage = url_stage
        self.titre = titre,
        self.specialite = specialite
        self.code_insee = code_commune
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.contact_employeur = contact_employeur
    
    def exite(self):
        return StageDao().exist_id(self)

    def supprimer_stage(self):
        if self.existe():
            StageDao().delete(self)

    def modifier_stage(self):
        if self.existe():
            StageDao().update(self)
    
    def enregistrer_stage(self):
        if not self.existe():
            StageDao().add(self)
        else:
            StageDao().update(self)

    def sauvegarder_dans_listeenvie(self, idUser):
        pass
