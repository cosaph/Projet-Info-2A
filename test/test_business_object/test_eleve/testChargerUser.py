import sys
sys.path.insert(0,"D:/Cours/S1/Projet informatique 2A/Code ProjetInfo/Projet-Info-2A")
import metier.eleve

from unittest import TestCase, TextTestRunner, TestLoader
from unittest.mock import patch
from metier.eleve import Eleve

class TestEleve(TestCase):
    
    @patch('metier.eleve.UserDao.charger_user')
    @patch('metier.eleve.AssoCritUserDao.exist_email')
    @patch('metier.eleve.AssoStageUserDao.exist_email')
    def test_charger_user(self, mock_exist_email_stage, mock_exist_email_crit, mock_charger_user):
        # GIVEN
        email = 'test@example.com'
        mdp = '123456'
        mock_charger_user.return_value = {
            'email': email,
            'mdp': mdp,
            'code_insee_residence': None,
            'souhaite_alertes': False,
            'profil': 'Eleve'
        }
        mock_exist_email_crit.return_value = False
        mock_exist_email_stage.return_value = False
        
        # WHEN
        eleve = Eleve.charger_user(email, mdp)
        
        # THEN
        self.assertIsInstance(eleve, Eleve)
        self.assertEqual(eleve.email, email)


if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(
        TestLoader().loadTestsFromTestCase(TestEleve)
    )
