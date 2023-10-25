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
        ville,
        date_debut=None,
        date_fin=None,
        contact_employeur=None
            ):

        self.url_stage = url_stage
        self.titre = titre,
        self.specialite = specialite
        self.ville = ville
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.contact_employeur = contact_employeur
    
    def existe(self):
        return StageDao().exist_id(self)
    
    @classmethod
    def charger_stage(self, url_stage, verbose=False):
        res = StageDao().charger_stage(url_stage)
        if not res:
            raise "Le stage n'existe pas"
        res = Stage(
            url_stage=res["url_stage"],
            titre=res["titre"],
            specialite=res["specialite"],
            ville=res["ville"],
            date_debut=res["date_debut"],
            date_fin=res["date_fin"]
            )
        if verbose:
            print(res)
        return res

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

    def __str__(self):
        res = "Specialite du stage: {} \nurl: {} \nLibellé du stage: {} \nLieu du stage: {}".format(self.specialite,self.url_stage, self.titre, self.ville)
        return res

    def sauvegarder_dans_listeenvie(self, idUser):
        pass
