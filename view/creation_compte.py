# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    creation_compte.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/25 11:58:35 by cosaph            #+#    #+#              #
#    Updated: 2023/10/26 12:27:20 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from dao.userDao import *

class Creation_compteView(AbstractView):


    def __init__(self):
        self.__questions = [
            {
                "type": "input",
                "name": "email",
                "message": "Quel est votre email ?",
            },
            {
                "type": "input",  # Utilisez "password" pour masquer la saisie du mot de passe
                "name": "password",
                "message": "Choisissez un mot de passe :",
            },
            {
                "type": "input",  # Utilisez "password" pour masquer la saisie du mot de passe
                "name": "alerte",
                "message": "souhaites-tu être alerté? (oui/non)",
            }
        ]



    def display_info(self):
        print(f"Hello, please enter your email and your password.")
    

    def make_choice(self):
        answers = prompt(self.__questions)
        Session().user_name = answers["email"]
        email = answers["email"]
        password = answers["password"]
        alerte = answers["alerte"]

        UserDao.add_user(email, password, alerte)
        # Ici, vous pouvez enregistrer ces informations dans votre application pour la création de compte.
        # Vous pouvez utiliser email et password pour créer un compte utilisateur dans votre système.

        from view.start_view import StartView
        return StartView()
