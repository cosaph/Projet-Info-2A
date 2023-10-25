from InquirerPy import prompt
from abstract_view import AbstractView
from metier.eleve import Eleve 
from metier.prof import Prof  

class ConnexionView(AbstractView):

    def __init__(self, title, message=""):
        super().__init__(title)
        self.message = message
        self.questions = [
            {
                "type": "input",
                "message": "Nom d'utilisateur:",
                "name": "username",
            },
            {
                "type": "password",
                "message": "Mot de passe:",
                "name": "password",
            },
        ]

    def display_info(self):
        print(f"{self.title}: Veuillez vous connecter.")
        if self.message:
            print(self.message)
        
    def make_choice(self):
        answers = prompt(self.questions)
        
        # On appelle le service pour trouver l'utilisateur (élève ou prof)
        eleve = EleveService().se_connecter(answers["username"], answers["password"])
        prof = ProfService().se_connecter(answers["username"], answers["password"])
        
        if eleve:
            message = f"Vous êtes connecté en tant qu'élève {eleve.nom}"
            from .menu_eleve_view import MenuEleveView  # Assurez-vous que le chemin d'importation est correct
            return MenuEleveView(message)
        
        elif prof:
            message = f"Vous êtes connecté en tant que prof {prof.nom}"
            from .menu_prof_view import MenuProfView  # Assurez-vous que le chemin d'importation est correct
            return MenuProfView(message)
        
        else:
            message = "Erreur de connexion"
            from .accueil_view import AccueilView  # Assurez-vous que le chemin d'importation est correct
            return AccueilView(message)
