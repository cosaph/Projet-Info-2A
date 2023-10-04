from metier.critere import Critere
from metier.userNonAuthentifie import UserNonAuthentifie
from metier.eleve import Eleve
from metier.prof import Prof
from metier.admin import Admin
from metier.contactEmployeur import ContactEmployeur
from dao.critereDAO import CritereDAO
from dao.userDao import UserDao
from dao.db_connection import DBConnection
from utils.singleton import Singleton
from datetime import datetime
#pip install python-dotenv
import dotenv


if __name__ == "__main__":
    dotenv.load_dotenv(override=True)
    
    unCritere = Critere("Rennes", 50, "sport", 3, 6)
    unAdmin = Admin(unCritere, "rwarnod@yahoo.fr", "lalala", "35034", True)
    print(unAdmin)
    unAdmin.enregistrer()

    deuxCritere = Critere("Rennes", 50, "lalalal", 3, 6)
    unProf = Prof(deuxCritere, "prof@yahoo.fr", "lalala", "35034", True)
    print(unProf)
    unProf.enregistrer()
    test = UserDao().charger_all_user()
    print(test)

    test2 = CritereDAO().charger_all_critere()
    print(test2)

    test3 = CritereDAO().charger_critere(1)
    print(test3)

    print(datetime.now())

    # unUser = UserDao().charger_user("av@sdggd.com", "mdp")
    # print(unUser)()
    # unCritere = Critere('35000', 10, 'lalalal', 3, 6)
    # #print(unCritere)
    # deuxEleve = Eleve(unCritere, "fffssgd@tatat.com", "mrp", "111138", True)
    # #print(UserDao().exist_id(deuxEleve))
    # #print(deuxEleve)
    # #succes = UserDao().add_user(deuxEleve)

    # # print(CritereDAO().exist_id(unCritere))
    # # #succes1 = CritereDAO().add(unCritere)
    
    # deuxCritere = Critere('75000', 2000, 'lal', 3, 6)
    # troisEleve = Eleve(deuxCritere, "avee@sdggd.com", "mrdp", "118", True)
    # print(UserDao().exist_id(deuxEleve))
    
    # #succes = UserDao().add_user(troisEleve)
    # # #print(succes)

    # succes = UserDao().update_user(troisEleve)
    # print(succes)

    # troisUser = Eleve.charger_user("avee@sdggd.com", "mrdp")
    # print(troisUser)

    # # print(UserDao().exist_id(deuxEleve))
    # # succes = UserDao().delete_user(deuxEleve)
    # print(succes)
    # print(UserDao().exist_id(deuxEleve))


    