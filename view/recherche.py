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
                "name": "Type",
                "message": "Etes-vous un élève ou un professeur ? :"
            },
            {
                "type": "input",
                "name": "email",
                "message": "Rentrez votre email :",
            },
            {
                "type": "password",
                "name": "password",
                "message": "Rentrez votre mot de passe :",
            }
        ]
