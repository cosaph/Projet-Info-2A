# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    historique.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/02 21:11:41 by cosaph            #+#    #+#              #
#    Updated: 2023/11/02 23:54:39 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from view.abstract_view import AbstractView
from InquirerPy import prompt
from metier.stage import Stage
from dao.stageDAO import StageDao

class listedenvie(AbstractView):
    
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": "liste d'envie",
                "choices": [
                    "Consulter la liste d'envie",
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
            from view.menu_post_connection import post_connection
            return post_connection()
        
        elif reponse["choix"] == "Consulter la liste d'envie":
            RealDictRow = StageDao().charger_stage()
            print(RealDictRow)
            
