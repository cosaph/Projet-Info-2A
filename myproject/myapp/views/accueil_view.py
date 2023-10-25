from django.shortcuts import render, redirect
from django.http import HttpResponse
from .abstract_view import AbstractView
from metier.userNonAuthentifie import UserNonAuthentifie 

# Classe de vue pour l'accueil
class AccueilView(AbstractView):
    
    def __init__(self, title):
        super().__init__(title)
        self.user = None  # Initialisation d'un utilisateur non authentifié

    def display_info(self):
        return f"{self.title}: Bienvenue à l'application de recherche de stages."
        
    # Enregistre un utilisateur non authentifié dans la session
    def set_user(self, critere):
        self.user = UserNonAuthentifie(critere)
        
    # Récupère l'utilisateur en session s'il existe
    def get_user(self):
        return self.user

    def make_choice(self, request):
        # Vérifie si l'utilisateur est en session
        user = self.get_user()
        
        # Mettez ici le code pour interagir avec les autres classes métiers si nécessaire??????????!!!!!!!!!!
        
        return render(request, 'accueil.html', {'user': user})

# Instanciation avec un titre
accueil = AccueilView("Page d'accueil")

