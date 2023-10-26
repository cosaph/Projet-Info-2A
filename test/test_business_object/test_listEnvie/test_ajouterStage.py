
import sys
sys.path.insert(0,"D:/Cours/S1/Projet informatique 2A/Code ProjetInfo/Projet-Info-2A")
import metier.eleve
from unittest import TestCase, TextTestRunner, TestLoader

from unittest import TestCase, TextTestRunner, TestLoader
from metier.listEnvie import ListEnvie
from metier.stage import Stage 

class TestListEnvie(TestCase):

    #Tester la méthode ajouter_stage()
    def test_ajouter_stage(self):
        # GIVEN
        liste = ListEnvie()
        stage = Stage()  

        # WHEN
        liste.ajouter_stage(stage)

        # THEN
        self.assertIn(stage, liste.listStage)


if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner(verbosity=2).run(
        TestLoader().loadTestsFromTestCase(TestListEnvie)
    )
