import sys
sys.path.insert(0,"D:/Cours/S1/Projet informatique 2A/Code ProjetInfo/Projet-Info-2A")
import metier.eleve


from unittest import TestCase, TextTestRunner, TestLoader
from metier.eleve import Eleve

class TestEleve(TestCase):
    
    #Tester la méthode supprimer_stageAuser()
    def test_supprimer_stageAuser(self):
        eleve = Eleve()  
        stage = Stage() 

        # Assurons-nous que l'étudiant possède ce stage
        eleve.ajouter_stageAuser(stage)
        result_before = eleve.possede_stage(stage)
        self.assertIsInstance(result_before, bool)
        self.assertTrue(result_before)

        # Supprimer le stage et vérifiez s'il a été supprimé
        eleve.supprimer_stageAuser(stage)
        result_after = eleve.possede_stage(stage)
        self.assertIsInstance(result_after, bool)
        self.assertFalse(result_after) 

if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(
        TestLoader().loadTestsFromTestCase(TestEleve)
    )



    