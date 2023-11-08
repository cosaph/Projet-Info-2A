# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    modifier_utilisateur.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/08 09:03:12 by cosaph            #+#    #+#              #
#    Updated: 2023/11/08 09:55:32 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from metier.eleve import Eleve
from metier.prof import Prof
from dao.userDao import UserDao
from view.start_view import StartView
from metier.admin import Admin
import view.shared_data as shared_data

class modifier_utilisateur(AbstractView):
        
        def __init__(self):
            self.__questions = [
                {
                    "type": "list",
                    "name": "choix",
                    "message": f"Hello Admin :)",
                    "choices": [
                        "Chargez la liste des utilisateurs.es",
                        "Supprimer un utilisateur",
                        "Modifier un.e admin",
                        "Messages"
                        "Quit"
                    ],
                }
            ]
    
        def display_info(self):
            with open("graphical_assets/art_admin.txt", "r", encoding="utf-8") as asset:
                print(asset.read())
    
        def make_choice(self):
            
            reponse = prompt(self.__questions)
            
            if reponse["choix"] == "Quit":
                from view.start_view import StartView
                return StartView()

            if reponse["choix"] == "Chargez la liste des utilisateurs.es": 
                tableau = Admin(shared_data.tab[0], shared_data.tab[1]).chargerToutLemonde()
                options = [
                {
                    "type": "list",
                    "name": "selected_items",
                    "message": "Select items:",
                    "choices": [
                        {
                            "name": f"{email}",
                            "value": email,
                        }
                        for email in tableau
                    
                    ],
                }
            
            ]
                res = prompt(options)
                print(res)
                
    
            elif reponse["choix"] == "Supprimer un utilisateur":
                pass
            
            elif reponse["choix"] == "Modifier un.e admin":
                pass

            elif reponse["choix"] == "Messages":
                pass
