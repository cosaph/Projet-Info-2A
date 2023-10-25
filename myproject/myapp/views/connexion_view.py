from django.shortcuts import render, redirect
from django.http import HttpResponse
from .abstract_view import AbstractView  # Assurez-vous que l'import est correct
from metier.eleve import Eleve, Prof  # Remplacez par les imports corrects

# Classe de vue pour la connexion
class ConnexionView(AbstractView):

    def __init__(self, title):
        super().__init__(title)

    def display_info(self):
        return f"{self.title}: Veuillez vous connecter."

    def make_choice(self, request):
        email = request.POST.get('email')  # Récupération de l'email depuis le formulaire
        password = request.POST.get('password')  # Récupération du mot de passe depuis le formulaire

        eleve = Eleve.objects.filter(email=email, mdp=password).first()
        prof = Prof.objects.filter(email=email, mdp=password).first()

        if eleve:
            request.session['user_id'] = eleve.id
            request.session['role'] = 'eleve'
            return redirect('menu_utilisateur')
        
        elif prof:
            request.session['user_id'] = prof.id
            request.session['role'] = 'prof'
            return redirect('menu_utilisateur')
        else:
            return HttpResponse("Échec de la connexion.")

# Instanciation avec un titre
connexion = ConnexionView("Page de Connexion")

