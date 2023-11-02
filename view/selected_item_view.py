# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    selected_item_view.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/02 15:11:45 by cosaph            #+#    #+#              #
#    Updated: 2023/11/02 17:30:03 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from InquirerPy import prompt

from view.abstract_view import AbstractView
from metier.stage import Stage
from metier.critere import Critere



class selected_item_view(AbstractView):
    
    def __init__(self, selected):
        self.selected = selected
        self.__questions = [
            {
                "type": "list",
                "name": "choice",
                "message": "Que voulez-vous faire ?",
                "choices": ["Ajouter à la liste d'envie", "En savoir plus sur le stage"]
            }
        ]

    def display_info(self):
        print(f"Bonjour, veuillez choisir parmi les informations suivantes:")

    def make_choice(self):
        answers = prompt(self.__questions)
        choice = answers["choice"]

        if choice == "Ajouter à la liste d'envie":
            print(self.selected)
            #Stage.enregistrer_stage(self.selected)

                # Do something with the url, title, and location
        elif choice == "En savoir plus sur le stage":
            pass  # Do something else
             
        


             
        