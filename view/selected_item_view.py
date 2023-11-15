# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    selected_item_view.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/02 15:11:45 by cosaph            #+#    #+#              #
#    Updated: 2023/11/15 11:09:18 by cosaph           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from InquirerPy import prompt

from view.abstract_view import AbstractView
from metier.stage import Stage
from metier.critere import Critere
import view.shared_data as shared_data
from metier.eleve import Eleve
#from metier.nouveau_compte import creation
import webbrowser



class selected_item_view(AbstractView):
    
    def __init__(self, selected):
        self.selected = selected
        self.__questions = [
            {
                "type": "list",
                "name": "choice",
                "message": "Que voulez-vous faire ?",
                "choices": ["Ajouter à la liste d'envie", "En savoir plus sur le stage", "Retour"]
            }
        ]

    def display_info(self):
        print(f"Bonjour, veuillez choisir parmi les informations suivantes:")

    def make_choice(self):
        answers = prompt(self.__questions)
        choice = answers["choice"]
        selected_item = self.selected
        url = selected_item['url']



        if choice == "Ajouter à la liste d'envie":

            selected_item = self.selected

            title = selected_item['title']
            url = selected_item['url']
            
            #location = selected_item['location']
            location = shared_data.tab[2]
            #rayon = shared_data.tab[0]
            specialite = shared_data.tab[0]

            try:
                Eleve(shared_data.tab_bis[0], shared_data.tab_bis[1]).ajouter_stageAuser(url, title, specialite, location)
                return self.make_choice()
            except IndexError:
                print("Vous n'avez pas accès a cette fonctionnalité")
                return self.make_choice()
            
        if choice == "En savoir plus sur le stage":
            webbrowser.open(url) 
            if shared_data.tab_ter[0] == 'élève':
                from view.menu_post_connection import post_connection
                return post_connection()
            elif shared_data.tab_ter[0] == 'professeur.e':
                from view.menu_post_connection_prof import post_connection_prof
                return post_connection_prof()
            else:
                print("Vous n'avez pas accès a cette fonctionnalité")

        if choice == "Retour":
            if shared_data.tab_ter[0] == 'élève':
                from view.menu_post_connection import post_connection
                return post_connection()
            elif shared_data.tab_ter[0] == 'professeur.e':
                from view.menu_post_connection_prof import post_connection_prof
                return post_connection_prof()
            else:
                from view.start_view import StartView
                return StartView()
             
        

             
        