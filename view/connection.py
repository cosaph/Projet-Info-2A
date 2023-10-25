# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    connection.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/25 11:58:22 by cosaph            #+#    #+#              #
#    Updated: 2023/10/25 16:05:22 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from metier.eleve import Eleve
""" from metier.admin import Admin
from metier.prof import Prof """

class ConnectionView(AbstractView):
    
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

    def verif_existence(self, email, password):
        """Vérifie si l'utilisateur est présent dans la base de données en utilisant la DAO."""
        try:
            eleve = Eleve.charger_user(email, password)
            if eleve is not None:
                return True  # Utilisateur trouvé
            else:
                return False  # Utilisateur non trouvé
        except Exception as e:
            print(f"Erreur lors de la vérification : {str(e)}")
            return False  # Utilisateur non trouvé

    def make_choice(self):
        answers = prompt(self.__questions)
        email = answers["email"]
        password = answers["password"]

        if self.verif_existence(email, password):
            Session().user_name = email
            from view.start_view import StartView
            return StartView()
        else:
            print("L'utilisateur n'a pas été trouvé dans la base de données. Veuillez réessayer.")
            