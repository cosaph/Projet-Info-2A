from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import User, Historique  # Remplacez par les bons imports si nécessaire
from .abstract_view import AbstractView  # Assurez-vous que l'import est correct

class MenuUtilisateurView(AbstractView):

    def __init__(self, title):
        super().__init__(title)

    def display_info(self):
        return f"{self.title}: Voici les actions que vous pouvez effectuer."

    def make_choice(self, request):
        user_id = request.session.get('user')
        user_role = request.session.get('role')
        
        if not user_id:
            return redirect('connexion')
        
        if user_role == 'eleve':
            # Logique spécifique à l'élève
            pass

        elif user_role == 'prof':
            # Logique spécifique au prof
            pass
        
        elif user_role == 'admin':
            # Logique spécifique à l'administrateur
            pass
        else:
            return HttpResponse("Rôle non reconnu.")


# display_info: Retourne une chaîne de caractères indiquant que la vue est pour le menu utilisateur.     
# make_choice: Cette méthode gère les choix de l'utilisateur et le redirige vers la page correspondante.

# Lors de l'instanciation de cette classe, vous fourniriez le titre comme suit :
menu_utilisateur = MenuUtilisateurView("Menu Utilisateur")
