from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import User  # Remplacez par le bon import si nécessaire
from .abstract_view import AbstractView  # Assurez-vous que l'import est correct

# Vue de connexion 
class ConnexionView(AbstractView):
    
    def __init__(self, title):
        super().__init__(title)

    def display_info(self):
        return f"{self.title}: Veuillez vous connecter."

    def make_choice(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password).first()
        
        if user:
            request.session['user'] = user.id  # Stocke l'utilisateur dans la session
            request.session['role'] = user.role  # Supposant que vous avez un champ "role" dans votre modèle User!!!!!!!!!!!!!!!?
            return redirect('menu_utilisateur') # Redirige vers la vue du menu utilisateur
        else:
            return HttpResponse("Échec de la connexion.")


#Lors de l'instanciation de cette classe, vous fourniriez le titre comme suit:
connexion = ConnexionView("Page de Connexion")
