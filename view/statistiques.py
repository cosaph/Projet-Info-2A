# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    statistiques.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/10 09:52:23 by cosaph            #+#    #+#              #
#    Updated: 2023/11/10 10:28:02 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from metier.eleve import Eleve
from metier.prof import Prof
from dao.userDao import UserDao
from view.start_view import StartView

class statistiques(AbstractView):
    
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Hello {Session().user_name}",
                "choices": [
                    "Liste d'élève qui ont trouvé un stage",
                    "Retour"
                ],
            }
        ]

    def display_info(self):
        with open("graphical_assets/art_statistiques.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Retour":
            pass 
        if reponse["choix"] == "Liste d'élève qui ont trouvé un stage": 
            UserDao.tout_mail_stage_touve()
            from view.menu_post_connection_prof import post_connection_prof
            return post_connection_prof()