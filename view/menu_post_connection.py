

from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from metier.eleve import Eleve
from metier.prof import Prof
from dao.userDao import UserDao
from view.start_view import StartView



class post_connection(AbstractView):
    
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Hello {Session().user_name}",
                "choices": [
                    "Recherche de stage",
                    "Historique",
                    "Quit"
                ],
            }
        ]

    def display_info(self):
        with open("graphical_assets/banner.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quit":
            pass 
        #Ici l'utilisateur fait le choix de se connecter?
        if reponse["choix"] == "Recherche de stage": 
            from view.recherche import recherche

            return recherche()

        elif reponse["choix"] == "Historique":
            from view.historique import historique

            return historique()
        