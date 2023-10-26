import sys
sys.path.insert(0,"D:/Cours/S1/Projet informatique 2A/Code ProjetInfo/Projet-Info-2A")
import metier.eleve


from unittest import TestCase, TextTestRunner, TestLoader
from metier.eleve import Eleve

class TestEleve(TestCase):
    
    #Tester la méthode set_souhaite_alertes()
    def test_set_souhaite_alertes(self):
        eleve = Eleve()  
        eleve.set_souhaite_alertes(True)  # Active les alertes
        self.assertTrue(eleve.souhaite_alertes)  # Vérifiez que les alertes sont actives


if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(
        TestLoader().loadTestsFromTestCase(TestEleve)
    )
 




   


    