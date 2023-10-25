# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    connection.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/25 11:58:22 by cosaph            #+#    #+#              #
#    Updated: 2023/10/25 11:58:24 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session


class ConnectionView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "pseudo",
                "message": "What's your pseudo",
            }
        ]

    def display_info(self):
        print(f"Hello, please choose your pseudo")

    def make_choice(self):
        answers = prompt(self.__questions)
        Session().user_name = answers["pseudo"]

        from view.start_view import StartView

        return StartView()
