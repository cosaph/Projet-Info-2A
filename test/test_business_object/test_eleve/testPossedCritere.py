import sys
sys.path.insert(0,"D:/Cours/S1/Projet informatique 2A/Code ProjetInfo/Projet-Info-2A")
import metier.eleve


from unittest import TestCase, TextTestRunner, TestLoader
from unittest.mock import patch
from metier.eleve import Eleve
from metier.critere import Critere  # Assurez-vous que c'est le bon import

class TestEleve(TestCase):
    
    @patch('metier.eleve.AssoCritUserDao.existe_user_crit')
    def test_possede_critere(self, mock_existe_user_crit):
        # GIVEN
        mock_existe_user_crit.return_value = True  
        eleve = Eleve(email='test@example.com', mdp='123456')
        
        # Créer un critère avec tous les arguments nécessaires
        critere = Critere(ville_cible='Paris', rayon_km=20, specialite='Informatique', duree_min=3, duree_max=6)
        
        # WHEN
        possede = eleve.possede_critere(critere)
        
        # THEN
        self.assertTrue(possede)

if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(
        TestLoader().loadTestsFromTestCase(TestEleve)
    )


