# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    start_view.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/25 11:57:13 by cosaph            #+#    #+#              #
#    Updated: 2023/10/25 16:45:45 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from InquirerPy import prompt

from view.abstract_view import *
from view.session import Session
from view.connection import ConnectionView


class StartView(AbstractView):

    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Hello {Session().user_name}",
                "choices": [
                    "Connection",
                    "Création Compte",
                    "Administrateur.e",
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
        if reponse["choix"] == "Connection": #pense a changer le if la.
            from view.connection import ConnectionView

            return ConnectionView()

        elif reponse["choix"] == "Création Compte":
            from view.creation_compte import Creation_compteView

            return Creation_compteView()
        
        elif reponse["choix"] == "Administrateur.e":
            from view.creation_compte import Creation_compteView

            return Creation_compteView()