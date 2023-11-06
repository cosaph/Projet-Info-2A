# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recherche.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/28 19:53:45 by marvin            #+#    #+#              #
#    Updated: 2023/11/06 09:33:43 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from view.abstract_view import AbstractView

from InquirerPy import prompt
from metier.critere import Critere
from view.selected_item_view  import selected_item_view
from metier.stage import Stage
import view.shared_data as shared_data

class recherche(AbstractView):

    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "critère",
                "message": "Entrez le type de stage que vous recherchez : :"
            },
            {
                "type": "input",
                "name": "localisation",
                "message": "Dans quelle localité ? ",
            },
            {
                "type": "input", # voir s'il existe pas un type pour les int sinon renvoie une erreur.
                "name": "rayon",
                "message": "Dans un rayon de combien de kilomètres ?",
            }
        ]

    def display_info(self):
        print(f"Bonjour, veuillez rentrer les informations suivantes:")


    def make_choice(self):
        answers = prompt(self.__questions)
        critere = answers["critère"]
        localisation = answers["localisation"]
        rayon = answers["rayon"]
        tableau = Critere.recherche_stage(critere, localisation, rayon)

        options = [
            {
                "type": "list",
                "name": "selected_items",
                "message": "Select items:",
                "choices": [
                    {
                        "name": f"{item['title']} - {item['location']} ({item['url']}) ",
                        "value": item,
                    }
                    for item in tableau
                    
                ],
            }
            
        ]
        
        response = prompt(options)
        selected = response["selected_items"]
        
        needs = []
        needs.append(critere)
        needs.append(rayon)
        needs.append(localisation)
        shared_data.tab = needs
        
        return selected_item_view(selected)