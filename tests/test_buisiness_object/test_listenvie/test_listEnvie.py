from unittest import TestCase, TextTestRunner, TestLoader
from Metier.listEnvie import ListEnvie
from Metier.stage import Stage 

class TestListEnvie(TestCase):

    #Tester la méthode __str__()
    def test___str__(self):
        # GIVEN
        stage = Stage()  
        liste = ListEnvie([stage])

        # WHEN
        resultat = liste.__str__()

        # THEN
        self.assertEqual(resultat, stage.__str__() + "\n")

        # Test avec une liste vide
        liste_vide = ListEnvie()
        
        # WHEN
        resultat_vide = liste_vide.__str__()

        # THEN
        self.assertEqual(resultat_vide, "Pas de stages dans la liste d'envie")

    #Tester la méthode ajouter_stage()
    def test_ajouter_stage(self):
        # GIVEN
        liste = ListEnvie()
        stage = Stage()  

        # WHEN
        liste.ajouter_stage(stage)

        # THEN
        self.assertIn(stage, liste.listStage)

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
