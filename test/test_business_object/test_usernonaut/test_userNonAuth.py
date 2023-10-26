import sys
sys.path.insert(0,"/home/cosaph/ENSAI2A/projet")

import unittest
from metier.critere import Critere
from dao.userDao import UserDao
from metier.userNonAuthentifie import UserNonAuthentifie

class TestUserNonAuthentifie(unittest.TestCase):


    def test_creer_compte(self):
        #GIVEN
        mdp = "123456"
        email = "test@example.com"
        alerte = "oui"
        type = "eleve"

        #WHEN
        new_user = UserNonAuthentifie.creer_compte(mdp, email, alerte, type)
        
        #THEN
        self.assertIsNotNone(new_user)

"""     def test_supprimer_critereAuser(self):
        # Écrivez un test pour la méthode supprimer_critereAuser
        # Assurez-vous de couvrir les cas où la suppression réussit et échoue
        pass """

"""     def test_rechercher_stage(self):
        # Testez la méthode rechercher_stage avec différents scénarios

        # Cas où self.critere est None
        with self.assertRaises(Exception) as context:
            self.user_non_auth.rechercher_stage()
        self.assertEqual(str(context.exception), "Pas de critères pas de recherches")

        # Cas où critereChoix est None et self.critere est une instance de Critere
        result = self.user_non_auth.rechercher_stage()
        self.assertIsNotNone(result)

        # Cas où critereChoix est une instance de Critere
        critere_choix = Critere()  # Créez un objet Critere pour le test
        result = self.user_non_auth.rechercher_stage(critere_choix)
        self.assertIsNotNone(result)

        # Cas où critereChoix n'est pas une instance de Critere
        with self.assertRaises(Exception) as context:
            self.user_non_auth.rechercher_stage("mauvais_critere")
        self.assertEqual(str(context.exception), "Les paramètre saisi n'est pas un critère")
 """
if __name__ == "__main__":
    unittest.main()
