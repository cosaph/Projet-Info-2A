# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    menu_post_connection_admin.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/04 19:06:07 by cosaph            #+#    #+#              #
#    Updated: 2023/11/13 15:58:31 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from metier.eleve import Eleve
from metier.prof import Prof
from dao.userDao import UserDao
from view.start_view import StartView
from metier.admin import Admin
import view.shared_data as shared_data



class post_connection_admin(AbstractView):
    
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Hello Admin :)",
                "choices": [
                    "Utilisateurs.es",
                    "Statistiques",
                    "Envoyer un mail à un.e élève",
                    "Retour"
                ],
            }
        ]

    def display_info(self):
        with open("graphical_assets/art_admin.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Retour":
            from view.start_view import StartView
            return StartView()

        if reponse["choix"] == "Utilisateurs.es": 
            from view.modifier_utilisateur import modifier_utilisateur
            return modifier_utilisateur()

        elif reponse["choix"] == "Statistiques":
            from view.statistiques import statistiques
            return statistiques()

        elif reponse["choix"] == "Envoyer un mail à un.e élève":
            from view.probleme import probleme
            return probleme()


"""
    def crea_role_prof(self, email, mdp):
        answers = prompt(self.__questions)
        Session().user_name = answers["email"]
        email = answers["email"]
        password = answers["password"]
        type = answers["prof"]
        alerte = answers["alerte"]

        UserNonAuthentifie.creer_compte(email, password, alerte, type)
"""
        