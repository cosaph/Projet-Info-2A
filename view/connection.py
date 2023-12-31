# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    connection.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/25 11:58:22 by cosaph            #+#    #+#              #
#    Updated: 2023/11/21 11:51:40 by cosaph           ###   ########.fr        #
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
import view.shared_data as shared_data


class ConnectionView(AbstractView):
    
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "type",
                "message": "Vous êtes ",
                "choices": [
                    "élève",
                    "professeur.e",
                ]
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
        with open("graphical_assets/art_connection.txt", "r", encoding="utf-8") as asset:
            print(asset.read())


    def make_choice(self):
        answers = prompt(self.__questions)
        email = answers["email"]
        password = answers["password"]
        type = answers["type"]
        shared_data.tab_ter.append(type)
        shared_data.tab_type.append(type)

        if type == 'élève':
            if Eleve.charger_user(email, password):
                #print(Eleve.charger_user(email, password)
                shared_data.tab_bis.append(email)
                shared_data.tab_bis.append(password)
                #Session().user_name = email
                from view.menu_post_connection import post_connection
                return post_connection()
            else :
                from view.connection import ConnectionView
                return ConnectionView()
        
        elif type == 'professeur.e':
            if Prof.charger_user(email, password):
                #print(Prof.charger_user(email, password))
                shared_data.tab_bis.append(email)
                shared_data.tab_bis.append(password)
                #Session().user_name = email
                from view.menu_post_connection_prof import post_connection_prof

                return post_connection_prof()
            else :
                from view.connection import ConnectionView
                return ConnectionView()
        
        
        """
        elif type == 'administrateur.e':
            if Admin.charger_user(email, password):
                shared_data.tab_bis.append(email)
                shared_data.tab_bis.append(password)
                Session().user_name = "Bonjour Admin :)) " 
                from view.menu_post_connection_admin import post_connection_admin
                
                return post_connection_admin()
        """
        from view.start_view import StartView
        return StartView()

        
        