from metier.prof import Prof
from metier.eleve import Eleve
from metier.critere import Critere
from metier.stage import Stage
from dao.userDao import UserDao
from metier.listEnvie import ListEnvie
from dao.assoCritUserDAO import AssoCritUserDao
from dao.assoStageUserDao import AssoStageUserDao

from email.message import EmailMessage
import smtplib


class Admin(Prof):
    """ Un Admin hérite de la classe Prof 
    il a les même varactéristique qu'un Prof et dispose de fonctions
    supplémentaires
    """
    def __init__(
        self,
        email,
        mdp,
        critere=None,
        code_insee_residence=None,
        list_envie=[],
        souhaite_alertes=False
            ):
        super().__init__(
            critere=critere,
            list_envie=list_envie,
            email=email,
            mdp=mdp,
            code_insee_residence=code_insee_residence,
            souhaite_alertes=souhaite_alertes
            )
    
    @classmethod
    def charger_user(self, email, mdp):
        res = UserDao().charger_user(email, mdp)
        if not res:
            raise "email ou mdp incorrect"
        if "Admin" not in res["profil"]:
            raise "L'utilisateur n'est pas un administrateur"
        return Admin(
                    email=res["email"],
                    mdp=res["mdp"],
                    critere=None,
                    list_envie=None,
                    code_insee_residence=res["code_insee_residence"],
                    souhaite_alertes=res["souhaite_alertes"]
                    )

    
    def chargerTout(self):
        listDic = UserDao().tous()

        if len(listDic) == 0:
            return None
    
        listRes = []
        for res in listDic:
            email = res["email"]
            #url_stage = res["url_stage"]
            listRes.append(email)
    
        return (listRes)
    

    def supprime_user(self, unUser: Eleve):
        if unUser.existe():
            AssoStageUserDao().delete(unUser) 
            UserDao().delete_user(unUser)
                
        else:
            print("L' utilisateur {} n'est pas enregistré".format(unUser.email))


    def envoi_mail(self, mail):

        message = input("Entrez votre message : ")
        sender = "stagefinderensai@outlook.com"

        email = EmailMessage()
        email["From"] = sender
        email["To"] = mail
        email["Subject"] = "Mail administrateur StageFinder"
        email.set_content(message)

        smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
        smtp.starttls()
        smtp.login(sender, "123456abc@@@")
        smtp.sendmail(sender, mail, email.as_string())
        smtp.quit()
