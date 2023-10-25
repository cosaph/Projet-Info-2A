from django.shortcuts import render, redirect
from django.http import HttpResponse
from .abstract_view import AbstractView

# Classe de vue pour l'accueil
class AccueilView(AbstractView):
    
    def __init__(self, title):
        super().__init__(title)

    def display_info(self):
        return f"{self.title}: Bienvenue à l'application de recherche de stages."
        
    def make_choice(self, request):
        # Votre logique ici
        pass

#Lorsque vous instancierez AccueilView, vous devrez fournir un titre :
accueil = AccueilView("Page d'accueil")
