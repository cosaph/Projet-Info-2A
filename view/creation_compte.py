# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    creation_compte.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/25 11:58:35 by cosaph            #+#    #+#              #
#    Updated: 2023/11/07 14:15:51 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
#from metier.userNonAuthentifie import UserNonAuthentifie
from metier.nouveau_compte import Creation
import view.shared_data as shared_data

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
                "type": "input",  # Utilisez "confirm" pour obtenir "oui" ou "non"
                "name": "code postal",
                "message": "donnes nous ton code postal:",
            },
            {
                "type": "input",  # Utilisez "confirm" pour obtenir "oui" ou "non"
                "name": "alerte",
                "message": "Souhaites-tu être alerté? (TRUE/FALSE)",
            },
            {
                "type": "input",  # Utilisez "confirm" pour obtenir "oui" ou "non"
                "name": "type",
                "message": "eleve ou prof",
            }
        ]

    def display_info(self):
        print(f"Bonjour, veuillez rentrer un email et un mot de passe :")

  

    def make_choice(self):
        answers = prompt(self.__questions)
        Session().user_name = answers["email"]
        email = answers["email"]
        code_insee_residence = answers["code postal"]
        password = answers["password"]
        alerte = answers["alerte"]
        type = answers["type"]

        if Creation(password, email, alerte, code_insee_residence, type).creer_compte():
            print("utilisateur crée")
        print("utilisateur pas crée")

        # Ici, vous pouvez enregistrer ces informations dans votre application pour la création de compte.
        # Vous pouvez utiliser email et password pour créer un compte utilisateur dans votre système.

        if type == 'eleve':
            shared_data.tab_bis.append(email)
            shared_data.tab_bis.append(password)
            from view.menu_post_connection import post_connection
            return post_connection()
        else :
            shared_data.tab_bis.append(email)
            shared_data.tab_bis.append(password)
            from view.menu_post_connection_prof import post_connection_prof
            return post_connection_prof()
    