import sys
sys.path.insert(0,"D:/Cours/S1/Projet informatique 2A/Code ProjetInfo/Projet-Info-2A")
import metier.eleve


from unittest import TestCase, TextTestRunner, TestLoader
from metier.eleve import Eleve

class TestEleve(TestCase):
    
        #Tester la méthode supprimer_compte()
    def test_supprimer_compte(self):
        # Créez et enregistrez un nouvel élève pour s'assurer qu'il existe dans la base de données
        eleve = Eleve()  # Initialisez comme nécessaire
        eleve.enregistrer()

        # Assurez-vous que l'élève existe dans la base de données
        self.assertTrue(eleve.existe())

        # Supprimez le compte
        eleve.supprimer_compte()

        # Vérifiez que le compte a été supprimé
        self.assertFalse(eleve.existe())

if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(
        TestLoader().loadTestsFromTestCase(TestEleve)
    )






