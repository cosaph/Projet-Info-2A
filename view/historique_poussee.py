# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    historique_poussee.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/07 12:41:38 by cosaph            #+#    #+#              #
#    Updated: 2023/11/07 14:20:43 by cosaph           ###   ########.fr        #
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


class historique_poussee(AbstractView):

    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "critere",
                "message": "Rentrez votre critere :",
            }
        ]

    def display_info(self):
        with open("graphical_assets/art_connection.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        response = prompt(self.__questions)
        liste = Eleve.charger_all_stage_mail_critere(shared_data.tab_bis[0], response["critere"])
        print(liste)
