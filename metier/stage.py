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
            ):
        self.url_stage = url_stage
        self.titre = titre,
        self.specialite = specialite
        self.ville = ville,

    def existe(self):
        return StageDao().exist_id(self)

    @classmethod
    def charger_stage(self, url_stage, titre, ville, verbose=False):
        res = StageDao().charger_stage(url_stage, titre, ville)
        if not res:
            raise "Le stage n'existe pas"
        res = Stage(
            url_stage=res["url_stage"],
            titre=res["titre"],
            specialite=res["specialite"],
            ville=res["ville"],
            )
        if verbose:
            print(res)
        return res

    # pas utilisé 
    def supprimer_stage(self):
        if self.existe():
            StageDao().delete(self)

    # pas utilisé 
    def modifier_stage(self):
        if self.existe():
            StageDao().update(self)
    
    def creer_stage(url_stage, titre, specialite, ville):
        """
        Créer un stage
        Le stage est ajouté à la base de données
        
        """
        S = Stage(url_stage, titre, specialite, ville)
        if S.existe():
            print("Le stage existe déjà")
        else:
            StageDao().add(S)
   
    """
    def __str__(self):
        res = "Specialite du stage: {} \nurl: {} \nLibellé du stage: {} \nLieu du stage: {}".format(self.specialite,self.url_stage, self.titre, self.ville)
        return res
    """

    def sauvegarder_dans_listeenvie(self, idUser):
        pass
