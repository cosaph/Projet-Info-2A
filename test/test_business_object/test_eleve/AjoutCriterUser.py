import sys
sys.path.insert(0,"D:/Cours/S1/Projet informatique 2A/Code ProjetInfo/Projet-Info-2A")
import metier.eleve


from unittest import TestCase, TextTestRunner, TestLoader
from metier.eleve import Eleve

class TestEleve(TestCase):
    
    # Tester la méthode ajouter_critereAuser()
    def test_ajouter_critereAuser(self):
        # GIVEN
        eleve = Eleve(email='test@example.com', mdp='123456')
        critere = Critere()  # Supposition
        # WHEN
        resultat = eleve.ajouter_critereAuser(critere)
        # THEN
        self.assertTrue(resultat)

if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(
        TestLoader().loadTestsFromTestCase(TestEleve)
    )


    