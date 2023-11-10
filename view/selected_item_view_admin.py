# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    selected_item_view_admin.py                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/08 19:52:57 by cosaph            #+#    #+#              #
#    Updated: 2023/11/10 22:16:36 by cosaph           ###   ########.fr        #
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

class selected_item_view_admin(AbstractView):
    
    def __init__(self, selected):
        self.selected = selected
        self.__questions = [
            {
                "type": "list",
                "name": "choice",
                "message": "Que voulez-vous faire ?",
                "choices": ["Supprimer l'utilisateur.e", "Retour"]
            }
        ]

    def display_info(self):
            with open("graphical_assets/art_admin.txt", "r", encoding="utf-8") as asset:
                print(asset.read())
    

    def make_choice(self):
        answers = prompt(self.__questions)
        dic = self.selected
        tableau = []
        tableau.append(dic)
        #tableau.append(dic["url_stage"])
        print(tableau)

        choice = answers["choice"]

        if choice == "Supprimer l'utilisateur.e":
            E = Eleve(tableau[0], None)
             # trouver un moyen de faire apparaître l'url.
            Admin(shared_data.tab[0], shared_data.tab[1]).supprime_user(E)

            from view.modifier_utilisateur import modifier_utilisateur
            return modifier_utilisateur()
             
        if choice == "Retour":
            from view.modifier_utilisateur import modifier_utilisateur
            return modifier_utilisateur()