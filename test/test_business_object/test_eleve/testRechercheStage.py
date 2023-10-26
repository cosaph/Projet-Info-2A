import sys
sys.path.insert(0,"D:/Cours/S1/Projet informatique 2A/Code ProjetInfo/Projet-Info-2A")
import metier.eleve


from unittest import TestCase, TextTestRunner, TestLoader
from metier.eleve import Eleve
from unittest.mock import patch

class TestEleve(TestCase):
    
    #Tester la méthode rechercher_stage()
    def test_rechercher_stage(self):
        eleve = Eleve()  # Initialisez comme nécessaire
        critere = Critere()  # Initialisez comme nécessaire

        # Mock du retour de la méthode `recherche_stage` de la classe `Critere`
        mock_return_value = [Stage(), Stage()]  # Assumez que Stage est une classe que vous avez définie
        with patch.object(Critere, 'recherche_stage', return_value=mock_return_value):
            # Assurez-vous que l'élève a des critères
            eleve.ajouter_critereAuser(critere)  

            # Test de la méthode
            result = eleve.rechercher_stage(critere)

        # Vérifiez que la méthode retourne une liste de stages
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), len(mock_return_value))

if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(
        TestLoader().loadTestsFromTestCase(TestEleve)
    )







    