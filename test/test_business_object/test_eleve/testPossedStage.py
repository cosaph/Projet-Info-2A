import sys
sys.path.insert(0,"D:/Cours/S1/Projet informatique 2A/Code ProjetInfo/Projet-Info-2A")
import metier.eleve


from unittest import TestCase, TextTestRunner, TestLoader
from metier.eleve import Eleve

class TestEleve(TestCase):
    
    #Tester la méthode possede_stage()
    def test_possede_stage(self):
        eleve = Eleve()  # Initialisez comme nécessaire
        stage = Stage()  # Initialisez comme nécessaire
        result = eleve.possede_stage(stage)
        self.assertIsInstance(result, bool)

if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(
        TestLoader().loadTestsFromTestCase(TestEleve)
    )

 


