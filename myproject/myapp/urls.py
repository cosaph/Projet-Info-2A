#Pour le fichier urls.py, il faut clarifier que les URL que vous configurez ici  sont les chemins internes à notre application Django. 
# Ces URL définissent comment les utilisateurs accèdent aux différentes vues de votre propre application. Elles n'ont rien à voir avec le site externe que vous scrappez.


from django.urls import path
from . import views

urlpatterns = [
    path('accueil/', views.AccueilView.as_view(), name='accueil'),
    path('connexion/', views.ConnexionView.as_view(), name='connexion'),
    path('menu_utilisateur/', views.MenuUtilisateurView.as_view(), name='menu_utilisateur'),
    # on peut ajouter d'autres chemins ici...
]
