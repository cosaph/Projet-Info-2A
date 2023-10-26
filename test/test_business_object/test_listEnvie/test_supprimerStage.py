import sys
sys.path.insert(0,"/home/cosaph/ENSAI2A/projet")
import metier.eleve
from unittest import TestCase, TextTestRunner, TestLoader

from unittest import TestCase, TextTestRunner, TestLoader
from metier.listEnvie import ListEnvie
from metier.stage import Stage 

class TestListEnvie(TestCase):

    #Tester la méthode supprimer_stage()
    def test_supprimer_stage(self):
        # GIVEN
        stage = Stage()  
        liste = ListEnvie([stage])

        # WHEN
        liste.supprimer_stage(stage)

        # THEN
        self.assertNotIn(stage, liste.listStage)


if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner(verbosity=2).run(
        TestLoader().loadTestsFromTestCase(TestListEnvie)
    )
