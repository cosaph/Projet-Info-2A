from InquirerPy import prompt
from .abstract_view import AbstractView

from InquirerPy import prompt
from .abstract_view import AbstractView  # Assurez-vous que l'import est correct

class MenuUtilisateurView(AbstractView):

    def __init__(self, title, role, message=""):
        super().__init__(title)
        self.role = role
        self.message = message
        self.set_questions()

    def set_questions(self):
        if self.role == 'eleve':
            self.questions = [
                {
                    "type": "list",
                    "name": "action",
                    "message": "Choisissez une action",
                    "choices": [
                        "Rechercher des stages",
                        "Consulter les stages appliqués",
                        "Se déconnecter"
                    ],
                }
            ]
        elif self.role == 'prof':
            self.questions = [
                {
                    "type": "list",
                    "name": "action",
                    "message": "Choisissez une action",
                    "choices": [
                        "Consulter la liste des élèves",
                        "Approuver les candidatures de stage",
                        "Se déconnecter"
                    ],
                }
            ]

    def display_info(self):
        print(f"{self.title}: Voici les actions que vous pouvez effectuer.")
        if self.message:
            print(self.message)

    def make_choice(self):
        answers = prompt(self.questions)
        
        if self.role == 'eleve':
            if answers["action"] == "Rechercher des stages":
                # Utilisez le DAO pour récupérer et afficher la liste des stages disponibles
                pass  
            elif answers["action"] == "Consulter les stages appliqués":
                # Utilisez le DAO pour récupérer et afficher les stages où l'élève a appliqué
                pass
            elif answers["action"] == "Se déconnecter":
                # Retournez à la page d'accueil
                pass
        
        elif self.role == 'prof':
            if answers["action"] == "Consulter la liste des élèves":
                # Utilisez le DAO pour récupérer et afficher la liste des élèves
                pass
            elif answers["action"] == "Approuver les candidatures de stage":
                # Utilisez le DAO pour récupérer et approuver les candidatures de stage
                pass
            elif answers["action"] == "Se déconnecter":
                # Retournez à la page d'accueil
                pass
