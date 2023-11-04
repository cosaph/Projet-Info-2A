# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    connection.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/25 11:58:22 by cosaph            #+#    #+#              #
#    Updated: 2023/11/04 19:09:49 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from metier.eleve import Eleve
from metier.prof import Prof
from dao.userDao import UserDao
import view.shared_data as shared_data
from metier.admin import Admin

class ConnectionView(AbstractView):
    
    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "Type",
                "message": "Etes-vous un élève ou un professeur ou un Admin ? :"
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
                shared_data.tab_bis.append(email)
                shared_data.tab_bis.append(password)
                Session().user_name = email
                from view.menu_post_connection import post_connection

                return post_connection()
        
        elif type == 'Prof':
            if Prof.charger_user(email, password):
                shared_data.tab_bis.append(email)
                shared_data.tab_bis.append(password)
                Session().user_name = email
                from view.menu_post_connection_prof import post_connection_prof

                return post_connection_prof()

        elif type == 'Admin':
            if Admin.charger_user(email, password):
                shared_data.tab_bis.append(email)
                shared_data.tab_bis.append(password)
                Session().user_name = "Bonjour Admin :)) " 
                from view.menu_post_connection_admin import post_connection_admin

                return post_connection_admin()
        
        from view.start_view import StartView
        return StartView()

        
        