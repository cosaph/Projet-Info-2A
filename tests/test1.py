from scr.critere import Critere
from scr.eleveNonAuthentifie import EleveNonAuthentifie
from scr.eleveAuthentifie import EleveAuthentifie
from scr.prof import Prof
from scr.admin import Admin
from scr.contactEmployeur import ContactEmployeur
from dao.critereDAO import CritereDAO
from dao.userDao import UserDao
from dao.db_connection import DBConnection
from utils.singleton import Singleton

if __name__ == "__main__":
    # Pour charger les variables d'environnement contenues dans le fichier .env
    import dotenv
    dotenv.load_dotenv(override=True)

    # Création d'une attaque et ajout en BDD
    unCritere = Critere(681, '47001', 'dataS', 3, 6)
    # print(unCritere)
    # succes1 = CritereDAO().add(unCritere)
    # print(succes1)
    deuxEleve = EleveAuthentifie(unCritere, "av@sdggd.com", "mdp", "33338", True)
    print(UserDao().exist_id(deuxEleve))
    print(deuxEleve)
    succes = UserDao().add_user(deuxEleve)
    print(succes)
    succes = UserDao().update_user(deuxEleve)
    print(succes)
    print(UserDao().exist_id(deuxEleve))
    succes = UserDao().delete_user(deuxEleve)
    print(succes)
    print(UserDao().exist_id(deuxEleve))