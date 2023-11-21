# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    listedenvie.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/02 21:11:41 by cosaph            #+#    #+#              #
#    Updated: 2023/11/21 14:55:49 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from view.abstract_view import AbstractView
from InquirerPy import prompt
from metier.stage import Stage
from dao.stageDAO import StageDao
from view.session import Session
from metier.eleve import Eleve
import view.shared_data as shared_data
from metier.critere import Critere
from metier.admin import Admin
from metier.prof import Prof




class listedenvie(AbstractView):
    
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": "liste d'envie",
                "choices": [
                    "Consulter la liste d'envie",
                    "Exporter la liste d'envie",
                    "Retour"
                ],
            }
        ]

    def display_info(self):
        with open("graphical_assets/banner.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):

        reponse = prompt(self.__questions)

        if reponse["choix"] == "Retour":
            if shared_data.tab_ter[0] == "élève":
                from view.menu_post_connection import post_connection
                return post_connection()
            elif shared_data.tab_ter[0] == "professeur.e":
                from view.menu_post_connection_prof import post_connection_prof
                return post_connection_prof()
            elif shared_data.tab_ter[2] == "Administrateur.e":
                from view.menu_post_connection_admin import post_connection_admin
                return post_connection_admin()
        
        elif reponse["choix"] == "Consulter la liste d'envie":
            try:
                if shared_data.tab_ter[0] == "élève":
                    RealDictRow= Eleve(shared_data.tab_bis[0], shared_data.tab_bis[1]).charger_all_stage_mail(shared_data.tab_bis[0])
                    return self.make_choice()
                if shared_data.tab_ter[0] == "professeur.e":
                    RealDictRow = Prof(shared_data.tab_bis[0], shared_data.tab_bis[1]).charger_all_stage_mail(shared_data.tab_bis[0])
                    return self.make_choice()
                if shared_data.tab_ter[2] == "Administrateur.e":
                    RealDictRow = Admin("m", "m").charger_all_stage_mail(shared_data.tab_ter[0])
                    return self.make_choice()
            except:
                print("Vous n'avez pas de liste d'envie")
                return self.make_choice()
        
        elif reponse["choix"] == "Exporter la liste d'envie":
            try:
                if shared_data.tab_ter[0] == "élève":
                    message = Eleve(shared_data.tab_bis[0], shared_data.tab_bis[1]).charger_all_stage_mail_f(shared_data.tab_bis[0])
                    #print(message)
                    chaine = ""
                    for item in message:
                        chaine += item + "\n"
                    #print(chaine)
                    Admin("m", "m").envoi_mail_envie(shared_data.tab_bis[0], chaine)
                    print("Votre liste d'envie a été envoyé à votre adresse mail.")

                    return self.make_choice()

                elif shared_data.tab_ter[0] == "professeur.e":
                    message = Eleve(shared_data.tab_bis[0], shared_data.tab_bis[1]).charger_all_stage_mail_f(shared_data.tab_bis[0])
                    #print(message)
                    chaine = ""
                    for item in message:
                        chaine += item + "\n"
                    #print(chaine)
                    Admin("m", "m").envoi_mail_envie(shared_data.tab_bis[0], chaine)
                    print("Votre liste d'envie a été envoyé à votre adresse mail.")
                    return self.make_choice()

                elif shared_data.tab_ter[2] == "Administrateur.e":
                    Admin(shared_data.tab_ter[0], shared_data.tab_ter[1]).charger_all_stage_mail_json(shared_data.tab_ter[0])
                    return self.make_choice()

            except:
                print("Vous n'avez pas de liste d'envie")
                return self.make_choice()
