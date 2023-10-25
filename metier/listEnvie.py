from metier.stage import Stage


class ListEnvie:
    def __init__(self, listStage=[]):
        self.listStage = listStage

    def __str__(self):
        if len(self.listStage) == 0:
            return "Pas de stages dans la liste d'envie"
        if self.listStage is None:
            return "Pas de stages dans la liste d'envie"
        res = ""
        for k in self.listStage:
            res = res + k.__str__() + "\n"
        return res

    def ajouter_stage(self, unStage):
        # print(unStage)
        if not isinstance(unStage, Stage):
            raise "Le paramètre doit etre un stage"
        self.listStage.append(unStage)

    def supprimer_stage(self, unStage):
        self.listStage.remove(unStage)