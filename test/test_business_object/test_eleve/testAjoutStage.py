import sys
sys.path.insert(0,"D:/Cours/S1/Projet informatique 2A/Code ProjetInfo/Projet-Info-2A")
import metier.eleve


from unittest import TestCase, TextTestRunner, TestLoader
from metier.eleve import Eleve

class TestEleve(TestCase):
    
    #Tester la méthode ajouter_stageAuser()
    def test_ajouter_stageAuser(self):
        # Assurez-vous que l'étudiant ne possède pas déjà ce stage
        self.assertFalse(self.eleve.possede_stage(self.stage))

        # Ajoutez le stage et vérifiez s'il a été ajouté
        self.eleve.ajouter_stageAuser(self.stage)
        self.assertTrue(self.eleve.possede_stage(self.stage))

if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(
        TestLoader().loadTestsFromTestCase(TestEleve)
    )



