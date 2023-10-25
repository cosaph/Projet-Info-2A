from InquirerPy import prompt
from view.abstract_view import AbstractView  # Remplacez par votre import correct
from metier.stage import Stage  # Import de la classe Stage
from dao.stageDAO import StageDao  # Import de la classe StageDao

class StageView(AbstractView):

    def __init__(self, message="") -> None:
        super().__init__(message)

    def choisir_menu(self):
        stage_dao = StageDao()

        # Supposons que vous ayez une liste de stages à afficher
        # (Vous devrez récupérer cette liste selon votre propre logique)
        stages = [...]  

        stage_choices = [stage.titre for stage in stages]
        stage_choices.append("Retour au Menu Utilisateur")

        self.questions = [
            {
                "type": "list",
                "name": "choix",
                "message": "Choisissez un stage",
                "choices": stage_choices,
            }
        ]

        reponse = prompt(self.questions)

        if reponse["choix"] == "Retour au Menu Utilisateur":
            from view.menu_utilisateur_view import MenuUtilisateurView
            return MenuUtilisateurView()

        else:
            # Trouver le stage choisi par l'utilisateur
            stage_choisi = next(stage for stage in stages if stage.titre == reponse["choix"])

            # Utilisation des méthodes disponibles dans Stage et StageDao
            if stage_choisi.existe():
                stage_choisi.modifier_stage()
            else:
                stage_choisi.enregistrer_stage()

            from view.menu_utilisateur_view import MenuUtilisateurView
            return MenuUtilisateurView()
