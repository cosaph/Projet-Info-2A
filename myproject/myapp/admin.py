#admin.py: Permet de définir ce qui sera visible et comment dans l'interface d'administration de Django.

from django.contrib import admin
from UserDao import UserDao
from dao.historique_dao import Historique
# Remplacez avec les chemins corrects des fichiers où vos modèles sont définis

# Personnalisation de l'interface admin pour le modèle User
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ['username', 'email']

# Personnalisation de l'interface admin pour le modèle Historique
class HistoriqueAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_recherche', 'critere')
    search_fields = ['user__username', 'date_recherche']

# Enregistrement des modèles dans l'interface d'administration
admin.site.register(User, UserAdmin)
admin.site.register(Historique, HistoriqueAdmin)



 #"personnaliser l'interface d'administration" signifie définir comment les modèles apparaissent et 
 # sont gérés dans l'interface d'administration de Django. Ceci inclut :
         #  Quels champs sont affichés dans la liste des enregistrements (list_display).
        #  Quels champs peuvent être utilisés pour rechercher des enregistrements (search_fields).


#le fichier admin.py ne définit pas les tâches de l'administrateur de l'application dans le sens métier t. Il sert
#  à configurer la manière dont les modèles sont affichés et interagis avec l'interface d'administration de Django. 
# Cette interface est surtout un outil de gestion des données de notre application pour des personnes avec 
# des permissions d'administrateur.