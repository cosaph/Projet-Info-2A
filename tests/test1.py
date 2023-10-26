from metier.stage import Stage
from metier.critere import Critere
from metier.userNonAuthentifie import UserNonAuthentifie
from metier.eleve import Eleve
from metier.prof import Prof
from metier.admin import Admin
from metier.contactEmployeur import ContactEmployeur
from dao.critereDAO import CritereDAO
from dao.userDao import UserDao
from dao.assoCritUserDAO import AssoCritUserDao
from dao.db_connection import DBConnection
from utils.singleton import Singleton
from dao.assoStageUserDao import AssoStageUserDao
from dao.stageDAO import StageDao
from view.connection import ConnectionView
# pip install python-dotenv
import dotenv


if __name__ == "__main__":
    dotenv.load_dotenv(override=True)
    # test admin
    # print(ConnectionView().verif_existence("zozo@yahoo.fr", "lalala"))
    # eleve = Eleve.charger_user(email, password)
    # unCrit = Critere("Paris", 500, "danse", 3, 6)
    # res = UserNonAuthentifie(unCrit).rechercher_stage()
    # unAdmin = Admin.charger_user("rwarnod@yahoo.fr", "lalala")
    # res = unAdmin.rechercher_stage(unCrit, verbose=True)
    # unAdmin.ajouter_stageAuser(res[1])

    # unAdmin.supprimer_stageAuser(res[1])
    # print(unAdmin)

    # unUser = unAdmin.chargerUnAutreUser("eleve1@yahoo.fr")
    # print(unUser)

    # deuxAdmin = Admin(email="admin12@yahoo.fr", mdp="0000")
    # unAdmin.ajouter_user(deuxAdmin)
    # trois = unAdmin.chargerUnAutreUser("admin12@yahoo.fr")
    # print(trois)

    # unAdmin = Admin.charger_user("admin12@yahoo.fr", "0000")
    # res = unAdmin.rechercher_stage(unCrit, verbose=False)
    # # unAdmin.ajouter_stageAuser(res[1])
    # print(unAdmin.list_envie)
    # print(StageDao().exist_id(res[1]))
    # unStage = Stage.charger_stage(res[1].url_stage)
    # print(unStage)

    # print(unAdmin.list_envie)

    # unAdmin = Admin.charger_user(email="jfjfjfj", mdp="lalal")

    # Test eleve

    # unEleve = Eleve.charger_user("zozo@yahoo.fr", "lalala")
    # unCrit = Critere("Rennes", 100, "statistiques", 3, 6)
    # res = unEleve.rechercher_stage(unCrit, verbose=False)
    # # print(unEleve.list_envie)
    # unEleve.ajouter_stageAuser(res[0])
    # unEleve.ajouter_stageAuser(res[2])
    # unEleve.supprimer_stageAuser(res[0])
    # unEleve.supprimer_stageAuser(res[2])
    # print(unEleve.list_envie)

    unAdmin = Admin.charger_user("rwarnod@yahoo.fr", "lalala")
    luser = unAdmin.chargerToutLemonde()
    print(luser[1])


    # lesCrit = unAdmin.charger_all_critere(verbose=True)

    

    # trCritere = Critere("Pino", 100, "dddeg", 1, 2)
    # deuxAdmin = Admin(email="jfjfjfj", mdp="lalal", critere=trCritere)
    # deuxAdmin.enregistrer()
    # unAdmin = Admin.charger_user(email="jfjfjfj", mdp="lalal")
    # print(unAdmin)
   
    # Admin(email="rwarnod@yahoo.fr", mdp="lalala",code_insee_residence="0217").modifier()
    # unAdmin = Admin.charger_user("rwarnod@yahoo.fr", "lalala")
    # lesCrit = unAdmin.charger_all_critere()
    # for k in lesCrit:
    #     print(k)
    # print(unAdmin)

    # trCritere = Critere("Pino", 100, "aaaaaddd", 1, 2)
    # unAdmin.modifier_user(Admin(email="admin222@yahoo.fr", mdp="mdp", code_insee_residence="35034", critere= trCritere))
    # deuxAdmin = Admin.charger_user("admin222@yahoo.fr", "mdp")
    # print(deuxAdmin)

    # unEleve = Eleve(email="zozo@yahoo.fr", mdp="lalala")
    # unEleve.enregistrer()
    # unEleve = Eleve.charger_user("zozo@yahoo.fr", "lalala")
    # trCritere = Critere("Paris", 100, "foot", 2, 4)
    # unEleve.ajouter_critereAuser(trCritere)
    # print(unEleve)

    # unUser = Prof.charger_user("prof@yahoo.fr", "lalala")
    # print(unAdmin)
    # unCritere = Critere("Rennes", 50, "sport", 3, 6)
    # unAdmin.enregistrer()
    # trCritere = Critere("Pino", 50, "geggdddeg", 1, 2)
    # print(trCritere)
    # print(unUser.supprimer_critereAuser(trCritere.id_crit))
    # print(unUser.ajouter_critereAuser(trCritere))
    # deuxAdmin = Admin(email="jfjfjfj", mdp="lalal", critere=trCritere)
    # print(deuxAdmin)
    # zozo = []
    # zozo.append(trCritere)
    # for k in zozo:
    #     print(k)

    # print(deuxAdmin.critere)
    # print(deuxAdmin)
    # unAdmin.ajouter_user(deuxAdmin)
    # unAdmin.ajouter_user(Prof(email="prof222@yahoo.fr", mdp="mdp"))

    # res = AssoCritUserDao().unUser_all_id_crit(unAdmin)
    
    # unCrit = Critere.charger_critere(res[0]["id_crit"])
    # print(unCrit)
    
    # print(unCrit)
    # print(res)
    # listCritere = []
    # for k in res:
    #     print(k["id_crit"])
    #     listCritere.append(Critere.charger_critere(k["id_crit"]))
    
    # print(listCritere[3])

    # listCritere = unAdmin.charger_all_critere()
    # print(listCritere[2])

    # listCritere = Eleve.charger_all_critere_mail("rwarnod@yahoo.fr")
    # print(listCritere[2])

    # print(res[0]["id_crit"])

    # deuxCritere = Critere("Rennes", 50, "lalalal", 3, 6)
    # unProf = Prof(deuxCritere, "prof@yahoo.fr", "lalala", "35034", True)
    # print(unProf)
    # unProf.enregistrer()

    # unEleve = Eleve(deuxCritere, "eleve1@yahoo.fr", "lalala", "47054", False)
    # unEleve.enregistrer()
    
    # troisCritere = Critere("Paris", 50, "lololo", 3, 6)
    # douzeEleve = Eleve(troisCritere, "eleve1@yahoo.fr", "lalala", "47054", False)

    # douzeEleve.enregistrer()

    # unEleve = Eleve(troisCritere, "eleve1@yahoo.fr", "lalala", "47054", False)
    # unEleve.enregistrer()

    # print( troisCritere == troisCritere)





    # test = UserDao().charger_all_user()
    # print(test)

    # test2 = CritereDAO().charger_all_critere()
    # print(test2)

    # test3 = CritereDAO().charger_critere(1)
    # print(test3)

    # print(datetime.now())

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


    