# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    listedenvie.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/02 21:11:41 by cosaph            #+#    #+#              #
#    Updated: 2023/11/07 20:24:02 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from view.abstract_view import AbstractView
from InquirerPy import prompt
from metier.stage import Stage
from dao.stageDAO import StageDao
from view.session import Session
from metier.eleve import Eleve
import view.shared_data as shared_data
from metier.critere import Critere



class listedenvie(AbstractView):
    
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": "liste d'envie",
                "choices": [
                    "Consulter la liste d'envie",
                    "Exporter la liste d'envie",
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
            RealDictRow = Eleve(shared_data.tab_bis[0], shared_data.tab_bis[1]).charger_all_stage_mail(shared_data.tab_bis[0])
            return self.make_choice()
        
        elif reponse["choix"] == "Exporter la liste d'envie":
            Eleve(shared_data.tab_bis[0], shared_data.tab_bis[1]).charger_all_stage_mail_csv(shared_data.tab_bis[0])
            
            return self.make_choice()
