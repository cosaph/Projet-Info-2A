# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    questionnaire.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/09 21:10:34 by cosaph            #+#    #+#              #
#    Updated: 2023/11/09 21:30:03 by cosaph           ###   ########.fr        #
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

class questionnaire(AbstractView):

    def __init__(self):
        self.__questions = [
            {
                "type": "list",  
                "name": "alerte",
                "message": "As-tu trouvé un stage grâce a notre application ?(oui/non)",
                "choices": [
                    "TRUE",
                    "FALSE"
                ]
            }
        ]
       
    
    def display_info(self):
        print(f"Bonjour, veuillez répondre aux informations suivantes:")

    def make_choice(self):
        answers = prompt(self.__questions)
        alerte = answers["alerte"]
        if alerte == "TRUE":
            print("Merci d'avoir utilisé notre application")
            Eleve(shared_data.tab_bis[0], shared_data.tab_bis[1]).set_stage_trouve(alerte)
        else:
            print("Nous sommes désolés que notre application n'ait pas pu vous aider")
                    