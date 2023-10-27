

from metier.eleve import Eleve
from metier.prof import Prof
from dao.userDao import UserDao

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