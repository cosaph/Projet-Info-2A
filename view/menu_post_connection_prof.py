# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    menu_post_connection_prof.py                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/04 18:09:12 by cosaph            #+#    #+#              #
#    Updated: 2023/11/04 18:46:08 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from metier.eleve import Eleve
from metier.prof import Prof
from dao.userDao import UserDao
from view.start_view import StartView



class post_connection_prof(AbstractView):
    
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Hello {Session().user_name}",
                "choices": [
                    "Recherche de stage",
                    "liste d'envie",
                    "Statistiques"
                    "Retour"
                ],
            }
        ]

    def display_info(self):
        with open("graphical_assets/banner.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Retour":
            pass 
        #Ici l'utilisateur fait le choix de se connecter?
        if reponse["choix"] == "Recherche de stage": 
            from view.recherche import recherche

            return recherche()

        elif reponse["choix"] == "liste d'envie":
            from view.listedenvie import listedenvie

            return listedenvie()
        
        elif reponse["choix"] == "Statistiques":
            pass
            """ from view.statistiques import statistiques

            return statistiques() """