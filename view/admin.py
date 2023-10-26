# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    admin.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/26 12:40:36 by cosaph            #+#    #+#              #
#    Updated: 2023/10/26 14:21:08 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from dao.userDao import *
from metier.admin import Admin

class AdminView(AbstractView):
    
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
        print(f"Hello, please enter your email and your password.")
    
    def crea_role_prof(self, email, mdp):
        answers = prompt(self.__questions)
        Session().user_name = answers["email"]
        email = answers["email"]
        password = answers["password"]
        role = answers["prof"]

        UserDao.add_user(email, password, role)