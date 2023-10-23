from metier.stage import Stage


class ListEnvie:
    def __init__(self, listStage=None):
        self.listStage = listStage

    def __str__(self):
        if self.listStage is None:
            return "Pas de stages dans la liste d'envie"
        res = ""
        for k in self.listStage:
            res + k.__str__()
        return res

    def ajouter_stage(self, unStage):
        if not isinstance(unStage, Stage):
            raise "Le paramètre doit etre un stage"
        if self.listStage is None:
            self.listStage = []
        self.listStage.append(unStage)
