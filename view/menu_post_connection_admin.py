# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    menu_post_connection_admin.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/04 19:06:07 by cosaph            #+#    #+#              #
#    Updated: 2023/11/04 20:00:04 by cosaph           ###   ########.fr        #
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



class post_connection_admin(AbstractView):
    
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Hello Admin :)",
                "choices": [
                    "Modifier utilisateurs.es",
                    "Statistiques",
                    "Quit"
                ],
            }
        ]

    def display_info(self):
        with open("graphical_assets/art_admin.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quit":
            pass 
        #Ici l'utilisateur fait le choix de se connecter?
        if reponse["choix"] == "Modifier utilisateurs.es": 
            pass

        elif reponse["choix"] == "Statistiques":
            pass
        