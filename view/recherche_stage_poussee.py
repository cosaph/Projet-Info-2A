# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recherche_stage_poussee.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/29 20:21:41 by marvin            #+#    #+#              #
#    Updated: 2023/11/01 23:06:09 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from InquirerPy import prompt

from view.abstract_view import AbstractView
from metier.stage import Stage
from metier.critere import Critere
import view.shared_data as shared_data


class recherche_stage_poussee(AbstractView):
    
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choice",
                "message": "Que voulez-vous faire ?",
                "choices": ["Ajouter à la liste d'envie", "En savoir plus sur le stage"]
            }
        ]
    
    def display_info(self):
        print(f"Bonjour, veuillez choisir parmis les informations suivantes:")


    def make_choice(self):
        answers = prompt(self.__questions)
        choice = answers["choice"]

        if choice == "Ajouter à la liste d'envie":
            print(shared_data.tableau)          
            pass
        elif choice == "En savoir plus sur le stage":
            # Code for learning more about the internship
            pass   

             
        