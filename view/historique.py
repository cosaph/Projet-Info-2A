# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    historique.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/07 12:34:41 by cosaph            #+#    #+#              #
#    Updated: 2023/11/21 17:44:51 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from metier.eleve import Eleve
from metier.prof import Prof
from dao.userDao import UserDao
from view.start_view import StartView
import view.shared_data as shared_data

class historique(AbstractView):
    
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Hello :) }",
                "choices": [
                    "Consulter l'historique de recherche",
                    "Retour"
                ],
            }
        ]

    def display_info(self):
        with open("graphical_assets/art_historique.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Retour":
            if shared_data.tab_ter[0] == 'élève':
                from view.menu_post_connection import post_connection
                return post_connection()
            else:
                from view.menu_post_connection_prof import post_connection_prof
                return post_connection_prof()
        #Ici l'utilisateur fait le choix de se connecter?
        if reponse["choix"] == "Consulter l'historique de recherche":
            from view.historique_poussee import historique_poussee
            return historique_poussee()