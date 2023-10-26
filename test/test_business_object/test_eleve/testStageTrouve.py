import sys
sys.path.insert(0,"D:/Cours/S1/Projet informatique 2A/Code ProjetInfo/Projet-Info-2A")
import metier.eleve


from unittest import TestCase, TextTestRunner, TestLoader
from metier.eleve import Eleve

class TestEleve(TestCase):
    
    #Tester la méthode set_stage_trouve()
    def test_set_stage_trouve(self):
        eleve = Eleve()  # Initialisez comme nécessaire
        eleve.set_stage_trouve(True)  # Indique que l'élève a trouvé un stage
        self.assertTrue(eleve.stage_trouve)  # Vérifiez que stage_trouve est vrai

if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(
        TestLoader().loadTestsFromTestCase(TestEleve)
    )





