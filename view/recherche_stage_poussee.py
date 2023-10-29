# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recherche_stage_poussee.py                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/29 20:21:41 by marvin            #+#    #+#              #
#    Updated: 2023/10/29 20:21:41 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from InquirerPy import prompt

from view.abstract_view import AbstractView


class recherche_stage_poussee(AbstractView):
    
    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "add_list",
                "message": "Voulez-vous ajouter ce stage dans votre liste d'envie ? :"
            },
            {
                "type": "input",
                "name": "voir_plus",
                "message": "En savoir plus sur le stage ?(en cours de construction)",
            },
        ]
    
    def display_info(self):
        print(f"Bonjour, veuillez choisir parmis les informations suivantes:")


    def make_choice(self):
        answers = prompt(self.__questions)
        add_list = answers["add_list"]
        voir_plus = answers["voir_plus"]
        type = answers["Type"]

        
        