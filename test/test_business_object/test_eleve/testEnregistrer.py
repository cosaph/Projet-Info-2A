import sys
sys.path.insert(0,"D:/Cours/S1/Projet informatique 2A/Code ProjetInfo/Projet-Info-2A")
import metier.eleve


from unittest import TestCase, TextTestRunner, TestLoader
from metier.eleve import Eleve

class TestEleve(TestCase):

    #Tester la méthode enregistrer()
    def test_enregistrer(self):
        eleve = Eleve()  # Initialisez comme nécessaire

        # Vérifiez que l'élément n'existe pas encore
        self.assertFalse(eleve.existe())

        eleve.enregistrer()  # Appel de la méthode enregistrer

        # Vérifiez que l'élément existe maintenant
        self.assertTrue(eleve.existe()) 

if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(
        TestLoader().loadTestsFromTestCase(TestEleve)
    )
