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
#pip install python-dotenv
import dotenv


if __name__ == "__main__":
    dotenv.load_dotenv(override=True)
    unUser = UserDao().charger_user("av@sdggd.com", "mdp")
    print(unUser)
    # unCritere = Critere('00001', 'dataS', 3, 6)
    # print(unCritere)
    # print(CritereDAO().exist_id(unCritere))
    # #succes1 = CritereDAO().add(unCritere)
    # # print(succes1)
    # deuxEleve = EleveAuthentifie(unCritere, "aveeeee@sdggd.com", "mrdp", "111138", True)
    # print(UserDao().exist_id(deuxEleve))
    # print(deuxEleve)
    # #succes = UserDao().add_user(deuxEleve)
    # #print(succes)
    # succes = UserDao().update_user(deuxEleve)
    # print(succes)
    # # print(UserDao().exist_id(deuxEleve))
    # # succes = UserDao().delete_user(deuxEleve)
    # print(succes)
    # print(UserDao().exist_id(deuxEleve))