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
    """ 
    The Admin class inherits from the Prof class and has the same characteristics as a Prof,
    but also includes additional functions.
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
        """
        Initializes an instance of the Admin class.

        Args:
            email (str): The email address of the admin.
            mdp (str): The password of the admin.
            critere (str, optional): The search criteria of the admin. Defaults to None.
            code_insee_residence (str, optional): The residence code of the admin. Defaults to None.
            list_envie (list, optional): The list of preferences of the admin. Defaults to an empty list.
            souhaite_alertes (bool, optional): Indicates whether the admin wishes to receive alerts. Defaults to False.
        """
        super().__init__(
            critere=critere,
            list_envie=list_envie,
            email=email,
            mdp=mdp,
            souhaite_alertes=souhaite_alertes
        )

    @classmethod
    def charger_user(cls, email, mdp):
        """
        Loads an admin user from the database based on the provided email and password.

        Args:
            email (str): The email address of the admin.
            mdp (str): The password of the admin.

        Returns:
            Admin: An instance of the Admin class.

        Raises:
            Exception: If the email or password is incorrect.
            Exception: If the user is not an admin.
        """
        res = UserDao().charger_user(email, mdp)
        if res == False:
            print("Mauvais identifiants veuillez recommencer")
        elif "<class 'metier.admin.Admin'>" not in res["profil"]:
            print("Vous n'êtes pas un.e administrateur.e")
            res = False
        else :
            return Admin(
                email=res["email"],
                mdp=res["mdp"],
            )
        return(res)

    def chargerTout(self):
        """
        Retrieves the list of all users from the database.

        Returns:
            list: A list of email addresses of all users.
        """
        listDic = UserDao().tous()

        if len(listDic) == 0:
            return None

        listRes = []
        for res in listDic:
            email = res["email"]
            listRes.append(email)

        return listRes

    def supprime_user(self, unUser: Eleve):
        """
        Deletes a user from the database.

        Args:
            unUser (Eleve): An instance of the Eleve class representing the user to be deleted.
        """
        if unUser.existe():
            AssoStageUserDao().delete(unUser)
            UserDao().delete_user(unUser)
        else:
            print("The user {} is not registered".format(unUser.email))

    def envoi_mail(self, mail):
        """
        Sends an email to the specified recipient.

        Args:
            mail (str): The email address of the recipient.
        """
        message = input("Enter your message: ")
        sender = "stagefinderensai@outlook.com"

        email = EmailMessage()
        email["From"] = sender
        email["To"] = mail
        email["Subject"] = "Internmatch Administrator Mail"
        email.set_content(message)

        smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
        smtp.starttls()
        smtp.login(sender, "123456abc@@@")
        smtp.sendmail(sender, mail, email.as_string())
        smtp.quit()

    def envoi_mail_envie(self, mail, message):
        """
        Sends an email to the specified recipient with its prefered internship.

        Args:
            mail (str): The email address of the recipient.
        """
        sender = "stagefinderensai@outlook.com"

        email = EmailMessage()
        email["From"] = sender
        email["To"] = mail
        email["Subject"] = "InternMatch Liste d'envie"
        email.set_content(message)

        smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
        smtp.starttls()
        smtp.login(sender, "123456abc@@@")
        smtp.sendmail(sender, mail, email.as_string())
        smtp.quit()
