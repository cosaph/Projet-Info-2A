class Recherche:
    """
    Une recherche est caractérisé par un identifiant, un utilisateur, 
    un critère, une liste de stage et une date.
    """
    def __init__(self, unUser, unCritere):
       # self.id_recherche= autoincrement
        self.user = unUser
        self.crit : unCritere
        self.list_stage = requeteSql_stage(self)
        #self.date_recherche = today
    
    # Retourne une liste de stage à partir de la base sql
    def requeteSql_stage(self):
        pass

    #La recherche est sauvegardée dans  l'historique
    def sauvegarder(self):
        pass
