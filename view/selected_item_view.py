# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    selected_item_view.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cosaph <cosaph@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/02 15:11:45 by cosaph            #+#    #+#              #
#    Updated: 2023/11/21 15:00:30 by cosaph           ###   ########.fr        #
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
from view.menu_post_connection import post_connection
from metier.admin import Admin
from metier.prof import Prof



class selected_item_view(AbstractView):
    
    def __init__(self, selected):
        self.selected = selected
        self.__questions = [
            {
                "type": "list",
                "name": "choice",
                "message": "Que voulez-vous faire ?",
                "choices": ["Ajouter à la liste d'envie", "En savoir plus sur le stage", "Redirection vers le lien du stage" ,"Retour"]
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
            categorie = shared_data.tab[4]

            # RAJOUTER categorie.

            try:

                if shared_data.tab_ter[0] == 'élève':
                    Eleve(shared_data.tab_bis[0], shared_data.tab_bis[1]).ajouter_stageAuser(url, title, specialite, location,categorie)
                    print("Stage ajouté à votre liste d'envie")
                    return self.make_choice()
                elif shared_data.tab_ter[0] == 'professeur.e':
                    Prof(shared_data.tab_bis[0], shared_data.tab_bis[1]).ajouter_stageAuser(url, title, specialite, location, categorie)
                    print("Stage ajouté à votre liste d'envie")
                    return self.make_choice()
                elif shared_data.tab_ter[2] == 'Administrateur.e':
                    Admin(shared_data.tab_ter[0], shared_data.tab_ter[1]).ajouter_stageAuser(url, title, specialite, location, categorie)
                    print("Stage ajouté à votre liste d'envie")
                    return self.make_choice()
            except IndexError:
                print("Vous n'avez pas accès a cette fonctionnalité")
                return self.make_choice()
                
                
        elif choice == "Redirection vers le lien du stage":
            webbrowser.open(url) 
            return self.make_choice()
            
        elif choice == "En savoir plus sur le stage":

            tab = Critere.scrap_description(url)
            if tab == []:
                print("Pas de description disponible pour ce stage, possibilité de redirection vers l'url") 
                return self.make_choice()
            print("Description du stage :")
            print(tab[0])
            return self.make_choice()
            try:

                if shared_data.tab_ter[0] == 'élève':
                    from view.menu_post_connection import post_connection
                    return self.make_choice()
                elif shared_data.tab_ter[0] == 'professeur.e':
                    from view.menu_post_connection_prof import post_connection_prof
                    return self.make_choice()
                elif shared_data.tab_ter[2] == 'Administrateur.e':
                    from view.menu_post_connection_admin import post_connection_admin
                    return self.make_choice()
                else:
                    return self.make_choice()
            except IndexError:
                return self.make_choice()



        elif choice == "Retour":
            try:
                if shared_data.tab_ter[0] == 'élève':
                    from view.menu_post_connection import post_connection
                    return post_connection()
                elif shared_data.tab_ter[0] == 'professeur.e':
                    from view.menu_post_connection_prof import post_connection_prof
                    return post_connection_prof()
                elif shared_data.tab_ter[2] == 'Administrateur.e':
                    from view.menu_post_connection_admin import post_connection_admin
                    return post_connection_admin()
                from view.start_view import StartView
                return StartView()
            except IndexError:
                from view.start_view import StartView
                return StartView()
                

             
        