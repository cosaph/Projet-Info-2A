

from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from metier.eleve import Eleve
from metier.prof import Prof
from dao.userDao import UserDao
from view.start_view import StartView
import view.shared_data as shared_data



class post_connection(AbstractView):
    
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Hello :)",
                "choices": [
                    "Recherche de stage",
                    "Liste d'envie",
                    "Historique de recherche par critère",
                    "Questionnaire",
                    "Modifier compte",
                    "Quitter"
                ],
            }
        ]

    def display_info(self):
        with open("graphical_assets/art_recherche.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quitter":
            pass
        #Ici l'utilisateur fait le choix de se connecter?
        if reponse["choix"] == "Recherche de stage": 
            from view.recherche import recherche

            return recherche()

        elif reponse["choix"] == "Liste d'envie":
            from view.listedenvie import listedenvie

            return listedenvie()
        
        elif reponse["choix"] == "Historique de recherche par critère":
            from view.historique import historique

            return historique()
        
        elif reponse["choix"] == "Questionnaire":
            from view.questionnaire import questionnaire

            return questionnaire()
        
        elif reponse["choix"] == "Modifier compte":
            Eleve(shared_data.tab_bis[0], shared_data.tab_bis[1]).modifier()
            print("Votre compte a bien été modifié")
            return post_connection()
            
        