# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    statistiques.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/10 09:52:23 by cosaph            #+#    #+#              #
#    Updated: 2023/11/19 21:59:01 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session
from metier.eleve import Eleve
from metier.prof import Prof
from dao.userDao import UserDao
from view.start_view import StartView
import view.shared_data as shared_data

class statistiques(AbstractView):
    
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Hello {Session().user_name}",
                "choices": [
                    "Liste d'élève qui ont trouvé un stage",
                    "Nombre d'élèves qui ont trouvé un stage",
                    "Retour"
                ],
            }
        ]

    def display_info(self):
        with open("graphical_assets/art_statistiques.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Retour":
            if shared_data.tab_ter[0] == 'professeur.e':
                from view.menu_post_connection_prof import post_connection_prof
                return post_connection_prof()
            else:
                from view.menu_post_connection_admin import post_connection_admin
                return post_connection_admin()
        if reponse["choix"] == "Liste d'élève qui ont trouvé un stage": 
            UserDao.tout_mail_stage_touve()
            if shared_data.tab_ter[0] == 'professeur.e':
                from view.menu_post_connection_prof import post_connection_prof
                return post_connection_prof()
            else:
                from view.menu_post_connection_admin import post_connection_admin
                return post_connection_admin()

        if reponse["choix"] == "Nombre d'élèves qui ont trouvé un stage":
            perso = UserDao.tout_mail_stage_touve_bis()
            somme = 0
            for k in perso:
                somme += 1
            print(f"Le nombre d'élèves qui ont trouvé un stage grâce à notre application est de {somme}")
            #print(shared_data.tab_ter[0])
            if shared_data.tab_ter[0] == 'professeur.e':
                from view.menu_post_connection_prof import post_connection_prof
                return post_connection_prof()
            else:
                from view.menu_post_connection_admin import post_connection_admin
                return post_connection_admin()


