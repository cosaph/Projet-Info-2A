import sys
sys.path.insert(0,"D:/Cours/S1/Projet informatique 2A/Code ProjetInfo/Projet-Info-2A")
import metier.eleve


from unittest import TestCase, TextTestRunner, TestLoader
from metier.eleve import Eleve

class TestEleve(TestCase):
    
    #Tester la méthode charger_all_critere
    def test_charger_all_critere(self):
        eleve = Eleve(email='test@example.com', mdp='123456')
        criteres = Eleve.charger_all_critere()
        self.assertIsInstance(criteres, list) 
    """    #Tester la méthode charger_all_critere_mail()
    def test_charger_all_stageAuser(self):
        eleve = Eleve()  # Initialisez comme nécessaire
        result = eleve.charger_all_stageAuser()
        self.assertIsInstance(result, list)
    for stage in result:
        self.assertIsInstance(stage, Stage)


    #Tester la méthode charger_all_stageAuser()
    def test_charger_all_stage_mail(self):
        result = Eleve.charger_all_stage_mail("email_exemple@gmail.com")
        self.assertIsInstance(result, list)
    for stage in result:
        self.assertIsInstance(stage, Stage)


    #Tester la méthode test_charger_all_stage_mail()
    def test_charger_all_stage_mail(self):
        result = Eleve.charger_all_stage_mail("email_exemple@gmail.com")
        self.assertIsInstance(result, list)
    for stage in result:
        self.assertIsInstance(stage, Stage)
        """

if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(
        TestLoader().loadTestsFromTestCase(TestEleve)
    )



   

    