

from metier.eleve import Eleve
from metier.prof import Prof
from dao.userDao import UserDao
from dao.stageDAO import StageDao
from metier.stage import Stage

class Creation:
    
    def __init__(self, mdp, email, souhaite_alertes, type):
        self.mdp = mdp
        self.email = email
        self.souhaite_alertes = souhaite_alertes
        self.type = type
    
    def creer_compte(self):
        if self.type == 'élève':
            E = Eleve(self.email, self.mdp, [], [], None, self.souhaite_alertes)
            if UserDao().exist_id(E):
                print("L'utilisateur existe déjà")
            else:
                UserDao().add_user(E)
        else:
            P = Prof(self.email, self.mdp, [], [], None, self.souhaite_alertes)
            if UserDao().exist_id(P):
                print("L'utilisateur existe déjà")
            else:
                UserDao().add_user(P)
