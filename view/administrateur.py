# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    administrateur.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/04 18:49:32 by cosaph            #+#    #+#              #
#    Updated: 2023/11/21 12:41:30 by cosaph           ###   ########.fr        #
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
from view.menu_post_connection_admin import post_connection_admin

class ConnectionView_admin(AbstractView):
    
    def __init__(self):
        self.__questions = [
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
        
        type = "Administrateur.e"
        if Admin.charger_user(email, password):
            shared_data.tab_ter.append(email)
            shared_data.tab_ter.append(password)
            shared_data.tab_ter.append(type)
            shared_data.tab_type.append(type)
            from view.menu_post_connection_admin import post_connection_admin

            return post_connection_admin()
        else :
            from view.administrateur import ConnectionView_admin
            return ConnectionView_admin()