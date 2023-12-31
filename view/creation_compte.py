# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    creation_compte.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/25 11:58:35 by cosaph            #+#    #+#              #
#    Updated: 2023/11/21 15:16:23 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from metier.userNonAuthentifie import UserNonAuthentifie
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
                "type": "password",  
                "name": "password",
                "message": "Choisissez un mot de passe :",
            },
            {
                "type": "list",  
                "name": "alerte",
                "message": "Souhaites-tu être alerté? (oui/non)",
                "choices": [
                    "TRUE",
                    "FALSE"
                ]
            },
            {
                "type": "list",
                "name": "type",
                "message": "Vous êtes :",
                "choices": [
                    "élève",
                    "professeur.e"
                ]
            },
        ]

    def display_info(self):
        print(f"Bonjour, veuillez rentrer un email et un mot de passe :")

  

    def make_choice(self):
        answers = prompt(self.__questions)
        #Session().user_name = answers["email"]
        email = answers["email"]
        #code_insee_residence = answers["code postal"]
        password = answers["password"]
        alerte = answers["alerte"]
        type = answers["type"]
        
        if Creation(password, email, alerte, type).creer_compte():
            print("utilisateur crée")

        # Ici, vous pouvez enregistrer ces informations dans votre application pour la création de compte.
        # Vous pouvez utiliser email et password pour créer un compte utilisateur dans votre système.

        if type == 'élève':
            shared_data.tab_bis.append(email)
            shared_data.tab_bis.append(password)
    
            from view.start_view import StartView
            return StartView()
        else :
            shared_data.tab_bis.append(email)
            shared_data.tab_bis.append(password)
            from view.start_view import StartView
            return StartView()
    