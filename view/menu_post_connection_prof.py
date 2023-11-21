# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    menu_post_connection_prof.py                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/04 18:09:12 by cosaph            #+#    #+#              #
#    Updated: 2023/11/21 15:19:54 by cosaph           ###   ########.fr        #
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



class post_connection_prof(AbstractView):
    
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Hello :)",
                "choices": [
                    "Recherche de stage",
                    "liste d'envie",
                    "Statistiques",
                    "Historique de recherche",
                    "Modifier Compte",
                    "Quitter"
                ],
            }
        ]

    def display_info(self):
        with open("graphical_assets/art_menu.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quitter":
            pass
        #Ici l'utilisateur fait le choix de se connecter?
        if reponse["choix"] == "Recherche de stage": 
            from view.recherche import recherche

            return recherche()

        if reponse["choix"] == "liste d'envie":
            from view.listedenvie import listedenvie

            return listedenvie()
        
        if reponse["choix"] == "Statistiques":
            from view.statistiques import statistiques

            return statistiques()
        
        if reponse["choix"] == "Historique de recherche":
            from view.historique import historique

            return historique()
        if reponse["choix"] == "Modifier Compte":
            Prof(shared_data.tab_bis[0], shared_data.tab_bis[1]).modifier()
            print("Votre compte a bien été modifié")
            return post_connection_prof()