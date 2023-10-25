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
