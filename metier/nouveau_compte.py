

from metier.eleve import Eleve
from metier.prof import Prof
from dao.userDao import UserDao
from dao.stageDAO import StageDao
from metier.stage import Stage

class creation:

    def creer_compte(mdp, email, souhaite_alertes, code_insee_residence, type):
        # Vérifiez si l'utilisateur existe déjà
        # if UserDao().exist_id(id):
        #     raise Exception("L'utilisateur a déjà un compte")
        
        # Chiffrez le mot de passe
        if type == 'eleve':
            E = Eleve(email, mdp, [], [], code_insee_residence, souhaite_alertes)
            if UserDao().exist_id(E):
                print("L'utilisateur existe déjà")
            UserDao().add_user(E)
        else:
            P = Prof(email, mdp, [], [], code_insee_residence, souhaite_alertes)
            if UserDao().exist_id(P):
                print("L'utilisateur existe déjà")
            UserDao().add_user(P)

    
    def creer_stage(url_stage, titre, specialite, ville):
        S = Stage(url_stage, titre, specialite, ville)
        if StageDao().exist_id(S):
            print("Le stage existe déjà")
        StageDao().add(S)