# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    probleme.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/10 15:08:31 by cosaph            #+#    #+#              #
#    Updated: 2023/11/19 14:14:59 by cosaph           ###   ########.fr        #
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


class probleme(AbstractView):

    def __init__(self) :
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Hello Admin :)",
                "choices": [
                    "Envoyer un mail",
                    "Retour"
                ],
            }
        ]

    def display_info(self):
        with open("graphical_assets/art_recherche.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Retour":
            from view.menu_post_connection_admin import post_connection_admin
            return post_connection_admin()
        #Ici l'utilisateur fait le choix de se connecter?
        elif reponse["choix"] == "Envoyer un mail": 

            # il faut charger une liste d'user
            tableau = Admin(shared_data.tab_ter[0], shared_data.tab_ter[1]).chargerTout()
            print(tableau)
            options = [
                {
                    "type": "list",
                    "name": "email",
                    "message": "Select items:",
                    "choices": 
                    [
                        {
                            "name": f"{email}",
                            "value": email,
                        }
                        for email in tableau
                    
                    ],
                }
            ]
            res = prompt(options)

            selected = res["email"]
            # verifer que l'utilisateur veut bien se faire id.
            Admin(shared_data.tab_ter[0], shared_data.tab_ter[1]).envoi_mail(selected)
            print("Mail envoyé")
            from view.menu_post_connection_admin import post_connection_admin
            return post_connection_admin()



