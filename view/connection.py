# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    connection.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/25 11:58:22 by cosaph            #+#    #+#              #
#    Updated: 2023/10/25 16:36:12 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from metier.eleve import Eleve
from metier.prof import Prof
from dao.userDao import UserDao

class ConnectionView(AbstractView):
    
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
    
    def display_info(self):
        print(f"Bonjour, veuillez rentrer les informations suivantes:")


    def make_choice(self):
        answers = prompt(self.__questions)
        email = answers["email"]
        password = answers["password"]
        type = answers["Type"]

        if type == 'Elève':
            if Eleve.charger_user(email, password):
                Session().user_name = email
        
        elif type == 'Prof':
            P = Prof(email, password)
            if UserDao().charger_user(P):
                Session().user_name = email

        from view.menu_post_connection import recherche

        return recherche()
        