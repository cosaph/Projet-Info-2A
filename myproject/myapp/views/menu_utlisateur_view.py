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
        if not user_id:
            return redirect('connexion')
        
        user = User.objects.get(pk=user_id)
        action = request.POST.get('action')

        if action == 'recherche':
            # Implémentez la logique de recherche
            return redirect('page_recherche')
        elif action == 'historique':
            # Récupérez et gérez l'historique
            historique = Historique.objects.filter(user=user)
            return render(request, 'historique.html', {'historique': historique})
        elif action == 'modifier_compte':
            # Implémentez la logique de modification du compte
            return redirect('page_modification_compte')
        elif action == 'alertes':
            # Implémentez la logique d'alertes
            return redirect('page_alertes')
        elif action == 'signaler_stage':
            # Implémentez la logique de signalisation de stage
            return redirect('page_signaler_stage')
        else:
            return HttpResponse("Action non reconnue.")


# display_info: Retourne une chaîne de caractères indiquant que la vue est pour le menu utilisateur.     
# make_choice: Cette méthode gère les choix de l'utilisateur et le redirige vers la page correspondante.

# Lors de l'instanciation de cette classe, vous fourniriez le titre comme suit :
menu_utilisateur = MenuUtilisateurView("Menu Utilisateur")
