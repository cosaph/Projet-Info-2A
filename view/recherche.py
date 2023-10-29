# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recherche.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: marvin <marvin@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/28 19:53:45 by marvin            #+#    #+#              #
#    Updated: 2023/10/28 19:53:45 by marvin           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from view.abstract_view import AbstractView

from InquirerPy import prompt
from metier.critere import Critere

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
     
        Critere.recherche_stage(critere, localisation, rayon)