from django.shortcuts import render, redirect
from django.http import HttpResponse
from metier.eleve import Eleve 
from metier.prof import Prof 
from .abstract_view import AbstractView  # Assurez-vous que l'import est correct

class MenuUtilisateurView(AbstractView):

    def __init__(self, title):
        super().__init__(title)

    def display_info(self):
        return f"{self.title}: Voici les actions que vous pouvez effectuer."

    def make_choice(self, request):
        user_id = request.session.get('user_id')
        user_role = request.session.get('role')

        # Vérification de la session
        if not user_id:
            return redirect('connexion')

        if user_role == 'eleve':
            # Logique spécifique à l'élève
            # Exemple : Récupérer les recherches de stages ou les critères spécifiques
            pass

        elif user_role == 'prof':
            # Logique spécifique au prof
            # Exemple : Récupérer les stages proposés ou autres actions
            pass
        
        else:
            return HttpResponse("Rôle non reconnu.")

# Instanciation avec un titre
menu_utilisateur = MenuUtilisateurView("Menu Utilisateur")

